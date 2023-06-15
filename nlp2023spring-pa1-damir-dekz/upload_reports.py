import json
import os
import gspread
import pandas as pd

# DO NOT CHANGE this file
report_file = './report.json'

# DO NOT CHANGE
def upload_to_google_sheet():
    try:
        with open(report_file, 'r') as infile:
            scores = json.load(infile)
    except Exception as e:
        print(f'Error while reading:\n{e}')
        return

    os.remove(report_file)
    print(f'Uploading scores: {scores}')

    js = r"""{  "type": "service_account",  "project_id": "elevated-codex-376213",  "private_key_id": "30abf3ad88f055c1966b44293caaf45035ff810c",  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC3t2qXovgpUzAK\nAMGm9AU8uL9oi7yH5tlj8mCrsJV9FoDFO8O1WhN0lcYko0syU/Z+NiwJLpvqvaKY\nFTdgcerguia8NhMYxInN1rMcqolDJe9VmfhSvKW0Y2dv7lfUpWdPSQf/A1ARAXtu\nqV+W09xtc5tRKsjnEfRSDLkiKWjl09JCxzN4fTOaxwSPq5roaDu9qwzIt8V2Yea8\nVeVvDkyMzoswuOfXzo2FAffiQ5c1TFi4fg9s4tVvFFHAtM08fL9aiS+bYMhLQG0K\n3LVhIkyoIyiHmscW0AFqfKP63Gx4Tn/s4/CakiMgFhLML8JMoZ66OTLo1Lt/WYwe\nvM4C0pfLAgMBAAECgf9ug+ebUG34bhJ38fyMcj60SG7cdTL0jeo4NZXxskg6905/\nV3Rjo8wQVgjcAV8650dgpTXYUDF7BJjK4/hsDBs/FLw4fE8AlzpOmNkmZXAs9KUE\n2ZqIKvODkEipDLfJM7bx+vzUaym/ESUvbLQUB16SePj12scAOcy/jufPpRl1JvF5\nrly+aTs7QOfDU12bBTZUxaD74knz0CAYU/fschwhAQsqIWa4Aw643UafOZ1WjRkc\nQU0ZOJHQMspa0Nrz0FGOaaC+wBEK9Dkh4/jLLAPzdBL64kuWeTLgGjtjQp9PanBM\nxfIqU+GH4/JJdKUyXTMu7m5RScNZIKtzGIGXBjECgYEA7BCW2DKh4m0sDyuePCnp\nA6jhn0sjtUTLum068TDb3C0YlFBDWg+OZCh+VIl+PtNvCUG8sL+eg64ITXXaRHGH\n2E4Osa2fE3a7+M9gQbA/lxn+MhWs1zYVSih8X3XfWL42b1lB0Hn23fhrHUCoZ07/\n1dGM1wfj+KEwr8NM0fhnEKUCgYEAxzsgAMziAfrt2RqGgcSBLy9pFCFMIRbR41Gt\nIl7BWCVW7J9WsPEfSWNLHzaxAQEsYKZgRSdpcUgU/Lk48D41SILziU2LKYmtkgLH\nFXZ2+YG6iAKfWXu2FW5iKsUAYpIidMojYQ+HPr2ogOL22D5ylHdqgbLcrdyt0Wxz\nYfdAq68CgYEA2cfwMeJ8QLUxGYnHAIA1rR+njtq2RawDO6k74HmPzA96hpGJoVOK\nrNJCweDarEFJRcP0vSb6qUbr9/JK/Cu1BJP2sGqZwE4g2kkO52sfL1pWjYQ7oYwO\nlgzFuRe4hlltRMqWkiuC2YMt5p3Y/v39vhgFk/d+lMi4bt6BR5CgHNUCgYA6UzLR\nSSm5Dq7m6f8Kqm5vU9/dRso0vauAcv7OmxLbLUM/Tn5gmpZgM7NgVfCHrMJDITH5\nzMnvofyS596lZnDO45dMUOk2pdmsbye9PsshzDrBapMf7TmnGIOgpb+xG7r+mda1\nqYgcdAWKhedh8xY0JKmHgsdcFsjEEI3O1kWWfQKBgQCljl0l0WxModMslpjK8g51\nkJZtCECY9/K+EvdaEoJfKKvbI+OPHA/1pQZ7YloLmkPFuxl4QtvinhrA+a37aDZ0\nF7NTGP+oXLUQkzWNg+v2gWzifjGdnfdGW0nslUPFblP6DhalvM+GYaRJ8WkSg6L6\n8ScxPbjYc4kKLTAIvByJJA==\n-----END PRIVATE KEY-----\n",  "client_email": "autograder-mukhtar@elevated-codex-376213.iam.gserviceaccount.com",  "client_id": "100774428268066672430",  "auth_uri": "https://accounts.google.com/o/oauth2/auth",  "token_uri": "https://oauth2.googleapis.com/token",  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/autograder-mukhtar%40elevated-codex-376213.iam.gserviceaccount.com"}"""
    owner = "".join(os.environ["OWNER"].split("/")[1:])
    print(f'Reporter: {owner}')

    sa = gspread.service_account_from_dict(info=json.loads(js, strict=False))
    sh = sa.open("NLP2023_Leaderboard")
    wks = sh.worksheet("HW1")
    data = wks.get('A2:E100')
    df = pd.DataFrame(data, columns=['name', 'a', 'b', 'c', 'total'])
    df["total"] = df["total"].astype('float64')
    df["a"] = df["a"].astype('int64')
    df["b"] = df["b"].astype('int64')
    df["c"] = df["c"].astype('int64')
    df.fillna({'a': 0, 'b': 0, 'c': 0, 'total': 0.0}, inplace=True)

    # upsert new scores
    mask = df['name'] == owner
    if mask.sum() == 0:
        # name not found, insert a new row with default values
        default_data = {'name': owner, 'a': 0, 'b': 0, 'c': 0}
        default_data.update(scores)
        a = default_data['a']
        b = default_data['b']
        c = default_data['c']
        default_data['total'] = a * 0.3 + b * 0.3 + c * 0.4
        df = df.append(default_data, ignore_index=True)
    else:
        # name found, update existing row
        a = df.loc[mask, 'a'].values[0] if 'a' not in scores else scores['a']
        b = df.loc[mask, 'b'].values[0] if 'b' not in scores else scores['b']
        c = df.loc[mask, 'c'].values[0] if 'c' not in scores else scores['c']
        df.loc[mask, 'a'] = a
        df.loc[mask, 'b'] = b
        df.loc[mask, 'c'] = c
        df.loc[mask, 'total'] = a * 0.3 + b * 0.3 + c * 0.4

    df.sort_values(by="total", ascending=False, inplace=True)
    wks.update('A2:E100', df.values.tolist())
    print("Scores are uploaded")


if __name__ == "__main__":
    upload_to_google_sheet()
