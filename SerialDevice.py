import serial


class SerialDevice:
    def __init__(self, port, baud, serial_connection: serial.Serial):
        self._port = port
        self._baud = baud
        self._serial_connection = serial_connection

    @property
    def port(self):
        return self._port

    @property
    def baud(self):
        return self._baud

    @property
    def serial_connection(self):
        return self._serial_connection
