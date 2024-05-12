from flask import Flask, render_template
import json

with open("konta_promowane.json", "r", encoding="UTF8") as f:
    konta_promowane = json.load(f)

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():

    return render_template("index.html", konta_promowane=konta_promowane["kontaPromowane"])

@app.route("/opis_produktu/<nazwa_konta>")
def opis_produktu(nazwa_konta):

    return render_template("opis_produktu.html", nazwa_konta = nazwa_konta)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)