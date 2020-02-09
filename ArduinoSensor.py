import SerialDevice
import SerialInterface
from abc import ABC, abstractmethod


class ArduinoSensor(ABC):
    @property
    def serial_device(self):
        return self._serial_device

    @property
    def id(self):
        return self._id

    def __init__(self, serial_device: SerialDevice, sensor_id):
        self._serial_device = serial_device
        self._id = sensor_id

    def attempt_reconnect(self):
        sel = SerialInterface.attempt_reconnect(self.id)
        if sel is None:
            for i in range(1):
                sel = SerialInterface.attempt_reconnect(self.id)
                if sel is not None:
                    break
        self._serial_device = sel

    @abstractmethod
    def read_data(self):
        pass
