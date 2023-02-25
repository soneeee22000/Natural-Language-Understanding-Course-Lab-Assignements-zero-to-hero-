# Code Autocomplete

## About Project

About this project, we are going to creat a web app for suggesting code completions primarily for Pytorch code. This was done so by training a model to do code generation on the given Python code. This is explored in 'auto complete psk.ipynb' file. File, 'backup_test.ipynb' contains the code used in Flask, especially in 'autocomplete.py', for suggesting code to complete the current Python code. Currently, the model is not giving good suggestions for code completion suggesting that better training, model, and/or dataset processing need to be done to get good code completion suggestions.

## Technologies used for Web App

`<b>`Frontend `</b>`

- React( But , not good at all so, might have to run to my friend Abinav to understand )

`<b>`Backend `</b>`

- Flask(getting used to this)

## Data

To train our model, we are going to use 'codeparrot-clean' dataset from CodeParrot organization. The dataset was meant to train models for code generation. Since the main emphasis is given to Pytorch code generation, all first 1000 repo suspected to contain Pytorch code were extracted for model training.

## Note

to note that Flask server run on port 5000 due to the proxy setting in package.json in React and also because the React app is hosted on port 3000. So, I learned.

## Demo

`<b>`Starting Page `</b>`
![starting page](https://user-images.githubusercontent.com/28766535/220980681-f28d755f-98c9-4011-811f-d32b8287741a.png)

`<b>`Suggesting Potention Code Completion after Python Code Input `</b>`
![Code Suggestion after Python Code Input](https://user-images.githubusercontent.com/28766535/220980908-faeca274-034e-48c5-a6d1-a7fd07b0445b.png)

## References

- https://stackoverflow.com/questions/62166362/how-to-tokenize-python-code-using-the-tokenize-module - Tokenizing Python code
- https://www.youtube.com/watch?v=7LNl2JlZKHA - Creating Flask - React Project
- https://dev.to/ondiek/sending-data-from-react-to-flask-apm - For sending data from React to Flask.
- https://stackoverflow.com/questions/61245215/saving-vocabulary-object-from-pytorchs-torchtext-library - Saving torch object
