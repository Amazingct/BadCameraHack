import cv2 as cv
import paho.mqtt.client as mqtt
import base64
import socket


hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
broker = ""
topic = "{}_camera".format(hostname)



while True:
    cap = cv.VideoCapture(-1)
    client = mqtt.Client()
    client.connect(broker,30100)
    try:
        print("Connected to broker and publishing frames")
        while cap.isOpened():
            _, frame = cap.read()
            frame =  cv.resize(frame, (150, 150))
            # change to black and white
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # Encoding the Frame
            _, buffer = cv.imencode('.jpg', frame)
            # Converting into encoded bytes
            jpg_as_text = base64.b64encode(buffer)
            # Publishig the Frame on the Topic 
            client.publish(topic, jpg_as_text)
    except:
        cap.release()
        client.disconnect()
