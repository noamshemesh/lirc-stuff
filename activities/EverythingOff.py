from subprocess import call
from time import sleep  

def send_once(device_id, message, count=1):
  call(['irsend', 'SEND_ONCE', device_id, message, '-d', '/var/run/lirc/lircd', '-#', str(count)])

if __name__ == "__main__":
  send_once('Onkyo_RC-710M', 'KEY_POWEROFF')
  sleep(0.3)
  send_once('XBOX-ONE', 'KEY_POWEROFF', 2)
  sleep(0.3)
  send_once('Samsung_BN59-00685A', 'KEY_POWEROFF', 2)

