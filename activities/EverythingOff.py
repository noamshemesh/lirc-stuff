from subprocess import call

def send_once(self, device_id, message):
  call(['irsend', 'SEND_ONCE', device_id, message, '-d', '/var/run/lirc/lircd'])

if __name__ == "__main__":
  send_once('Onkyo_RC-710M', 'POWEROFF')
#  send_once('

