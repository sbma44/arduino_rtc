import datetime
import serial

if __name__ == '__main__':
	ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
	dt = datetime.datetime.now()
	ser.write("".join([dt.strftime("T%S%M%H"), str(dt.weekday()), dt.strftime("%d%m%y")]))
	ser.close()