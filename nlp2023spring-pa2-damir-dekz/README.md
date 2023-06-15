# NLP_2023_Spring_PA2

## Assignment Statement

For this assignment, you will modify the a2_1.py, a2_2.py, and b.ipynb, c.ipynb files. To ensure the autograder works correctly, each .py file must have a main() method.

We have provided starter code in each file and strongly recommend that you use it. The code includes "TODO" and "DO NOT CHANGE" sections; you should only make changes in the "TODO" sections

To see autograder output: Open your repository -> Click Actions -> Click on last (or top) run -> Click Autograding -> Expand Testing step -> Analyze log output (view your scores or failing cases)

Tasks to complete:

### Task A: (Deadline Week 4)

**(Paper Based)**: Find the probability of message S1 being spam and not spam using Laplace smoothing:

| Training set                                                                                                                                                                                                                                                                                                             | Input message                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| Spam messages: <br>M1: Buy bicycles for free<br>M2: Bicycles and motorbikes for free<br>M3: Motorbikes rides easy and free<br>Normal messages:<br>M4: Let's go ride bicycles<br>M5: Last week I bought motorbikes and they are cool<br>M6: Some messages about bicycles and motorbikes, that are free, are spam messages | Cool bicycles and motorbikes |

Calculate Precision and recal, F1

|  | Selected as sport | Selected as politics | Selected as culture |
| --- | --- | --- | --- |
| Classified as sport | 200 | 20 | 30 |
| Classified as politics | 10 | 150 | 15 |
| Calculate as culture | 60 | 90 | 10 |

### Task B: (Deadline week 5)

[IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

Read CSV file and tokenize all texts. [https://spacy.io/usage/spacy-101#annotations-token](https://spacy.io/usage/spacy-101#annotations-token)

Read sentiment data (2020.tsv).

Use IMBD dataset and calculate positivity and negativity by mean_sentiment

Calculate precision and Recall, F1.

### Task C: (Deadline Week 5)

Use CountVectorizer, and implement Naive Bayes (without using ready projects) to classify messages.

Calculate precision, recall, and F1.

Use dataset from B task (IMBD dataset)


## Hints
- If you need a refresher on Python or Jupyter Notebooks, or are new to either of them, we strongly recommend reviewing [PA0](https://github.com/cs124/pa0-python-jupyter-tutorial) first.
- We've also provided a Numpy tutorial (numpy_tutorial.ipynb) with this assignment to help you practice numpy.
- You can see expected answers for A2 task in expected/a_2_2.csv, for other tasks in tasks_test.py
- You can see grading logic in tasks_test.py. But don't change it