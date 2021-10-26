from algorithms import *
from flask import Flask, render_template, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


def get_candles(df, df_pred):
    data = []
    data_pred = []
    try:
        for row in df_pred.iterrows():
            row_data = {'date': row[1]['Datetime'], 'close': row[1]['Close']}
            data_pred.append(row_data)
        for row in df.iterrows():
            row_data = {'date': row[1]['Datetime'], 'close': row[1]['Close']}
            data.append(row_data)
    except Exception as e:
        print(e)
    return [data, data_pred]


@app.route('/getJson/<ticker>', methods=['GET'])
def get_json_data(ticker='BTC-INR'):
    df, df_pred = crypto_data(ticker, '3mo', "60m")  # get last 3 months data with 60min interval
    df = df.dropna()
    df.reset_index(inplace=True)
    df['Datetime'] = df['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    # To be implemented for other algorithms
    pred_LSTM, rmse_lstm = lstm(df)

    array = df[['Close']].to_numpy(dtype='float')
    final = np.append(array, pred_LSTM)
    df_pred['Close'] = final.tolist()
    df_pred.reset_index(inplace=True)
    df_pred['Datetime'] = df_pred['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

    response = jsonify(get_candles(df, df_pred.tail(15)))   # last 13 hrs data for pred
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/', methods=['GET'])
def index():
    return render_template('plot.html')


@app.errorhandler(Exception)
def internal_error(error):
    code = 500
    print(error.args)
    if isinstance(error, HTTPException):
        code = error.code
    return '', code


app.run(host="0.0.0.0", port=5000, debug=True)  # ssl_context="adhoc"
