> [Internet of Things (IoT) | Training Course](setup.md) ▸ **Setup**

# Course setup

[1. Installing Atom editor](#installing-atom-editor)

[2. Installing Atom Pymakr plugin](#installing-atom-pymakr-plugin)

[3. Upgrading Pycom boards firmwares](#upgrading-pysense-board-firmware)

[4. Installing Anaconda](#installing-anaconda)

[5. Installing GitHub Desktop [optional]](#installing-github-desktop)

[6. Installing Filezilla](#installing-filezilla)

[7. Installing PuTTY](#installing-putty)

[7. Downloading course material](#downloading-course-material)

[8. Troubleshooting](#troubleshooting)

## Installing Atom editor
Atom is an Integrated Development Environment (**IDE**), providing convenient features to edit Python code (among many others): syntax highlighting, completion, auto-indentation, integration with Git, bash, ...

We will use Atom to write Python code during the labs sessions. 

To install it, download the installation file for your Operating System here: [https://atom.io/](https://atom.io/)

## Installing Atom Pymakr plugin
The Python code written will not be executed in your local machine. Instead, you need to transfer it to your IoT device (in our case Pycom Lopy). To do so, [Pycom](https://www.pycom.io/) developed a plugin named **Pymakr** that will facilitate the execution and syncing of Python to the device.

To install the plugin in Atom:

1. Open Atom
2. In top menu: Atom ► Preferences...
3. And write `pymkr` in the input box under the `Install tab` (followed by `Enter`):

![img/install-pymkr.png](http://i.imgur.com/Of2NTPR.png)

## Upgrading Pysense board firmware
Pycom devices are under constant development and improvement. You must make sure you have the latest firmware version installed. 

Firmware upgrading procedure is documented here: https://docs.pycom.io/chapter/pytrackpysense/installation/firmware.html

## Installing Anaconda
Python comes in different flavours: different versions and different environment of libraries. Moreover, a Python's version is most probably already installed in your machine. 

So in order to not screw up your installation, it is advised to install Anaconda https://anaconda.org/ which provides a very convenient way to run various Python version with various set of Python modules and libraries in an isolated and safe way.

For our labs, we will use Anaconda version 3.6 https://www.continuum.io/downloads

### [OPTIONAL]: Creating a new environment using Python 2.7

Once installed (Anaconda with Python version 3.6 by default), we want now to install Python 2.7 as well. To do so:

1. Open `Anaconda Navigator`
2. Click on `Environments` tab
3. Ckick on the arrow on the right of `root` item
4. `Open Terminal`

![img/anaconda-env-prog.png](http://i.imgur.com/Cfp8QSo.png)

Documentation on how setting up various Python versions and environments in Anaconda https://conda.io/docs/py2or3.html

In the terminal:

* to know your current Python version: `python --version`


* to get a list of existing environments: `conda info --envs`

Now, to create a new environment with Python version 2.7:

`conda create -n py4data-2.7 python=2.7 anaconda`

`py4data-2.7` being the name of your environment.

## Installing FileZilla
FileZilla will be used occasionnaly to synchronize or retrieve file from IoT device via ftp and Wifi of the device itself.

Download the FileZilla ftp client here: https://filezilla-project.org/

## Installing GitHub Desktop
Git is a version control system (VCS) for tracking changes in computer files and coordinating work on those files among multiple people. 

GitHub is a web-based Git or version control repository facilitating collaborative software development.

We will cover only the very basics of Git during these labs and will use GitHub Desktop standalone.
If you want to have a deeper understanding, you can look at this free online course at Udacity: https://www.udacity.com/course/how-to-use-git-and-github--ud775

So, download it here: https://desktop.github.com/ and install it.

## Installing PuTTY
PuTTY will be used to initiate SSH communication with a Raspberry PI. If you have a machine with OSX or Linux installed you can use directly the `ssh` program available in a terminal. If you have a Windows machine, you can use PuTTY instead.

You can download PuTTY using this link: http://www.putty.org and install it (download the installer and double click on it).

To copy files from your machine to the Raspberry PI or the opposite over the SSH protocol, you can use the `scp` command under OSX or Linux. Under Windows, you can use the `pscp.exe` program that you can download here: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

## Downloading course material

Course material can be download as a `zipped` archive [here](../downloads).

## Troubleshooting
### Windows 7 drivers
On most platforms, once the Atom Pymakr package installed, you will be in a position to communicate with Pycom devices via the USB port without any issue.

In the case of Windows 7, you will need to install an additional driver. The procedure is documented in Pycom documentation at the following url: https://docs.pycom.io/chapter/pytrackpysense/installation/drivers.html

Alternatively, you can find as well the required driver here [../softs/windows/pycom.inf](../softs/windows/pycom.inf)

