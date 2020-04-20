import logging
import sys
import os

from agt import AlexaGadget

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

logging.getLogger('agt.alexa_gadget').setLevel(logging.DEBUG)

#########################
#  SCRIPT tv.sh example #
#########################

#     #!/bin/bash
#
#     if [[ "$1" == "on" ]]
#     then
#       echo 'on 0.0.0.0' | cec-client -s -d 1
#       exit 0
#     fi
#     
#     if [[ "$1" == "off" ]]
#     then
#       echo 'standby 0.0.0.0' | cec-client -s -d 1
#       exit 0
#     fi
#     
#     if [[ "$1" == "as" ]]
#     then
#       echo 'as' | cec-client -s -d 1
#       exit 0
#     fi

class ShellRunnerGadget(AlexaGadget):
    def __init__(self):
        super().__init__()

    def on_custom_shellrunnergadget_tvon(self, directive):
        os.system('/home/pi/bin/tv.sh on')

    def on_custom_shellrunnergadget_tvoff(self, directive):
        os.system('/home/pi/bin/tv.sh off')

    def on_custom_shellrunnergadget_rpias(self, directive):
        os.system('/home/pi/bin/tv.sh rpias')

    def on_custom_shellrunnergadget_tvas(self, directive):
        os.system('/home/pi/bin/tv.sh tvas')

    def on_custom_shellrunnergadget_tvvolup(self, directive):
        os.system('/home/pi/bin/tv.sh volup')

    def on_custom_shellrunnergadget_tvvoldnw(self, directive):
        os.system('/home/pi/bin/tv.sh voldnw')

    def on_custom_shellrunnergadget_tvmute(self, directive):
        os.system('/home/pi/bin/tv.sh mute')

    def on_custom_shellrunnergadget_reboot(self, directive):
        os.system('reboot')

    def on_custom_shellrunnergadget_upgrade(self, directive):
        os.system('apt-get update && apt-get upgrade -y')

    def on_custom_shellrunnergadget_torrent(self, directive):
        os.system('/home/pi/bin/becario.sh torrent')

    def on_custom_shellrunnergadget_kodi(self, directive):
        os.system('/home/pi/bin/becario.sh kodi')

    def on_custom_shellrunnergadget_pcreboot(self, directive):
        os.system('/home/pi/bin/becario.sh pcreboot')

    def on_custom_shellrunnergadget_pchalt(self, directive):
        os.system('/home/pi/bin/becario.sh pchalt')

if __name__ == '__main__':
    try:
        ShellRunnerGadget().main()
    finally:
        pass
