#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from urllib.request import urlopen
import inquirer

# need `sudo` to show all networks
def start():
	# download most used passwords on github.com and build a dict
	print("Fetch top 100K most used passwords on Github...")
	url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-100000.txt"
	response = urlopen( url )
	txt = response.read()
	passwords = txt.splitlines()

	questions = [
		inquirer.Text('wifi',
			message="Kojoj mrezi se zelis pridruziti?",
		),
		inquirer.Text('names',
			message="Kako se kafic zove? Ukoliko ima vise imena/skracenica odvoji ih zarezom",
		),
	]
	answers = inquirer.prompt(questions)
	print(answers["wifi"])
	print(answers["names"].split(","))

	print("Zaporka nije pronadena! Pitaj konobara :(")

#	for password in passwords:
#		for cell in networks:
			# try:
			# 	scheme = Scheme.for_cell('wlan0', 'home', cell, 'test')
			# 	scheme.activate()
			# 	print("Connect to {} with `{}` passkey works!!".format(cell, 'test'))
			# 	sys.exit(0)
			# except exceptions.ConnectionError as e:
			# 	pass
			# finally:
			# 	nb_test += 1

			# sys.stdout.write('\r{} / {}'.format( nb_test, nb_loops ))
			# sys.stdout.flush()