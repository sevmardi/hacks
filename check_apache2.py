import psutil 
import subprocess
from smtplib import SMTP



def check_apache2():
	for i in psutil.pids():
		p = psutil.Process(i)
		if p.name() == 'apache2':
			# print('found it!')
			# subprocess.check_call("sudo service apache2 restart".split())
			subprocess.Popen(['/etc/init.d/apache2', 'restart'])

			print("restart was executed..")


def send_email():
	pass
	



if __name__ == '__main__':
	check_apache2()