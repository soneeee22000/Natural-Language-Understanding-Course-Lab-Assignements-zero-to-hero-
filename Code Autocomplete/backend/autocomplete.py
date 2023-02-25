import torch
import torch.nn as nn
import math
import tokenize
import io

device = torch.device('cpu')

########## Loading Vocab ##########
vocab = torch.load('vocab_obj.pth')

########## Model ##########
class LSTMLanguageModel(nn.Module):
    def __init__(self, vocab_size, emb_dim, hid_dim, num_layers, dropout_rate):
                
        super().__init__()
        self.num_layers = num_layers
        self.hid_dim = hid_dim
        self.emb_dim = emb_dim

        self.embedding = nn.Embedding(vocab_size, emb_dim)
        self.lstm = nn.LSTM(emb_dim, hid_dim, num_layers=num_layers, 
                    dropout=dropout_rate, batch_first=True)
        self.dropout = nn.Dropout(dropout_rate)
        self.fc = nn.Linear(hid_dim, vocab_size)
        
        self.init_weights()
        
    def init_weights(self):
        init_range_emb = 0.1
        init_range_other = 1/math.sqrt(self.hid_dim)
        self.embedding.weight.data.uniform_(-init_range_emb, init_range_emb)
        self.fc.weight.data.uniform_(-init_range_other, init_range_other)
        self.fc.bias.data.zero_()
        for i in range(self.num_layers):
            self.lstm.all_weights[i][0] = torch.FloatTensor(self.emb_dim,
                    self.hid_dim).uniform_(-init_range_other, init_range_other) 
            self.lstm.all_weights[i][1] = torch.FloatTensor(self.hid_dim, 
                    self.hid_dim).uniform_(-init_range_other, init_range_other) 

    def init_hidden(self, batch_size, device):
        hidden = torch.zeros(self.num_layers, batch_size, self.hid_dim).to(device)
        cell   = torch.zeros(self.num_layers, batch_size, self.hid_dim).to(device)
        return hidden, cell
    
    def detach_hidden(self, hidden):
        hidden, cell = hidden
        hidden = hidden.detach()
        cell = cell.detach()
        return hidden, cell

    def forward(self, src, hidden):
        #src: [batch size, seq len]
        embedding = self.dropout(self.embedding(src))
        #embedding: [batch size, seq len, emb_dim]
        output, hidden = self.lstm(embedding, hidden)      
        #output: [batch size, seq len, hid_dim]
        #hidden = h, c = [num_layers * direction, seq len, hid_dim)
        output = self.dropout(output) 
        prediction = self.fc(output)
        #prediction: [batch size, seq_len, vocab size]
        return prediction, hidden

vocab_size = len(vocab)
emb_dim = 1024
hid_dim = 1024
num_layers = 2
dropout_rate = 0.65

model = LSTMLanguageModel(vocab_size, emb_dim, hid_dim, num_layers, dropout_rate)

########## Loading Learned Weights ##########
path = './best-val-auto.pt'
model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))


tok_name = tokenize.tok_name
def python_code_tokenizer(content):
    tokenized_code = []
    
    try:
        for token in tokenize.generate_tokens(io.StringIO(content).readline):
            encoding = tok_name[token.type]
            if encoding == "COMMENT" or encoding== "NL":
                continue
            elif encoding == "NUMBER":
                tokenized_code.append("<NUMBER>")
            elif encoding == "STRING":
                tokenized_code.append("<STRING>")
            else:
                tokenized_code.append(token.string)
    except:
        return []
    
    return tokenized_code

########## Inference ##########
def generate(prompt, max_seq_len, temperature, model, tokenizer, vocab, device, seed=None):
    if seed is not None:
        torch.manual_seed(seed)
    model.eval()
    tokens = tokenizer(prompt)
    indices = [vocab[t] for t in tokens]
    batch_size = 1
    hidden = model.init_hidden(batch_size, device)
    with torch.no_grad():
        for i in range(max_seq_len):
            src = torch.LongTensor([indices]).to(device)
            prediction, hidden = model(src, hidden)
            
            #prediction: [batch size, seq len, vocab size]
            #prediction[:, -1]: [batch size, vocab size] #probability of last vocab
            
            probs = torch.softmax(prediction[:, -1] / temperature, dim=-1)  
            prediction = torch.multinomial(probs, num_samples=1).item()    
            
            while prediction == vocab['<unk>']: #if it is unk, we sample again
                prediction = torch.multinomial(probs, num_samples=1).item()

            if prediction == vocab['<eos>']:    #if it is eos, we stop
                break

            indices.append(prediction) #autoregressive, thus output becomes input

    itos = vocab.get_itos()
    tokens = [itos[i] for i in indices]
    return tokens

def get_code_suggestions(prompt):
    max_seq_len = 30
    seed = 0

    code_suggestion = []
    temperatures = [0.5, 0.7, 0.75, 0.8, 1.0]
    for temperature in temperatures:
        generation = generate(prompt, max_seq_len, temperature, model, python_code_tokenizer, 
                            vocab, device, seed)
        code_suggestion.append(' '.join(generation))
    
    return code_suggestion