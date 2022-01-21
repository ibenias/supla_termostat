import subprocess
import sys
import requests
import json
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.LOW)

print("#########################")
print(" Start supla - termostat ")
print("#########################")

# check ip address
#ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
#print('IP address: %s' % ip_address.decode('utf-8'))

# check ping conections to google.com
def check_internet():
	url = 'http://www.google.com/'
	timeout = 5
	try:
		_ = requests.get(url, timeout = timeout)
		return True
	except requests>ConnectionError:
		print("Internet connection is false")
	return False

while True:
	if check_internet() == True:
		print("Internet connection is true")

		# read temperature from device 1 (Julka)
		response_1 = requests.get('https://svr11.supla.org/.................')
		if response_1.status_code == 200:
			temp = json.loads(response_1.text)["temperature"]
			print temp
		elif response_1.status_code == 404:
			print("Devise not found")

		# read temperature and humidity from device 2 (taras)
		response_2 = requests.get('https://svr11.supla.org/.................')
		if response_2.status_code == 200:
			humid_2 = json.loads(response_2.text)["humidity"]
			temp_2 = json.loads(response_2.text)["temperature"]
			print temp_2
			print humid_2
		elif response_2.status_code == 404:
			print("Device not found")

	else:
		print("Internet connection is false")
		print("termostat is off")
		GPIO.output(25, GPIO.LOW)

	time.sleep(30)
