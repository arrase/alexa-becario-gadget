## Run on boot

Paste this line in */etc/crontab*

    @reboot root screen -dmS becario bash -c "cd /home/pi/Alexa-Gadgets-Raspberry-Pi-Samples/ && python3 launch.py --example src/examples/shell_runner/shell_runner.py"
