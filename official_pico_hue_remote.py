# Manual Micropython Philips Hue Connection & Controll

import urequests
from machine import Pin
import utime
import network

import _thread

#  Change the first parameter with the pin your button's connected to.
button = Pin(14, Pin.IN, Pin.PULL_UP)

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#  Network Credentials
ssid = ""  # Network name (Your Wifi's name)
password = ""  # Network password (Your Wifi's password)

# Connection to Network
wlan.connect(ssid, password)

#  Your hub credentials
hub_id = ""
user_token = ""

link = "https://" + hub_id + "/api/" + user_token + \
    "/lights/"  # Auto link creation for your Hue Hub
# Insert the Ids of your lights (ex: lights_ids = [1, 2, 3]) -> Follow tutorial
lights_ids = []


#  Setting up lights status -> Default manual set-up on folse (Lights off)
lights_on = False

#  json body to send to Hub via http PUT method
body = {
    "on": False
}

# Test Connection with debug prints
r = urequests.get(link+"lights")
print(r)
print(r.content)
print(r.json())
print(r.headers)

print("READY TO USE\n")

while True:

    if button.value() == 0:
        print("\nbutton pressed\n")

        # We use the busson as a switch -> we change the state of the lights_on variable True/False and we make requests to the Hue Hub to change the state of the lights

        # Changhing state of lights_on variable
        if not lights_on:
            lights_on = True

        else:
            lights_on = False

        #  Gettign ready json data for Hue Hub
        body = {
            "on": lights_on
        }

        #  Act to every light indipendently
        for id in lights_ids:

            #  Set-up individual light link
            light_link = link + str(id) + "/state"
            # print("\nlight_link: ", light_link)

            # Try to act on the light
            try:
                r = urequests.put(light_link, json=body)
            except Exception as e:
                # Debug print if catch errorung while acting on the light (http PUT method)
                print("\nexception while acting on lights\n")
                try:
                    print(r)
                    print(r.content)
                    print(r.json())
                    print(r.headers)
                finally:
                    print("\n\nIt occured the following error: ", e)

            finally:
                #  Finally get some sleep time between a call and another to avoid crashes

                # utime.sleep(0.25) # Even Safer Time but too slow
                utime.sleep(0.05)  # Safe time

            #  Debug prints
            """
            print("\n\nstart little debug print\n\n")
            print(r)
            print(r.content)
            print(r.json())
            print(r.headers)
            print("\n\nend little debug print\n\n")
            """

        #  Sleep time to avoid crashes
        utime.sleep(0.5)  # Not necessary required

        print("Lights are now in mode: ", lights_on)
