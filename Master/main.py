import base64
import cv2 as cv
import numpy as np
import paho.mqtt.client as mqtt


class VisionFromMqtt:
    def __init__(self, mqttBroker,mqttPort, mqttReceive):
        self.mqttBroker = mqttBroker
        self.mqttReceive = mqttReceive
        self.frame = np.zeros((240, 320, 3), np.uint8)
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.mqttBroker, mqttPort)
        self.client.loop_start()
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(self.mqttReceive)
    def on_message(self, client, userdata, msg):
        # Decoding the message
        img = base64.b64decode(msg.payload)
        # converting into numpy array from buffer
        npimg = np.frombuffer(img, dtype=np.uint8)
        # Decode to Original Frame
        self.frame = cv.imdecode(npimg, 1)
    def publishObjects(self, objects):
        to_send = {"persons":[], "actions":[], "emotions":[]}
        for obj in objects:
            to_send["persons"].append(list(obj.keys())[0])
            to_send["actions"].append(list(obj.values())[0].split("/")[0])
            to_send["emotions"].append(list(obj.values())[0].split("/")[1])
        self.client.publish(self.mqttReceive[:-6]+"/log", json.dumps(to_send))
    def getFrame(self):
        return self.frame
    def stop(self):
        self.client.loop_stop()


MQTT_BROKER = "45.55.44.162"
MQTT_RECEIVE = "parallelscore_camera"
vision = VisionFromMqtt(MQTT_BROKER,30100, MQTT_RECEIVE)

while True:
    frame = vision.getFrame()
    cv.imshow("MQTT_RECEIVE", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
