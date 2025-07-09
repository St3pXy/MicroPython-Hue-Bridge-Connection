# MicroPython-Hue-Bridge-Connection
This repo contains code to control all your Philips Hue Devices connected to the the Hue Bridge, via a WI-FI connected microcontroller (ex: Raspbery Pi Pico W, ESP32, ecc...)
The objective is to provide anyone with a easy-to-read and easy-to-use MicroPYthon code to interract with they Hue Hub.


## Features
- Connection to Wi-Fi
- Always ready to act
- Hue Bridgege Comunication



## Before Usage
Before beeing able to use the code, you need to get:
- Id of your hub (Hue Mobile app > settings > My Hue System > i (info) > Ip Adress)
- Username Token (Connect to the Hue Api Debug tool: you can follow this [TUTORIAL](https://developers.meethue.com/develop/get-started-2/).)

## Usage
### Setting Up Variables
In way to use the code, you have to change the variables on the following lines:

- Line 11:
> button = Pin(14, Pin.IN, Pin.PULL_UP)
Chagne the number of the Button Pin with the pin you are using

- Line 19 & 19:
> ssid = ""  # Network name (Your Wifi's name)
> password = ""  # Network password (Your Wifi's password)
Insert your WiFi Name and Password to allow WiFi acces

- Line 25 & 26:
> hub_id = ""
> user_token = ""
into the "hub_id" variable insert your Hue Hub Id
Meanwhile, into the "user_token" variable insert the username token you got from the "Hue API DEBUG TOOL"



### Debug Prints
Feel free to de-comment, add or change the debug prints present in the code
They are mostly used to view if the connection is stable, if the PUT request was succesful and eventually to handle exceptions.



## Future Features (Work in progress...)
- Automatic Bridge Discovery
- Automatic lights recongization
- Possibility to controll groups (not only lights)
