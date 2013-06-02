from os import path
from ConfigParser import SafeConfigParser

ROOT_PATH = path.abspath(path.dirname(path.realpath(__file__)))
CONFIG_FILE = path.join(ROOT_PATH, "settings.conf")

config = SafeConfigParser()
with open(CONFIG_FILE) as config_file:
    config.readfp(config_file)

RXA730_IP = config.get('rxa730', 'ip')
RXA730_PATH = config.get('rxa730', 'path')
RXA730_URL = "".join(["http://", "/".join([RXA730_IP, RXA730_PATH])])

PHONE_IP = config.get('netspy', 'phone_ip')

COMMAND_OFF = config.get('commands', 'OFF')
COMMAND_ON = config.get('commands', 'ON')

POWER_TEMPLATE = """<YAMAHA_AV cmd="PUT">
<Main_Zone>
<Power_Control>
<Power>%s</Power>
</Power_Control>
</Main_Zone>
</YAMAHA_AV>"""
