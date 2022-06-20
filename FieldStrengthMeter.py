import board
import digitalio
import analogio
import config
import math

Led = digitalio.DigitalInOut(board.GP14)
Led.direction = digitalio.Direction.OUTPUT

Led.value = True

# INPUTS

Button = digitalio.DigitalInOut(board.GP18)
Button.direction = digitalio.Direction.INPUT
Button.pull = digitalio.Pull.UP

rfLevel = analogio.AnalogIn(board.GP26)
batLevel = analogio.AnalogIn(board.GP27)

def myround(x, base=10):
    return base * round(x/base)

def batery_voltage():
    return ((batLevel.value / 65535 * batLevel.reference_voltage)*2)


def rf_millivoltage():
    return (rfLevel.value / 65535 * rfLevel.reference_voltage)*100


def batPCT():
    #return str(round(((65535/batLevel.value)*100),0))+"%"
    if (batery_voltage()-3 < 0):
        return '{message: <4}'.format(message="USB")
    else:
        return '{message: <4}'.format(message=str(myround(((batery_voltage()-2) / 1.4) * 100, 10))+"%")



# 10dB accuracy
def rfDbWideband():
    # reference mv/dB
    mvDb=25
    # all things dB
    offsetdB=-92 # Dynamic range
    transformerGain=12 # UNUN
    widebandLoss=-3 # from 0-500Mhz

    inputDb=rf_millivoltage()/mvDb
    dBm=inputDb+transformerGain+widebandLoss+offsetdB+config.antennaGainWideband
    #dbuV=dBm+107
    #returnValue=10*(((dbuV/1)-120/20))
    return '{message: <13}'.format(message=str(round(dBm,2))+" dBm")


# https://www.aaronia.com/fileadmin/media-archive/conversion_formulas.pdf