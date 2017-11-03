# Configuration file for IoT gateway API

FILE_PATH = '../raspi-lora-gateway'
FILE_NAME = 'packets.csv'

CSV_COLUMN_NAMES = ['time', 'channel', 'snr', 'rssi',
                    'freq_error', 'bytes', 'packet_idx',
                    'lora_mac', 'temperature', 'humidity',
                    'station_name']


DEFAULT_PARAMS = {'STATION_NAME': None, 'NB_MEASUREMENTS': 10}
