# python-public-API
## This repository is a public API for solving the problem of the final of the AIIJC competition.
The task is to create an AI for the classification of traffic signs, the 'model' file is a ready trained model and the prediction is done in 'PublicAPI.py'.

The API itself is written in Python using the Flask framework

The API should receive an image of a road turn sign as input (it can consist of several signs) and send the name of the signs from left to right.

![alt text](https://github.com/LevProg/python-public-API/blob/main/post-get.png?raw=true)

We will use our own computer as a server and ngrok as a proxy.
ngrok - https://ngrok.com/download

With 'PublicAPI.py' we start a local server

```python
    if __name__ == "__main__":
      app.run(host='0.0.0.0', port=4444)
```


Next, open ngrok.exe and run the proxy with the command: 'ngrok http your_port', in our case, our port is 4444, in response we will receive a lot of information, including the URL


```cmd
    Forwarding          http://bbce-5-142-42-152.ngrok.io -> http://localhost:4444
```


We will check the functionality of the API using the 'TestPublicAPI.py' file, we send a request with a photo to the URL received from ngrok.

```python
    import requests
    import json

    files = {'file': open('TestImage.png','rb')}
    print(requests.post('http://e252-178-67-199-112.ngrok.io', files=files).text)
```

Also we can just go to the received URL and send the file manually

![alt text](https://github.com/LevProg/python-public-API/blob/main/site.png?raw=true)
