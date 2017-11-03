
> [Internet of Things (IoT) | Training Course](setting-up-a-raspberry.md) ▸ **Setting up a Raspberry PI 3**

## Setting up a Raspberry PI 3
This tutorial is optional and will outline the installation required steps including:

[1. Copying an Ubuntu Mate image to an SD card](#copying-the-ubuntu-mate-image)

[2. Installing Ubuntu Mate](#installing-ubuntu-mate)

[3. Enabling SSH](#enabling-ssh)

[4. Identifying IP address](#identifying-the-ip-address)

[5. Installing Mosquitto MQTT (clients, publishers and broker)](#installing-mosquitto)

[6. Setting up a LoRa Gateway (with LoRa expansion board)](#setting-up-a-lora-gateway)

[7. Setting up a Flask API](#setting-up-a-flask-api)

[8. Running the LoRa gateway and API](#running-the-lora-gateway-and-api)

## Copying the Ubuntu Mate image

Ubuntu Mate can be downloaded here: https://ubuntu-mate.org/raspberry-pi/ This link also includes guidance on how to extract and copy the image to an SD card using for instance Win32 Disk Imager if you are using a Windows OS. This video shows how to use Win32 Disk Imager: https://www.youtube.com/watch?v=WCrNIyhPXcs

The steps below outline how to do so under MAC OSX (http://terraltech.com/copying-an-image-to-the-sd-card-in-mac-os-x/):

```console
# Install .xz unarchiver
brew install xz

# Unarchive
xz -d ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz

# Displays disk usage information based on file system (ie: entire drives, attached media, etc)
# First without connecting the SD card to USB, list devices
df -h

# Connect your SD card and noticed the added device in the list: for instance: "/dev/disk1s1"
df -h

# Unmount the partition so that you will be allowed to overwrite the disk
sudo diskutil unmount /dev/disk1s1

# Write image on the raw device: if the mounted identifier is "disk1s1", 
# we will write to the raw device identifier "rdisk1"

# Using the device name of the partition work out the raw device name for the entire disk, by omitting the final “s1” and replacing “disk” # with “rdisk”. Exemple: /dev/disk1s1 -> /dev/rdisk1
sudo dd bs=1m if=ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img of=/dev/rdisk1

# After the dd command finishes, eject the card

# Eject the card
sudo diskutil eject /dev/rdisk1
```

## Installing Ubuntu Mate
> Important: during the installation phase, you need to connect your Raspberry to a USB mouse, a USD keyboard and a screnn via HDMI. 

1. Insert the SD card with Ubuntu Mate image into the SD card reader of your Raspberry
2. Switch it on
3. Follow instructions of the installation steps wizard

## Enabling SSH
To enable SSH, open a terminal `right-click ▸ Open in Terminal` and run the `raspi-config` utility:

`sudo raspi-config`

Then navigate with keyboard arrows to `Ìnterfacing Options ▸ SSH ▸ Enable`

## Identifying the IP address
To identify Raspberry PI IP address, simply:

`ifconfig` or `hostname -I`

You can then, use SSH to interact remotely with your Raspberry Pi from your machine. For instance, `ssh 192.168.1.102 -l user_name`

Tip: if you want to switch off remotely your Raspberry over SSH, you can run:
`sudo poweroff`

## Installing Mosquitto

```console
# Install repository
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa

# Remove the lock files in case of following error:
# "E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable)
# E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?"
sudo rm /var/lib/apt/lists/lock && sudo rm /var/lib/dpkg/lock

# Update repository
sudo apt-get update

# Install mosquitto
sudo apt-get install mosquitto mosquitto-clients
```

## Setting up a LoRa gateway
This step requires to get a LoRa expansion board, for instance this one: https://store.uputronics.com/index.php?route=product/product&path=61&product_id=68

![](https://i.imgur.com/6JlluCf.png?1)

### Setting up the LoRa expansion board
To use this expansion board you need to run the `raspi-config` utility:

`sudo raspi-config`

Then navigate with keyboard arrows to `Ìnterfacing Options ▸ SPI ▸ Enable`

`SPI` stands for Serial Peripheral Interface Bus: https://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus

### Installing LoRa gateway code
To use the Raspberry as a LoRa gateway you need to copy the folder named `raspi-lora-gateway`:
[`src/lora-sensing-final-project`](https://github.com/franckalbinet/iot-uaa-isoc/tree/master/labs/src/lora-sensing-final-project)

Using `scp`, copy the folder `raspi-lora-gateway` to the Raspberry.

Last, ensure that the following libraries are installed:

`sudo apt-get install git wiringpi libcurl4-openssl-dev libncurses5-dev`

## Setting up a Flask API
Last, to install an API providing access to the LoRa packets received by the LoRa gateway over HTTP, you need to copy the following folder `flask-api` to the Raspberry Pi. 

Important: this folder should be in same folder (at the same level) than `raspi-lora-gateway` one. 

Exemple:
```
/iot 
   - /raspi-lora-gateway
   - /flask-api
```

Last, install `Flask` Python micro framework for web development http://flask.pocoo.org/:
```
pip install flask
sudo apt-get install python-pandas
```
and set the FLASK_APP environment variable:
`export FLASK_APP=api.py`

## Running the LoRa gateway and API
The tutorial: [lora-sensing-final-project.md](lora-sensing-final-project.md) describes how to use the LoRa gateway.
