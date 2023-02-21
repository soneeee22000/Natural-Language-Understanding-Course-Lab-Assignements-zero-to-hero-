# Sentiiment Analysis

## How to run

- pip install flask praw matplotlib
- python app.py
- pip install -U spacy
- python -m spacy download en_core_web_md --- might already satisfied
- python app.py--- as usual on run this on localhost

## About The Project

A web application using Flask was used to do sentiment analysis on Reddit posts. Originally supposed to use Twitter api but, it's so cliche and the permission policy might have changed due to recent shift in CEO position.  To do sentiment analysis, a model was trained using 'Stanford Sentiment Treebank'. My friend "Abhinav" and I, we were walking thorugh training the dataset (using the SST2 dataset ,of course) but, it doesn't perform very well.For instance, it can easily analyze / classify whether it's positive or negative. But, when it comes to double negative or so positive negative : the results weren't necessarily promising ! ( it can't identify at all ) I learned that , we can do so much to solve this problem. There are so many ways to solve this problem since it's very common to occur in sentiment analysis. Many reasons leading to this problem could be not enough double negatives in the training dataset, limiting our model's abillity to correctly classfiy them.

Solution to solve this problem could be : 

* to fine-tune our model using a larger dataset that includes more examples of double negatives. We can search for other sentiment analysis datasets that contain double negatives or create our own by manually labeling a set of double negative examples.
* Alternatively, we could use data augmentation techniques to generate synthetic double negative examples from our existing dataset.
* Another solution is to use a more advanced machine learning technique or model architecture. For instance, we could try using a recurrent neural network (RNN) or a transformer-based model like BERT, which has shown to be effective in handling complex language patterns like double negatives. Furthermore, we could explore using pre-trained language models like GPT or RoBERTa and fine-tune them for our sentiment analysis task.
* Finally, it is also essential to ensure that our evaluation metrics are appropriate for our use case. If correctly classifying double negatives is critical to your task, we might consider using a more stringent evaluation metric, such as F1 score, instead of accuracy. This way, we can ensure that our model is not just correctly identifying positive and negative sentiments but also handling double negatives as well.



It is explored further in 'Sentiment_Analysis_PSK.ipynb' file. In this file, double negation and negative positive sentence test(finally resolved) was also performed to test the model. 'reddit_sentiment_analysis.ipynb' file shows how the models works sentiment analysis task on Reddit posts (on a certain Subreddit.)

## References

PRAW tutorial

- https://medium.com/geekculture/how-to-extract-reddit-posts-for-an-nlp-project-56d121b260b4
- https://pythonprogramming.net/introduction-python-reddit-api-wrapper-praw-tutorial/

# Demo of the Running Application

#### Home Page

![homepage](https://user-images.githubusercontent.com/28766535/219431802-e1b71180-4054-4334-966e-5caf60100152.png)

#### Sentiment Analysis Page

![result page 1](https://user-images.githubusercontent.com/28766535/219431866-e85e6c4d-2985-42f5-a9ac-0dd48ffc6d55.png)
![result page 2](https://user-images.githubusercontent.com/28766535/219431883-f69beb74-cfe4-4017-9bbf-a47d22c2943f.png)
![result page 3](https://user-images.githubusercontent.com/28766535/219431893-6a5c2180-0d54-434b-9a4d-7dfd61f95135.png)
