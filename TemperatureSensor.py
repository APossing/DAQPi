import ArduinoSensor


class TemperatureSensor(ArduinoSensor.ArduinoSensor):
    @property
    def location(self):
        return self._location

    def __init__(self, serial_device, id, location):
        super(TemperatureSensor, self).__init__(serial_device, id)
        self._location = location
        self.serial_device.serial_connection.write("StartData".encode())

    def read_data(self):
        data = ""
        try:
            if self._serial_device.serial_connection.in_waiting:
                data = self._serial_device.serial_connection.read_all()
                print(data)
        except Exception as ex:
            self.attempt_reconnect()
            if self._serial_device.serial_connection is not None:
                self._serial_device.serial_connection.write("StartData".encode())
