import json
import os
import unittest

import pandas as pd

import a2_1
import a2_2
from upload_reports import report_file

epsilon = 1e-8


# DO NOT CHANGE this file
def is_equal(expected: float, actual: float):
    return abs(expected - actual) < epsilon


def print_score(score: int, task: str):
    print(f'\nScore for {task}: {score}\n')


class TestTasks(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.a_1 = None
        self.a_2 = None
        self.b = None
        self.c = None

    def test_a2_1(self):
        actual = a2_1.main()
        expected = 0.5713454459332822
        if is_equal(expected, actual):
            self.a_1 = 100
        else:
            self.a_1 = 0
            print(f'Expected probability: {expected}, actual: {actual}')
        print_score(self.a_1, 'A1')

    def test_a2_2(self):
        a2_2.main()

        expected_df = pd.read_csv("./expected/a_2_2.csv")
        actual_df = pd.read_csv("./result/a_2_2.csv")

        incorrect_calculations = []
        categories = expected_df.pop("Category")
        metrics = expected_df.columns
        actual_df.pop("Category")
        for row_index in range(expected_df.shape[0]):
            for column_index in range(expected_df.shape[1]):
                expected = expected_df.iloc[row_index, column_index]
                actual = actual_df.iloc[row_index, column_index]
                if not is_equal(expected, actual):
                    incorrect_calculations.append((categories[row_index], metrics[column_index], actual, expected))
        self.a_2 = int((1.0 - len(incorrect_calculations) / len(categories) / len(metrics)) * 100)
        for cat, met, actual, expected in incorrect_calculations:
            print(f'For {cat} the {met} is: {actual}, expected: {expected}')
        print_score(self.a_2, 'A2')

    def test_b2(self):
        os.system("jupyter nbconvert --to python b.ipynb")
        import b
        expected_f1 = 0.696171009309244
        base_line = 0.6
        actual_f1 = b.f1
        if b.f1 >= (expected_f1 - epsilon):
            self.b = 100
        else:
            self.b = max(100 * (actual_f1 - base_line) / (expected_f1 - base_line), 0)
            print(f'Expected f1 score: {expected_f1}, actual f1 score: {actual_f1}')
        print_score(self.b, 'B')
        os.remove('./b.py')

    def test_c2(self):
        os.system("jupyter nbconvert --to python c.ipynb")
        import c
        actual_f1 = c.f1
        expected_f1 = 0.8438280166435506
        if actual_f1 >= (expected_f1 - epsilon):
            self.c = 100
        else:
            self.c = 0
            print(f'Expected f1 score: {expected_f1}, actual f1 score: {actual_f1}')
        print_score(self.c, 'C')
        os.remove('./c.py')

    def tearDown(self):
        try:
            with open(report_file, 'r') as infile:
                scores = json.load(infile)
        except Exception:
            scores = {}
        if self.a_1 is not None:
            scores['a_1'] = self.a_1
        if self.a_2 is not None:
            scores['a_2'] = self.a_2
        if self.b is not None:
            scores['b'] = self.b
        if self.c is not None:
            scores['c'] = self.c
        json_object = json.dumps(scores, indent=4)
        with open(report_file, 'w+') as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
    unittest.main()
