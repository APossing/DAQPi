import serial
import platform
import os
import time
import SerialDevice
import TemperatureSensor


class SerialInterface:
    def __init__(self):
        self.__system = platform.system()

    def __get_tty_files(self, path, starts_with):
        tty_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.startswith(starts_with):
                    tty_files.append(os.path.join(root, file))
        return tty_files

    def __get_linux_active_serial_ports(self):
        tty_files = self.__get_tty_files("/dev/", "tty")
        tty_files_with_baud = [(file, 9600) for file in tty_files]
        active_ports = self.__find_active_ports(tty_files_with_baud)
        return active_ports

    def __find_active_ports(self, portInfoList):
        activePorts = []
        for port, baud in portInfoList:
            try:
                ser = serial.Serial(
                    port=port,
                    baudrate=baud,
                )
                activePorts.append(SerialDevice.SerialDevice(port, baud, ser))
            except Exception as ex:
                #this should mean port is not active
                pass
        time.sleep(5)  # To ensure that devices have time to reset after serial connection opening
        return activePorts

    def __get_windows_active_serial_ports(self):
        port_names = []
        for i in range(10): # TODO should play with size of range...
            port_names.append(('COM'+str(i), 9600))
        activePorts = self.__find_active_ports(port_names)
        return activePorts

    def __assign_sensor_to_obj(self, serial_device, id, sensor_type, options):
        if sensor_type == "temperature":
            return TemperatureSensor.TemperatureSensor(serial_device, id, options[0])

    def get_active_sensors(self):
        active_ports = []
        if self.__system == 'Linux':
            active_ports = self.__get_linux_active_serial_ports()
        elif self.__system == 'Windows':
            active_ports = self.__get_windows_active_serial_ports()
        else:
            raise Exception("Why is the OS not Linux or Windows??")

        sensors = []
        for active_port in active_ports:
            active_port.serial_connection.write('DeviceCheck'.encode())
            time.sleep(0.1)
            x = active_port.serial_connection.read_all().decode()
            if x.startswith("1234"):
                x = x.split()
                sensors.append(self.__assign_sensor_to_obj(active_port, x[1], x[2], x[3:]))

        return sensors



