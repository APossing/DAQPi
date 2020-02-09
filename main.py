# coding: utf-8
import paho.mqtt.client as mqtt
import time
import os
import SerialInterface



class MainRunner:

    def __init__(self):
        self.arduinos = []
        self._sensors = SerialInterface.get_active_sensors()

    def readData(self):
        for sensor in self._sensors:
            sensor.read_data()


def get_data_packet():
    # data packet format:
    # lp1/lp2/lp3/lp4 g rpm   br1/br2 str thr time_epoch
    # ###/###/###/###_#_#####_###/###_###_###_###...###

    # TODO
    # poll data sensors and update the values for each variable...
    # lp1 = 0.00
    # lp2 = 0.00
    # lp3 = 0.00
    # lp4 = 0.00
    # g = 0
    # rpm = 0
    # br1 = 0.00
    # br2 = 0.00
    # steering = 0.00
    # throttle = 0.00
    #t = time.time()

    # the fastest string concatenation approach in python (when joining fairly small [n<~100,000] numbers of variables) is to simply use the + operator, as per Jsaon Baker's answer at:
    # https://stackoverflow.com/questions/1316887/what-is-the-most-efficient-string-concatenation-method-in-python#1316959

    #return str(lp1) + '_' + str(lp2) + '_' + str(lp3) + '_' + str(lp4) + '_' + str(g) + '_' + str(rpm) + '_' + str(br1) + '_' + str(br2) + '_' + str(steering) + '_' + str(throttle) + '_' + str(t)
    return str(time.time())


if __name__ == '__main__':
    mainRunner = MainRunner()
    while 1:
        mainRunner.readData()

    # create mqtt instance
    #client = mqtt.Client("wsu_fsae_client_1")

    # connect to an mqtt broker
    #print("connecting to broker")
    #broker_address="mqtt.eclipse.org"
    #client.connect(broker_address)
    #print("connected")

    # while car is on...
    #while True:
        # wait a 'lil bit, we don't want to overload the free broker
        #time.sleep(1.000)

        # publish the car's telemetry data packet to mqtt broker
        #print("publishing")
        #client.publish("wsu/fsae",get_data_packet())
