
usage: DalekV2MainV2.py [-h] [-r RIGHTSPEED] [-l LEFTSPEED] [-s SPEED]
                        [-b BRIGHTNESS] [-i INNERTURNSPEED]
                        [-o OUTERTURNSPEED] [-c SHOWCAM] [-v SOUNDVOLUME]

PiWars Dalek Control Program

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


# Turn all motors off
def stop():
# forward(speed): Sets all 4 motors to move forward at speed. 0 <= speed <= 100
def forward(Speed):
# backward(speed): Sets all 4 motors to reverse at speed. 0 <= speed <= 100
def backward(Speed):
# turnForward(leftSpeed, rightSpeed): Moves forwards in an arc by setting different speeds. 0 <= leftSpeed,rightSpeed <= 100
def turnForward(leftSpeed, rightSpeed):
# turnBackward(leftSpeed, rightSpeed): Moves backwards in an arc by setting different speeds. 0 <= leftSpeed,rightSpeed <= 100
def turnBackward(leftSpeed, rightSpeed):
# spinLeft(speed): Sets motors to turn opposite directions at speed. 0 <= speed <= 100
def spinLeft(Speed):
# spinRight(speed): Sets motors to turn opposite directions at speed. 0 <= speed <= 100
def spinRight(Speed):

#======================================================================	
# Test Functions
#======================================================================	

def FRF(Speed):
def FLF(Speed):
def BRF(Speed):
def BLF(Speed):
def FRB(Speed):
def FLB(Speed):
def BRB(Speed):
def BLB(Speed):
