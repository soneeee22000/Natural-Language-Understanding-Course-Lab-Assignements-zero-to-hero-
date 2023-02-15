#I need to create two functions to parse the resume and extract the information from the resume. 
# The first function is preprocessing which is to tokenize the input sentences 
# The second funciton is to extract the unique skills and education 
# and the third funciton being the main function which calls the first two 

# Importing the libraries
import pandas as pd 
#import numpy as np #if needed
import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from PyPDF2 import PdfReader  #to read the pdf file


# Importing the dataset
nlp = spacy.load('en_core_web_sm') #loading the spacy model
skill_path = 'static\pattern_data\education_skill.jsonl'

ruler = nlp.add_pipe("entity_ruler", before="ner") #adding the entity ruler to the spacy model
ruler.from_disk(skill_path) #loading the skills file
#path to the skills file

#let's preprocess the resume data 
#remove the stop words and punctuations
#lowercase the words
#let's create a function to preprocess the resume data
def preprocessing(sentence):
    
    stopwords = list(STOP_WORDS)
    doc = nlp(sentence)
    cleaned_tokens = []
    
    for token in doc:
        if token.text not in stopwords and token.pos_ != 'PUNCT' and token.pos_ != 'SPACE' and \
            token.pos_ != 'SYM':
                cleaned_tokens.append(token.lemma_.lower().strip())
                
    return " ".join(cleaned_tokens)



#let's create a function to extract the unique skills from the resume

def unique_skills_and_education(doc):
    skills    = []
    education = []

    for ent in doc.ents:
        if ent.label_ == 'SKILL':
            skills.append(ent.text)
        elif ent.label_ == 'EDUCATION':
            education.append(ent.text)
    
    # Convert from set to list type
    education_list = list(set(education))
    # Reverse list to display education in order
    education_list.reverse()
    return set(skills), education_list

#combine the two functions to create the main parsing resume function

def extract_skills_education(filePath):
    reader = PdfReader(filePath)
    number_of_pages = len(reader.pages)

    # Extract text from uploaded resume from all pages
    text = ''
    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text += ' ' + page.extract_text() 
    
    # Clean text
    text = preprocessing(text)

    # Tokenize text
    doc = nlp(text)

    # Get unique skills and eduation
    skills, education = unique_skills_and_education(doc)

    return skills, education
    



