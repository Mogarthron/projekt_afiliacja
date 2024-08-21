from flask import Flask, render_template
import json
import os


konta_bankowe = list()

for path in os.listdir():
    if path.endswith(".json") and path[:2] == "KB":
        with open(path, "r", encoding="utf8") as f:
            konto = json.load(f)
    
        konta_bankowe.append(konto)


app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():

    konta_promowane = [k for k in konta_bankowe if k["kontoPromowane"]]


    return render_template("index.html", konta_promowane=konta_promowane)

@app.route("/opis_produktu/<nazwa_konta>")
def opis_produktu(nazwa_konta):

    opis = [k for k in konta_bankowe if k["nazwa"] == nazwa_konta][0]
    

    return render_template("opis_produktu.html", nazwa_konta = nazwa_konta, warunki_przystoapienia_do_promocji=opis["warunkiPrzystoapieniaDoPromocji"])


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)