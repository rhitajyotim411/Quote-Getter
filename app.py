import pandas as pd
from flask import Flask, render_template, request
import base64, pyttsx3, zipfile, io

app = Flask(__name__)

archive = zipfile.ZipFile('quotes.zip', 'r')
fl = io.BytesIO(archive.read('quotes.csv'))
df = pd.read_csv(fl, dtype="string").dropna()
# Dataset from kaggle


def ado(qt):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.runAndWait()
    engine.save_to_file(qt, 'speech.mp3')
    engine.runAndWait()

    data = str(base64.b64encode(open("speech.mp3", "rb").read()))[2:-1]
    # encoded string inside b'...' thus slicing required
    return 'data:audio/mpeg;base64,' + data


def quote(cat):
    a = [cat in i for i in df.category]
    df_cat = df.loc[a]

    while True:
        rnd_qt = df_cat.sample()
        qt = rnd_qt.quote.values[0]

        if(len(qt) < 450):
            break

    ath = rnd_qt.author.values[0]
    return qt, ath


@app.route('/quote', methods=['POST'])
def getQuote():
    cat = request.form['cat']
    qt, ath = quote(cat)
    url = ado(qt)
    return render_template('qt.html', qt=qt, ath=ath, url=url, opt=cat)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
