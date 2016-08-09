import serial
import time

class arduinoHandler():
	def __init__(self):
		self.port = '/dev/ttyACM0'
		self.baud = 9600
		self.ser = serial.Serial(self.port, self.baud)
	def up(self, reps):
		for i in range(reps):
			self.ser.write('U')
	def down(self, reps):
		for i in range(reps):
			self.ser.write('D')
	def left(self, reps):
		for i in range(reps):
			self.ser.write('L')
	def right(self,reps):
		for i in range(reps):
			self.ser.write('R')