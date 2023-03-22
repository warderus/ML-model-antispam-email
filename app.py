import pandas as pd

from transformers import BertTokenizer, BertForSequenceClassification
from flask import Flask, jsonify, request


tokenizer = BertTokenizer.from_pretrained('model_spam')
model =BertForSequenceClassification.from_pretrained('model_spam')


app = Flask(__name__)


@app.route("/antispam", methods=["POST"])
def antispam():
    X = request.get_json()
    preds = model.predict_proba(pd.DataFrame(X, index=[0]))
    result = {"answer": preds}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
