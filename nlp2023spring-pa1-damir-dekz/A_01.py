import pandas as pd
import re


def find_sex_f(row):
    if re.search(r'[вн]а\b|[кқг]ызы\b', row[0].lower()):
        return 'F'
    if re.search(r'[уұ]лы\b|\w+вич\b|\w+[ое]в\b', row[0].lower()):
        return 'M'
    else:
        return 'U'


def add_gender(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: Implement your approach here!

    df['gender'] = df.apply(find_sex_f, axis=1)
    return df


# DO NOT CHANGE
def main():
    """
    Below the starter code that uses pandas.
    You can write you own logic, but it's not recommended
    """
    df = pd.read_csv("./data/StateGrants.csv", names=["name"])
    df = add_gender(df)
    df.to_csv("./result/A_01.csv", index=False)
    print(df.head())


if __name__ == "__main__":
    main()
