import SerialDevice
import serial
from abc import ABC, abstractmethod


class ArduinoSensor(ABC):
    @property
    def serial_device(self):
        return self._serial_device

    @property
    def id(self):
        return self._id

    def __init__(self, serial_device: SerialDevice, sensorId):
        self._serial_device = serial_device
        self._id = sensorId

    def attempt_reconnect(self):
        ser = serial.Serial()

    @abstractmethod
    def read_data(self):
        pass

