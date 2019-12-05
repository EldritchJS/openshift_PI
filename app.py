import argparse
import logging
import os
import requests

from flask import Flask, request, jsonify, render_template

parser = argparse.ArgumentParser(description='PI Server Interface')
parser.add_argument('--piserver', help='PI server address', default='piserver')
parser.add_argument('--username', help='PI server username', default='piuser')
parser.add_argument('--password', help='PI server password', default='piuserpassword')
args = parser.parse_args()

piserver   = os.getenv('', args.piserver)
piusername = os.getenv('', args.username)
pipassword = os.getenv('', args.password)

print('piserver={}, piusername={}, pipassword={}'.format(piserver, piusername, pipassword))

app = Flask(__name__)

@app.route("/")
def ahahah():
    logging.debug('serving...')
    return render_template('index.html',
                           categories=['foo'],
                           data=[['bar']])

@app.route("/data")
def dataonly():
    logging.debug('serving data...')
    categories, data = top(request)
    data.insert(0, "counts")
    return jsonify({"categories": ['foo'], "data": [['bar']]})


app.run(host='0.0.0.0', port=8080)
