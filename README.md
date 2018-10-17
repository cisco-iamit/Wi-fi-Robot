# wi-fi-robot-
raspberry pi based wi-fi robot using html rest calls and python

How to install this package? 
First install raspbian from https://www.raspberrypi.org/downloads/
Using rufus http://rufus.ie/ install the rasbian image on to the sd card.
After starting the pi run a ```sudo apt-get update``` and ```sudo apt-get upgrade``` .
Then install pip using ```sudo apt-get install python-pip```.
Now download the package from git using git clone command e.g. ```git clone https://github.com/cisco-iamit/Wi-fi-Robot.git```.
Now extract the package from a **tar.gz** to a directory in the pi.
This can be done through the GUI or CLI, the GUI will allow you to use application such as achive extractor, thought the CLI you will need to use the command **unzip <filename>** e.g. ```unzip WebIOPi-0.7.1.zip``` to un pack the package.
Now you will need to navigate into the package using **cd** command e.g. ```cd WebIOPi-0.7.1.zip```
once in the package run ```sudo ./setup.sh``` this command will install and setup the package within raspbian
to start up the package run
```sudo /etc/init.d/webiopi start```
to stop run
```sudo /etc/init.d/webiopi stop```
on the same network as the pi goto the ip address and port 8000 e.g. http://raspberrypi:8000/ 
Default user is "webiopi" and password is "raspberry"
