#!/usr/bin/python

####################
# Gateway simple API
####################

# Using Flask micro web framework http://flask.pocoo.org/
# Flask quick start http://flask.pocoo.org/docs/0.11/quickstart/
# Install:
#   - via pip: `pip install Flask`
#   - export FLASK_APP=api.py
# Run:
#   - `flask run --host=0.0.0.0`
# Data:
#  - csv file expected
# Activate Debug mode:
#   - `export FLASK_DEBUG=1`

from flask import Flask
from flask import jsonify
import pandas as pd
import os

import config
import utils

app = Flask(__name__)

file = os.path.join(config.FILE_PATH, config.FILE_NAME)

@app.route('/gateway/api')
def get_data():
    params = utils.get_params()
    nb_measurements = int(params['nb_measurements'])
    station_name = params['station_name']

    nb_lines = sum((1 for i in open(file, 'rb')))
    skiprows = max(0, nb_lines - nb_measurements)

    data_df = pd.read_csv(file, header=None, skiprows=skiprows,
                          names=config.CSV_COLUMN_NAMES)
    
    data_df.dropna(inplace=True)

    if (station_name):
        data_df = data_df[data_df['station_name'] == station_name]

    return jsonify(data_df.T.to_dict().values())
