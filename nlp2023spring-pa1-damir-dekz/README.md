# NLP_2023_Spring_PA1

## Assignment Statement

For this assignment, you will modify the A_01.py, B_01.py, and C_01.py files. To ensure the autograder works correctly, each file must have a main() method.

We have provided starter code in each file and strongly recommend that you use it. The code includes "TODO" and "DO NOT CHANGE" sections; you should only make changes in the "TODO" sections. Additionally, the expected folder contains the expected (valid) .csv files that the autograder will use to test your code.

To see autograder output: Open your repository -> Click Actions -> Click on last (or top) run -> Click Autograding -> Expand Testing step -> Analyze log output (view your scores or failing cases)

Tasks to complete:

- Task A: Use Pandas (optional) to read student names from the ./data/StateGrants.csv file. Write a regular expression that can identify girls and boys in the list. The output should be written to the ./result/B_01.csv file and should include the student's full name and gender ("M" or "F").

- Task B: In the BBC-Fulltext file, find all proper names (e.g. names, surnames, company names). The output should be written to the ./result/B_01.csv file, which should have one field only, containing the found elements.

- Task C: In the spam lord file, find all phone numbers and email addresses using regular expressions. The output should be written to the ./result/C_01.csv file, which should have three fields: the filename, the type (email = "e" or phone = "p"), and the actual email or phone (separated by "|"). For example: "ashishg|e|ashishg@stanford.edu".

## Hints
- If you need a refresher on Python or Jupyter Notebooks, or are new to either of them, we strongly recommend reviewing [PA0](https://github.com/cs124/pa0-python-jupyter-tutorial) first.
- We've also provided a Regular Expressions tutorial (regular_expressions_tutorial.ipynb) with this assignment to help you practice regular expressions.
- For Task B, even if you reach 50 points, it's okay. It can be difficult to score 100.
- For Task C, if you're new to this, it may be helpful to first complete [PA1](https://github.com/cs124/pa1-regular-expressions) before writing your solution in C_01.py.