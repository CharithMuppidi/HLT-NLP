# HLT-NLP
This is a portfolio for CS 4395 - Human Language Technologies.

## Assignment 0: Getting Started

I set up this portfolio and made and an [overview of NLP](Overview_of_NLP.pdf).

## Assignment 1: Text Processing with Python

The [program](assignment1.py) will read a csv file that contains the following fields: last name, first name, middle initial, ID, and phone number. These fields will be saved in the Person class. It will then process the text so that the first letter in each part of the name is captalized, the ID is in 'AB1234' form, and the phone number is in '123-456-7890' form. If either the ID or phone number is in the incorrect form, it will ask the user to insert the info the correct way. After processing, the person will be added to a dictionary, and this dictionary will be stored in a pickle file. Finaly, we will unpickle the file and use the Person class's display() method to output the information about each person.

To run the program, atleast on windows, open up the terminal, enter the command "cd (filepath)", then enter "python assignment1.py data/data.csv".

The main strength that Python has when it comes to text processing is that its syntax lends itself to its ease of use. Its weaknesses are its has limitations. For example, the PorterStemmer() tends to take off parts of the root word because it thinks it is part of the suffix. While Lemmatizer() tends to fix this problem, it has a longer runtime compared to the stemmer.

What I learned about python is how simple it is to execute many actions with the language. To get specific indexes, you can just simply type "list[si:ei]" to get the specific elements you need to see, rather than in Python you make a for loop to access those indexes. I also got review some python basics such as how to use loops and if statements in Python.

## Assignment 2: NLTK
I experimented with nltk [here](Exploring_NLTK.ipynb).

## Assignment 3: Guessing Game
I implemented a word guessing game, more commonly known as [hangman](hangman.py).

## Assignment 4: WordNet
I got to experiment with [WordNet](Wordnet.ipynb).

## Assignment 5: Ngrams
I, along with a partner, made 2 progams and a narrative. In [program 1](Program1.py), we created bigram and unigram dictionaries for English, French, and Italian. In [program 2](Program2.py), we compute the probabilities for each language. For a refresher on Ngrams, please refer to our [narrative](NgramProjectNarrative.docx).

## Assignment 6: Finding or Building a Corpus
I, along with a partner, made a [program](corpus.py) to create a knowledge base for a [future chatbot](CS_4395_Webcrawler_Report.docx).

## Assignment 7: Syntax Parsing
I experimented with [syntax parsing](Syntax_Parsing.pdf).

## Assignment 8: Author Attribution
We used Machine Learning and the Scikit-learn library on the federalist papers to [attribute](AuthorAttribution.ipynb) who wrote each essay.
