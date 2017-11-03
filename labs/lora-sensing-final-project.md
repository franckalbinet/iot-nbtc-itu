> [Internet of Things (IoT) | Training Course](lora-sensing-final-project.md) ▸ **LoRa sensing | Final project**

# LoRa sensing | Final project

## Table of content

[1. Introduction](#introduction)

[2. Learning outcomes](#learning-outcomes)

[3. Required components](#required-components)

[4. Introduction to data analysis with Pandas](#introduction-to-data-analysis-with-python)

[5. LoRa node setup](#lora-node-setup)

[6. Setting up the Raspberry LoRa Gateway](#setting-up-the-raspberry-lora-gateway)

[7. Setting up the Flask API](#setting-up-the-flask-api)

[8. Exercises](#exercises)

## Introduction
In this lab. we will consider the following setup:

![](https://i.imgur.com/OIY6tBP.png)

where:
* LoPys on Pysense boards will make measurements and send it over LoRa;
* then a Raspberry Pi and its LoRa expansion board once received, will serve them through an API;
* last, client machine(s) will fetch measurements via the API and anlyze it (using Jupyter Notebooks).

To be clear, again, communication between IoT nodes (Lopys + Pysense expansion boards) and the Raspberry PI (used as a LoRa gateway) will be ensured via LoRa. As regards, communication between the client machines and the Raspberry PI, it will be ensured via WiFi in a LAN. 

An example use case might be a farm where you deploy dozens of sensors to monitor temperature, humidity, soil moisture, CO2, ... in agricultural fields, aggregate the measurements in a Gateway and then analyze, monitor, decide using analytical platforms (here Jupyter Notebooks and Python).

## Learning outcomes
This lab. will allow to recap most of the components seen so far in a realistic use case. Once the base/reference architecture implemented, you will be asked to further improve it for instance by adding a simple notification system or any ideas you might consider relevant and use your creativity.

## Required Components

For this example you will need:

- LoPy(s) module plugged into a Pysense board
- a microUSB cable
- a development PC
- a Raspberry Pi 3
- a Raspberry LoRa expansion board

The source code is in the [`src/lora-sensing-final-project`](https://github.com/franckalbinet/iot-uaa-isoc/tree/master/labs/src/lora-sensing-final-project) directory.

## Introduction to data analysis with Python
Our ultimate goal in that lab. is to monitor/analyse data collected in the field, conveyed over LoRa and fetched from an API into a Jupyter notebook.

Python ecosystem includes many packages for data analysis, machine learning and deep learning. In Python data science, **Pandas** http://pandas.pydata.org is a must. We will use Pandas package for both data analysis and the Flask API (see below).

A Jupyter notebook is provided here: [`src/lora-sensing-final-project/notebooks/1-intro-to-pandas.ipynb`](src/lora-sensing-final-project/notebooks/1-intro-to-pandas.ipynb)

Launch `Anaconda` and the `Jupyter` notebook.

## LoRa node setup
We will start with the LoRa node setup. This is pretty straighforward as this is something we have seen already. We will just access Pycom's Pysense Python lib to get measurements and send it as LoRa packets.

You will find the source code in the following folder: [`src/lora-sensing-final-project`](src/lora-sensing-final-project)

Below the code of `main.py` file:

```python
import network
from network import LoRa
import binascii
import socket
import machine
import time
import binascii
from pysense import Pysense
from SI7006A20 import SI7006A20
import pycom
import micropython
from machine import RTC

import sys
import utils # utilities module with CRC calculation

# CONFIGURATION
NODE_NAME = '__YOUR_NODE_NAME__'

# Initialize LoRa in LORA mode.
freq=868000000                  # def.: frequency=868000000
tx_pow=14                       # def.: tx_power=14
band=LoRa.BW_125KHZ             # def.: bandwidth=LoRa.868000000
spreadf=8                       # def.: sf=7
prea=8                          # def.: preamble=8
cod_rate=LoRa.CODING_4_5        # def.: coding_rate=LoRa.CODING_4_5
pow_mode=LoRa.ALWAYS_ON         # def.: power_mode=LoRa.ALWAYS_ON
tx_iq_inv=False                 # def.: tx_iq=false
rx_iq_inv=False                 # def.: rx_iq=false
ada_dr=False                    # def.: adr=false
pub=False                        # def.: public=true
tx_retr=1                       # def.: tx_retries=1
dev_class=LoRa.CLASS_A          # def.: device_class=LoRa.CLASS_A

lora = LoRa(mode=LoRa.LORA,
        frequency=freq,
        tx_power=tx_pow,
        bandwidth=band,
        sf=spreadf,
        preamble=prea,
        coding_rate=cod_rate,
        power_mode=pow_mode,
        tx_iq=tx_iq_inv,
        rx_iq=rx_iq_inv,
        adr=ada_dr,
        public=pub,
        tx_retries=tx_retr,
        device_class=dev_class)

# Get loramac as id to be sent in message
lora_mac = binascii.hexlify(network.LoRa().mac()).decode('utf8')

# Create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# mr add 27/07
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# Creating temp/hum object
py = Pysense()
tempHum = SI7006A20(py)

count_tx = 0

# tx loop
while True:
    s.setblocking(True)

    temperature = tempHum.temp()
    humidity = tempHum.humidity()

    template = '{},{},{:.2f},{:.1f},{}'
    msgtx = template.format(str(count_tx),
                            lora_mac,
                            temperature,
                            humidity,
                            NODE_NAME)

    msgtx = msgtx

    print(msgtx)

    s.send(msgtx)
    print('Tx: {} is sending data ...'.format(lora_mac))

    count_tx += 1

    time.sleep(2)
```

Take a few moments to review the code provided. At this stage of the training should not be too challenging.

## Setting up the Raspberry LoRa Gateway
> [Optional] If you want to reproduce Raspberry PI installation we are using, you can refer to the following tutorial [setting-up-a-raspberry.md](setting-up-a-raspberry.md)

The Raspberry Pi will be used in that setup as a LoRa Gateway.

To run the LoRa Gateway you will have to:

1. connect via SSH to the Raspberry
2. run the following command: `sudo ./gateway` in `/raspi-lora-gateway` folder


## Setting up the Flask API

Write `export FLASK_APP=api.py` in a console.

In folder `/flask-api`, run `flask run --host=0.0.0.0`

Get the Raspberry Pi IP address: `hostname -I` for instance 192.168.1.101

Open your browser, you should be able to get data dumped by the LoRa Gateway by writing this URL `http://192.168.1.101:5000/gateway/api` (you might need to update the IP address).


```python
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
```

Let's analyse it a bit.

We first import required packages:

```python
from flask import Flask # Flask is a web microframework
from flask import jsonify # jsonify allows to handle JSON data-intechange format
import pandas as pd # Pandas for data manipulation
import os

import config # Configuration parameters 
import utils # Utility functions
```

We create the Flask app.:

`app = Flask(__name__)`

The we define a route and associated action:

```python
@app.route('/gateway/api') # This @ symbol allows to define a decorator - will be introduced during lab.
def get_data(): # Association action
  ...
```
Let's make it more concrete. 
When you write in your Browser `http://192.168.1.101:5000/gateway/api?nb_measurements=100&station_name=Monitoring station A`

The `get_data` function is called and we:
```python
def get_data():
    params = utils.get_params() # Retrieve the query string parameters: nb_measurements, station_name, ...
    nb_measurements = int(params['nb_measurements']) # Get the nb of measurements and convert it to integer
    station_name = params['station_name'] # Retrieve station name

    # The LoRa gateway logs measurement in a file (appending measurements to the end of file), we hence want
    # to retrieve only the last X measurements (actually the number you pass in your query string
    nb_lines = sum((1 for i in open(file, 'rb'))) # A one liner to count the nb of lines in log files written by LoRa gateway
    skiprows = max(0, nb_lines - nb_measurements) # Calculate the nb of lines to skip in order to get the last proper number of lines

    # We load the csv file as a Pandas dataframe
    data_df = pd.read_csv(file, header=None, skiprows=skiprows,
                          names=config.CSV_COLUMN_NAMES)
    
    # Drop any problematic line 
    data_df.dropna(inplace=True)

    # Filter out measurements by station name
    if (station_name):
        data_df = data_df[data_df['station_name'] == station_name]

    # And return data of interest in a JSON format
    return jsonify(data_df.T.to_dict().values())
```

## Exercises
A Jupyter notebook to complete is provided here: [`src/lora-sensing-final-project/notebooks/2-data-analysis-and-more.ipynb`](src/lora-sensing-final-project/notebooks/2-data-analysis-and-more.ipynb)

1. Run the Lopy node, the LoRa Gateway and the API and try to fetch data from a Jupyter notebook. The notebook: ... will guide you through the several steps.

2. Try to implement a notification system where for instance, when temperature exceeds 29.5 degrees, an sms or notification via MQTT is sent [No guidance here, this is free style].



