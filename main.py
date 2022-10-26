import requests
import pandas as pd


def cemantix():

    
    url = "https://cemantix.certitudes.org/score"
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
            "Accept": "*/*",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-origin",
            "Content-Type": "application/x-www-form-urlencoded",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
    }
    body = {"word": "barbe"}

    data = requests.post(url=url, headers=headers, data=body)
    print(data.json())

print("Downloading dictionnary...")
lex = pd.read_csv("http://www.lexique.org/databases/Lexique383/Lexique383.tsv", sep="\t")
print("Done.")

#https://chrplr.github.io/openlexicon/datasets-info/

print("Selecting proper words from dictionnary...")
mots = []
for mot in lex['lemme']:
    if not (mot in mots):
        mots.append(mot)
print("Done.")


if __name__ == "__main__":
    cemantix()