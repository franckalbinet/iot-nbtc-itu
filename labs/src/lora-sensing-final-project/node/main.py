# ---------------------------------------------------
# tx messages with lora-mac
# see:
# loramac
# https://docs.pycom.io/pycom_esp32/pycom_esp32/tutorial/includes/lora-mac.html
# https://forum.pycom.io/topic/934/lora-stats-documentation-is-missing-the-parameter-must-passed/2


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
NODE_NAME = 'Monitoring station A'

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
# pub=True                        # def.: public=true
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
