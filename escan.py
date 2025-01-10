R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

import time
import subprocess

print ('--------------------')
print ('Escaneando Red Local')
print ('--------------------')


def escanear_red(interface=None):
	comando = ["sudo","arp-scan"]
	
	comando.append("192.168.1.1/24")
	try:

		resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
		print ("Resultados del escaneo:\n")
		print (resultado.stdout)
	except subprocess.CalledProcessError as e:
		print ("Ocurrio un error al escanear la red:\n", e.stderr)

if __name__ == "__main__":
	
	escanear_red(interface="eth0")

print ('--------------------')
print ('Su escaneo ha sido exitoso')
print ('--------------------')

print ('\033[32m-----> Created By 4LFASec')
print ('\033[32m-----> Github https://github.com/codetamar')
print ('\033[32m-----> Twitter X.com https://x.com/4lfasec')
print ('\033[32m')

# Script Gracias a 4LFASec https://github.com/codetamar
