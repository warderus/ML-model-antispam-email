import pandas as pd

from transformers import BertTokenizer, BertForSequenceClassification
from flask import Flask, jsonify, request

# Вопрос в каком виде импортировать модель через метод from_pretrained()
tokenizer = BertTokenizer.from_pretrained('/content/drive/MyDrive/hw/toLoad/model_spam')
model =BertForSequenceClassification.from_pretrained('/content/drive/MyDrive/hw/toLoad/model_spam')


app = Flask(__name__)


@app.route("/antispam", methods=["POST"])
def antispam():
    X = request.get_json()
    # Вопрос в каком виде и каким методом отправлять данные в модель
    preds = model.predict_proba(pd.DataFrame(X, index=[0]))[0, 1]
    result = {"answer": preds}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
