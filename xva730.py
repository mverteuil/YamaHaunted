import ConfigParser

import requests

import settings

def power_on():
    command = settings.POWER_TEMPLATE % settings.COMMAND_ON
    requests.post(settings.RXA730_URL, data=command)

def power_off():
    command = settings.POWER_TEMPLATE % settings.COMMAND_OFF
    requests.post(settings.RXA730_URL, data=command)
