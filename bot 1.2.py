import sys
import string
import csv
import requests
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# can't use ffox 46+

test_server = 'http://www.google.com'
mega_list = []

def get_info():
	#try:
		ffox = FirefoxBinary('/home/kashyap/myprograms/firefox45/firefox')
		browser = webdriver.Firefox(firefox_binary=ffox)

		browser.get('http://karresults.nic.in/indexcet2016.asp')
		
		# generating combinations
		A1 = list(string.ascii_uppercase)
		A2 = list(string.ascii_uppercase)
		district_list = []
		for i in A1:
			for j in A2:
				s = i + j
				district_list.append(s)

		num_list = list(range(1, 1000))
		num_list = [('00' + str(i))[-3:] for i in num_list]

		for x in district_list:
			for y in num_list:
				reg_no = x + y
				
				reg_no_elem = browser.find_element_by_class_name('form-control')
				reg_no_elem.send_keys(reg_no)

				submit_btn = browser.find_element_by_name('B1')
				submit_btn.click()

				info_list = []

				try:
					name_elem = browser.find_element_by_class_name('table')
					info_list = name_elem.text.split('\n')
					rank_elem = browser.find_elements_by_class_name('textright')	# is a list
					eng = rank_elem[0].text
					med = (rank_elem[1].text)[1:]

					info_list.append(eng)
					info_list.append(med)
					info_list[0] = info_list[0][6:]
					info_list[1] = info_list[1][11:]
					# print(info_list)
					mega_list.append(info_list)
					browser.back()
				except:
					is_connected()
					browser.back()
					break

		print(mega_list)
		print('done !')
		browser.close()
	#except:
	#	print('poop')

def is_connected():
	attempts = 0
	while (attempts < 3):
		if rq() == True:
			print('yay')
			return True
		time.sleep(5)	# sleep for a min
		print('attempt no: ' + str(attempts))
		attempts = attempts + 1
	print('Diconnected at: ')
	print(datetime.now().strftime('%H:%M %d-%m-%Y'))
	print('boo')

def rq():
	try:
		requests.get('http://www.google.com')
	except:
		return False
	return True


if __name__ == '__main__':
	get_info()
	outfile = open('./CET_RESULTS.csv', 'w')
	writer = csv.writer(outfile)
	writer.writerow(['NAME', 'REG_NO', 'ENG_RANK', 'MED_RANK'])
	writer.writerows(mega_list)