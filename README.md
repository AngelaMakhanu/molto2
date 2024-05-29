
Token2 Molto2 USB Config Tool, Python version
=======================

This is a command line tool to configure Molto2v2, a multiprofile TOTP token by [Token2](https://www.token2.com/).
The steps below are for Ubuntu operating system, but should be the same or similar with any other Linux distribution. 

Installation
------------
The script is written for Python3 
Install requirements: `pip install -r requirements.txt` (or `pip3 install -r requirements.txt`)
Or one by one : `pip install pyscard` and `pip install sm4`


PCSC Installation and configuration
--------

The script is using PCSC service to connect to the device, therefore you should be having some components installed before you can launch the script.
`sudo apt-get install libusb-dev libusb++`
`sudo apt-get install libccid`
`sudo apt-get install pcscd`
`sudo apt-get install libpcsclite1`
`sudo apt-get install libpcsclite-dev`
`sudo apt-get install pcsc-tools`

PCSC comes with a pre-defined list of supported hardware, primarily smart card readers. As Molto2v2 is a relatively new product, it is not listed in the default configuration, therefore we need to add it manually. Follow the instructions below:

 - Open the device list file, which is usually located at the path below (but the exact folder name may slightly vary):
      `sudo nano /usr/lib/pcsc/drivers/ifd-ccid.bundle/Contents/Info.plist`
     (if this file is not found, try searching using "sudo find / -name Info.plist ")
    
 - Add  `<string>0x349E</string>` at the end of the section `<key>ifdVendorID</key>`
 - Add `<string>0x0300</string>` at the end of the section `<key>ifdProductID</key>`
 - Add `<string>Token2 Molto2</string>` at the end of the section `<key>ifdFriendlyName</key>`
 - Save and restart the system for the changes to take effect.

Usage
-----
As a start, make sure your system is correctly configured. Plug Molto2 into a USB port and run the script without any parameters:
`python3 molto2.py`

This should produce results similar to the below:

    [i] TOKEN2 Molto2 USB Config Tool, Python version, v0.2
                                             (c) TOKEN2 Sarl
    [!] Note: No customer key was provided, default customer key will be used
    [+] device serial number: 826658719844499
    [+] device system time (UTC): 2022-11-16 09:07:19
    [+] Authentication successful
If you see the serial number of the device, this means the script has access to it.  You can continue with using the tool. The exact syntax and parameters can be obtained by running the script with --help argument.

`python3 molto2.py --help`

    usage: molto2.py [-h] [--key KEY] [--keyascii KEYASCII] [--profile PROFILE] [--title TITLE] [--seed SEED] [--seedbase32 SEEDBASE32] [--setkey SETKEY] [--setkeyascii SETKEYASCII] [--config]
                     [--display_timeout DISPLAY_TIMEOUT] [--algorithm ALGORITHM] [--timestep TIMESTEP] [--factoryreset]
    
    optional arguments:
      -h, --help            show this help message and exit
      --key KEY             Customer key in hex format. Default will be used if not supplied.
      --keyascii KEYASCII   Customer key in ascii format. Default will be used if not supplied.
      --profile PROFILE     Profile number, from 0 to 49 (Molto2) or from 0 to 99 (Molto2 v2)
      --title TITLE         Profile title, 12 chars max
      --seed SEED           Seed to write, in hex format
      --seedbase32 SEEDBASE32
                            Seed to write, in base32 format
      --setkey SETKEY       Set the new customer key, providing the key in hex. Please note that setting new key requires confirmation on the device (physical button press)
      --setkeyascii SETKEYASCII
                            Set the new customer key, providing key in ascii. Please note that setting new key requires confirmation on the device (physical button press)
      --config              If config parameter is set, the config parameters become required.
      --display_timeout DISPLAY_TIMEOUT
                            mandatory if --config is set as 1. Possible values 0=15s, 1=30s, 2=60s, 3=120s
      --algorithm ALGORITHM
                            mandatory if --config is set as 1. Possible values 1=SHA1 HMAC or 2=SHA256 HMAC hashing algorithm
      --timestep TIMESTEP   mandatory if --config is set as 1. Possible values 1=30 seconds or 2= 60 seconds
      --factoryreset        Resets the device to factory setting and clear all data. Please note this requires confirmation on the device (physical button press)
      --synctime            Will update time on the given profile.
      --synctimeall         Will update time on all profiles.
      --lock                Lock device screen (only for v2.1 and higher)
      --unlock              Unlock device screen (only for v2.1 and higher)    

The following example sets a new hex seed (`--seed DEADBEEFDEADBEEF`)  and a configuration (`--config`) of  TOTP step of 30 seconds (`--timestep 1`), the HMAC algorithm of SHA1 (`--algorithm 1`), title of 'Google' (`--title Google`) and a display sleep timeout of 30 seconds (`--display_timeout 2`)  for profile №2 (`--profile 2`):

    python3 molto2.py --confg --profile 2 --seed DEADBEEFDEADBEEF  --timestep 1 --algorithm 1  --display_timeout 2

GUI Interface
------------------
A simplified GUI built with QT is also available. Launch the GUI using the following command (from the same directory):

`python3 gui.py`

The GUI replicates the interface of the Windows app. Please ensure that the PyQT5 module is installed by executing:

`pip install PyQt5`



Supported Products
------------------

* [Token2 Molto2v2]



License
-------
Licensed to : gauthier.hubert@flowdesk.co
This application was  developed by Token2 RD Team (https://www.token2.com/) 


