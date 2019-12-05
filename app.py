import logging
import os
import requests

from flask import Flask, request, jsonify, render_template

piserver   = os.getenv('PISERVER')
piusername = os.getenv('PIUSERNAME')
pipassword = os.getenv('PIPASSWORD')

print('piserver={}, piusername={}, pipassword={}'.format(piserver, piusername, pipassword))

app = Flask(__name__)

@app.route("/")
def baseendpoint():
    logging.debug('serving...')
    return render_template('index.html',
                           categories=['foo'],
                           data=[['bar']])

@app.route("/data")
def dataendpoint():
    logging.debug('serving data...')
    return jsonify({"categories": ['foo'], "data": [['bar']]})


app.run(host='0.0.0.0', port=8080)
