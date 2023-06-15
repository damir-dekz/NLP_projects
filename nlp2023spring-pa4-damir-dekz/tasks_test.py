import json
import os
import unittest
import math

from upload_reports import report_file


# DO NOT CHANGE this file

def print_score(score: int, task: str):
    print(f'\nScore for {task}: {score} out of 100\n')


class TestTasks(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.pa4 = None

    def test_pa4(self):
        os.system("jupyter nbconvert --to python pa4.ipynb")
        import pa4
        self.pa4 = pa4.final_score
        print_score(self.pa4, 'pa4')
        os.remove('./pa4.py')

    def tearDown(self):
        try:
            with open(report_file, 'r') as infile:
                scores = json.load(infile)
        except Exception:
            scores = {}
        if self.pa4 is not None:
            scores['pa4'] = self.pa4
        json_object = json.dumps(scores, indent=4)
        with open(report_file, 'w+') as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
    unittest.main()
