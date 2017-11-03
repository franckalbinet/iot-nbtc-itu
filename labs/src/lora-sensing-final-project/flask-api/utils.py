# Utility functions

from flask import request
import config

def get_params():
    params = {
        'station_name': config.DEFAULT_PARAMS['STATION_NAME'],
        'nb_measurements': config.DEFAULT_PARAMS['NB_MEASUREMENTS']
    }
    for key, value in params.iteritems():
        params[key] = request.args.get(key) or value
    return params
