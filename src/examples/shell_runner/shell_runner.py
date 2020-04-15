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

if __name__ == '__main__':
    try:
        ShellRunnerGadget().main()
    finally:
        pass
