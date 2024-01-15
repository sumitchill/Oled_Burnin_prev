
from flask import Flask
import subprocess
import time

app = Flask(__name__)


@app.route('/turnon')
def turn_on():

    # uses voice assistant to greet!
    # subprocess.Popen(["nircmd.exe", "speak", "text",'"Hellosir"', "2", "80"], shell=True)
    
     # move cursor command used above to move the cursor and bypass the autosleep after monitor turns on!)
    subprocess.run(["nircmd.exe","beep","500","1000"],shell=True)
    subprocess.run(["nircmd.exe", "monitor", "on"], shell=True)

    # Uses to move the cursor from a specific Co-ordinates!
    subprocess.run(["nircmd", "movecursor", "96", "75"], shell=True)
  


    # Turn on the monitor (But the monitor turnsOff again after some seconds
    # the request do work but the screen doesn't stay awake so we'll use
   
    # subprocess.Popen(["nircmd.exe","screensaver"],shell=True)

    # subprocess.run(["nircmd.exe", "exitwin", "logoff"], shell=True)

    # subprocess.run(["nircmd.exe", "exitwin", "poweroff"], shell=True)

    # time.sleep(700)
    return "Screen turned on"


@app.route('/turnoff')
def turn_off():
    # Uses screen off function in nircmd
    subprocess.run(["nircmd.exe", "monitor", "async_off"], shell=True)
    # subprocess.run(["nircmd.exe", "standby"], shell=True)
    return "Screen turned off"


@app.route("/screensaver")
def screensaver():
    # uses the hibernate command to hibernate the laptop uses 1 hrs time interval!
    subprocess.Popen(["nircmd.exe", "hibernate"], shell=True)
    return "screensaver"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
