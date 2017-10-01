# DalekBot
This is the code for my Dalek Bot</p>
</p>
DalekV2Drive.py - Contains the functions required to make the motors work.</p>
DalekV2MainV2.py - Contains the main control code.  The plan is to have this be the locus of control with functions for each event in PiWars.  Additional modules will be created as deemed necessary.</p>
</p>
</p>
usage: DalekV2MainV2.py [-h] [-r RIGHTSPEED] [-l LEFTSPEED] [-s SPEED]
                        [-b BRIGHTNESS] [-i INNERTURNSPEED]
                        [-o OUTERTURNSPEED] [-c SHOWCAM] [-v SOUNDVOLUME]
</p>
PiWars Dalek Control Program</p>
</p>
optional arguments:
  -h, --help         show this help message and exit
  -r RIGHTSPEED      Initial speed of Right motors (0 - 100)
  -l LEFTSPEED       Initial speed of Left Motors (0 - 100)
  -s SPEED           Initial General speed of Motors (0 - 100)
  -b BRIGHTNESS      Brightness of scrollpHat (0 - 5)
  -i INNERTURNSPEED  Speed of Inner wheels in a turn (0 - 100)
  -o OUTERTURNSPEED  Speed of Inner wheels in a turn (0 - 100)
  -c SHOWCAM         Show Image from Active Cam (True/False)
  -v SOUNDVOLUME     Set Sound volume (0 - 100)
</p>
