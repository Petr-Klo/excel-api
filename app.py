from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return 'Excel API is running!'

@app.route('/json_process', methods=['POST'])
def json_process():
    data = request.get_json()
    df = pd.DataFrame(data)
    
    # Add a column with row-wise sum of numeric columns
    df['Total'] = df.select_dtypes(include='number').sum(axis=1)
    
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run()
