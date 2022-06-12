import board
import digitalio
import analogio
import config

Led = digitalio.DigitalInOut(board.GP14)
Led.direction = digitalio.Direction.OUTPUT

Led.value = True

# INPUTS

Button = digitalio.DigitalInOut(board.GP18)
Button.direction = digitalio.Direction.INPUT
Button.pull = digitalio.Pull.UP

rfLevel = analogio.AnalogIn(board.GP26)
batLevel = analogio.AnalogIn(board.GP27)


def batery_voltage():
    #return batLevel.value / 65535 * batLevel.reference_voltage
    return (batLevel.value*2) / 65535 * 4.3

def rf_millivoltage():
    return (rfLevel.value / 65535 * rfLevel.reference_voltage)*100


def batPCT():
    #return str(round(((65535/batLevel.value)*100),0))+"%"
    return '{message: <4}'.format(message=str(round(batery_voltage() / 3.3) * 100)+"%")


# 10dB accuracy
def rfDbWideband():
    # reference mv/dB
    mvDb=25
    # all things dB
    offsetdB=-100
    transformerGain=12
    widebandLoss=-3

    inputDb=rf_millivoltage()/mvDb
    returnValue=inputDb+transformerGain+widebandLoss+offsetdB+config.antennaGainWideband
    return '{message: <13}'.format(message=str(round(returnValue,2))+" dB")

def batLevel():
    if batery_voltage() > 4.1:
        return '100%'
    elif batery_voltage() > 4:
        return ' 90%'
    elif batery_voltage() > 3.9:
        return ' 80%'
    elif batery_voltage() > 3.8:
        return ' 60%'
    elif batery_voltage() > 3.7:
        return ' 50%'
    elif batery_voltage() > 3.6:
        return ' 40%'
    elif batery_voltage() > 3.5:
        return ' 30%'
    elif batery_voltage() > 3.4:
        return ' 20%'
    elif batery_voltage() > 3.3:
        return ' 10%'
    elif batery_voltage() > 3:
        return '  0%'
