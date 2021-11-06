# python-public-API
## This repository is a public API for solving the problem of the final of the AIIJC competition.
The task is to create an AI for the classification of traffic signs, the 'model' file is a ready trained model and the prediction is done in 'PublicAPI.py'.

The API itself is written in Python using the Flask framework

The API should receive an image of a road turn sign as input (it can consist of several signs) and send the name of the signs from left to right.

![alt text](https://github.com/LevProg/python-public-API/blob/main/post-get.png?raw=true)

We will use our own computer as a server and ngrok as a proxy.
ngrok - https://ngrok.com/download

With 'PublicAPI.py' we start a local server

![alt text](https://github.com/LevProg/python-public-API/blob/main/localServer.png?raw=true)

Next, open ngrok.exe and run the proxy with the command: 'ngrok http your_port', in our case our port is 4567, in response we will receive the URL

![alt text](https://github.com/LevProg/python-public-API/blob/main/proxy.png?raw=true)

We will check the functionality of the API using the 'TestPublicAPI.py' file, we send a request with a photo to the URL received from ngrok.

![alt text](https://github.com/LevProg/python-public-API/blob/main/request.png?raw=true)

Also we can just go to the received URL and send the file manually

![alt text](https://github.com/LevProg/python-public-API/blob/main/site.png?raw=true)
