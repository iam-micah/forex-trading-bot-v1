import defs
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

session = requests.Session()
instrument = 'EUR_USD'
count = 10
granularity = 'H1'
url = f'{defs.OANDA_URL}/instruments/{instrument}/candles'

params = dict(
    count=count,
    granularity=granularity,
    price='MBA'
)


@app.route('/oanda-data')
def get_oanda_data():
    response = session.get(url, headers=defs.SECURE_HEADER, params=params)
    return response.json()
    # data = {"price": "1.2345", "time": "2020-01-01T00:00:00.000000000Z"}
    # return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
