from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/json_process", methods=["POST"])
def process_json():
    content = request.get_json()
    operation = content.get("operation")
    data = content.get("data")
    
    df = pd.DataFrame(data)

    if operation == "discount":
        df["DiscountedPrice"] = df["Price"] * 0.9
    elif operation == "total":
        df["Total"] = df.select_dtypes(include="number").sum(axis=1)
    elif operation == "summary":
        return jsonify(df.describe().to_dict())

    return jsonify(df.to_dict(orient="records"))
