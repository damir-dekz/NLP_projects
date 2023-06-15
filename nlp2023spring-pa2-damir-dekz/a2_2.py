import pandas as pd
import numpy as np


def precision(confusion_matrix, category: int):
    true_p = confusion_matrix[category][category]
    false_p = np.sum(confusion_matrix[:, category]) - true_p
    print(false_p)
    return true_p / (true_p + false_p)
# The precision function calculates the precision of a binary classifier for a given category.
# Precision is a measure of the accuracy of the positive predictions, defined as the number of true positive predictions
# (i.e., instances correctly predicted as positive) divided by the total number of positive predictions made by the classifier.


def recall(confusion_matrix, category: int):
    true_p = confusion_matrix[category][category]
    false_p = np.sum(confusion_matrix[category]) - true_p
    return true_p / (true_p + false_p)
# The recall function calculates the recall of a binary classifier for a given category.
# Recall is a measure of the completeness of the positive predictions,
# defined as the number of true positive predictions divided by the total number of actual positive instances for the category.


def f1_score(precision: float, recall: float):
    return 2 * (precision * recall) / (precision + recall)
#he f1_score function calculates the F1 score, which is the harmonic mean of precision and recall.
# The F1 score is a single metric that summarizes the precision and recall of a binary classifier.
# It is commonly used as a performance metric for binary classification problems,
# as it balances the trade-off between precision and recall.


# DO NOT CHANGE
def calculate_metrics(confusion_matrix, category_labels):
    n_categories = confusion_matrix.shape[0]
    precision_array = np.zeros(n_categories)
    recall_array = np.zeros(n_categories)
    f1_array = np.zeros(n_categories)
    for i in range(n_categories):
        precision_array[i] = precision(confusion_matrix, i)
        recall_array[i] = recall(confusion_matrix, i)
        f1_array[i] = f1_score(precision_array[i], recall_array[i])
    df = pd.DataFrame(
        {'Category': category_labels, 'Precision': precision_array, 'Recall': recall_array, 'F1-score': f1_array})
    return df


# DO NOT CHANGE
def calculate_metrics_df(df: pd.DataFrame):
    category_labels = df.columns
    confusion_matrix = df.to_numpy()
    print(confusion_matrix)
    return calculate_metrics(confusion_matrix, category_labels)


# DO NOT CHANGE
def main():
    df = pd.read_csv('./data/a_2_2.csv')
    print(df)
    metrics_df = calculate_metrics_df(df)
    metrics_df.to_csv("./result/a_2_2.csv", index=False)


if __name__ == "__main__":
    main()
