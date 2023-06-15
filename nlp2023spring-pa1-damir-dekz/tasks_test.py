import json
import math
import unittest
import pandas as pd
import A_01
import B_01
import C_01
from upload_reports import report_file


# DO NOT CHANGE this file
class TestTasks(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.a = None
        self.b = None
        self.c = None

    def test_a01(self):
        A_01.main()
        actual_df = pd.read_csv("./result/A_01.csv").sort_values("name")
        expected_df = pd.read_csv("./expected/A_01.csv").sort_values("name")
        if 'gender' not in actual_df.columns:
            print(f'gender column was not found')
            self.a = 0
            return

        result_df = pd.merge(actual_df, expected_df, how="inner", on="name", suffixes=("_actual", "_expected"))
        fp = result_df[result_df['gender_actual'] != result_df['gender_expected']]
        fp = fp[fp['gender_expected'] != "U"]  # drop unknown genders
        expected_without_unknown = expected_df[expected_df['gender'] != "U"]
        wrong_count = fp.shape[0]
        self.a = math.ceil(100 - 100.0 * wrong_count / expected_without_unknown.shape[0])
        print(f'Score A (out of 100): {self.a}')
        print(f'Following students were incorrectly labeled: \n{fp}\n')

    def test_b01(self):
        B_01.main()

        # Assume the two files are named "expected.csv" and "actual.csv"
        expected_df = pd.read_csv("./expected/B_01.csv", names=["data"])
        actual_df = pd.read_csv("./result/B_01.csv", names=["data"])

        # Assume the column name is "data"
        expected = set(expected_df["data"])
        actual = set(actual_df["data"])

        # True positives
        tp = sorted(expected.intersection(actual))

        # False positives
        fp = sorted(actual - expected)

        # False negatives
        fn = sorted(expected - actual)

        # Calculate score
        self.b = math.ceil(len(tp) / (len(tp) + len(fp) + len(fn)) * 100)
        print("Score B (out of 100): ", self.b)
        print(f"""True Positives:
{tp}
False positives:
{fp}
False negatives:
{fn}
""")

    def test_c01(self):
        C_01.main()

        # Assume the two files are named "expected.csv" and "actual.csv"
        expected_df = pd.read_csv("./expected/C_01.csv", delimiter="|", names=['file', 'type', 'data'])
        actual_df = pd.read_csv("./result/C_01.csv", delimiter="|", names=['file', 'type', 'data'])

        # Assume the column name is "data"
        expected = set(expected_df.apply(tuple, axis=1).tolist())
        actual = set(actual_df.apply(tuple, axis=1).tolist())

        # Compute the true positives, false positives, and false negatives
        tp = actual.intersection(expected)
        fp = actual - expected
        fn = expected - actual

        print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp), len(fp), len(fn)))
        self.c = math.ceil(len(tp) / (len(tp) + len(fp) + len(fn)) * 100)
        print(f'Score C (out of 100): {self.c}')
        print(f"""True Positives:
{tp}
False positives:
{fp}
False negatives:
{fn}
""")

    def tearDown(self):
        try:
            with open(report_file, 'r') as infile:
                scores = json.load(infile)
        except Exception:
            scores = {}
        if self.a is not None:
            scores['a'] = self.a
        if self.b is not None:
            scores['b'] = self.b
        if self.c is not None:
            scores['c'] = self.c
        json_object = json.dumps(scores, indent=4)
        with open(report_file, 'w+') as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
    unittest.main()
