import ArduinoSensor


class TemperatureSensor(ArduinoSensor.ArduinoSensor):
    @property
    def location(self):
        return self._location

    def __init__(self, serial_device, id, location):
        super(TemperatureSensor, self).__init__(serial_device, id)
        self._location = location

    def read_data(self):
        self._serial_device.serial_connection.read()