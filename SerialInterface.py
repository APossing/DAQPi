import serial
import platform
import os
import time
import SerialDevice
import TemperatureSensor


def __find_active_ports(port_info_list):
    active_ports = []
    for port, baud in port_info_list:
        try:
            ser = serial.Serial(
                port=port,
                baudrate=baud,
            )
            active_ports.append(SerialDevice.SerialDevice(port, baud, ser))
        except Exception as ex:
            # this should mean port is not active
            pass
    time.sleep(5)  # To ensure that devices have time to reset after serial connection opening
    return active_ports


def __get_tty_files(path, starts_with):
    tty_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(starts_with):
                tty_files.append(os.path.join(root, file))
    return tty_files


def __get_linux_active_serial_ports():
    tty_files = __get_tty_files("/dev/", "tty")
    tty_files_with_baud = [(file, 9600) for file in tty_files]
    active_ports = __find_active_ports(tty_files_with_baud)
    return active_ports


def __get_windows_active_serial_ports():
    port_names = []
    for i in range(10):  # TODO should play with size of range...
        port_names.append(('COM'+str(i), 9600))
    active_ports = __find_active_ports(port_names)
    return active_ports


def __assign_sensor_to_obj(serial_device, id, sensor_type, options):
    if sensor_type == "temperature":
        return TemperatureSensor.TemperatureSensor(serial_device, id, options[0])


def __get_active_ports():
    active_ports = []
    if platform.system() == 'Linux':
        active_ports = __get_linux_active_serial_ports()
    elif platform.system() == 'Windows':
        active_ports = __get_windows_active_serial_ports()
    else:
        raise Exception("Why is the OS not Linux or Windows??")
    return active_ports


def get_active_sensors():
    active_ports = __get_active_ports()
    time.sleep(1)

    sensors = []
    for active_port in active_ports:
        active_port.serial_connection.write('DeviceCheck'.encode())

    time.sleep(5)

    for active_port in active_ports:
        z = active_port.serial_connection.in_waiting
        x = active_port.serial_connection.read(z).decode()
        if x.startswith("1234"):
            x = x.split()
            sensors.append(__assign_sensor_to_obj(active_port, x[1], x[2], x[3:]))

    return sensors


def attempt_reconnect(id):
    active_ports = __get_active_ports()
    time.sleep(1)

    for active_port in active_ports:
        active_port.serial_connection.write('DeviceCheck'.encode())

    time.sleep(5)

    for active_port in active_ports:
        x = active_port.serial_connection.read_all().decode()
        if x.startswith("1234"):
            x = x.split()
            if x[1] == id:
                return active_port
            else:
                pass  # TODO this means there is a device that is out there and not mapped... Maybe a problem?
