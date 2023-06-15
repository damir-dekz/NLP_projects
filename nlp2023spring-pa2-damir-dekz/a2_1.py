import json
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


with open('./data/a_2_1.json', "r") as f:
    data: dict = json.load(f)
corpus = data["normal_messages"] + data["spam_messages"]
y = [0] * len(data["normal_messages"]) + [1] * len(data["spam_messages"])
input_message = data["input_message"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
df.index = y
df = df.T
df['total'] = df.sum(axis=1)

spam = df[1].copy()
spam['total'] = spam.sum(axis=1)

nspam = df[0].copy()
nspam['total'] = nspam.sum(axis=1)
print(nspam)

prob_s = len(data["spam_messages"]) / len(corpus)
prob_ns = len(data["normal_messages"]) / len(corpus)

sum_bow = df['total'].to_dict()
term_occurences = df['total'].sum()

sum_bow_s = spam['total'].to_dict()
sum_bow_ns = nspam['total'].to_dict()

term_occurences_s = spam['total'].sum()
term_occurences_ns = nspam['total'].sum()

unique_term = len(df.index)
prob_bow = {}
for key in sum_bow:
    prob_bow[key] = sum_bow[key]/term_occurences


def probSpam(email):
    email = email.lower().split()
    likelihood = 1
    evidence = 1
    for term in email:
        if term in sum_bow_s:
            likelihood *= (sum_bow_s[term] + 1) / (term_occurences_s + unique_term)
        else:
            likelihood *= 1 / (term_occurences_s + unique_term)
        evidence *= prob_bow[term]
    likelihood_prior = likelihood * prob_s
    posterior = likelihood_prior / evidence
    return posterior


def probNotSpam(email):
    email = email.lower().split()
    likelihood = 1
    evidence = 1
    for term in email:
        if term in sum_bow_ns:
            likelihood *= (sum_bow_ns[term] + 1) / (term_occurences_ns + unique_term)
        else:
            likelihood *= 1 / (term_occurences_ns + unique_term)
        evidence *= prob_bow[term]
    likelihood_prior = likelihood * prob_ns
    posterior = likelihood_prior / evidence
    return posterior


def main() -> float:
    email_spam = float(probSpam(input_message))
    email_nspam = float(probNotSpam(input_message))
    if email_nspam > email_spam:
        print('NOT SPAM')
        return email_nspam / (email_nspam + email_spam)
    elif email_nspam < email_spam:
        print('SPAM')
        return email_spam / (email_nspam + email_spam)


if __name__ == "__main__":
    print(main())

