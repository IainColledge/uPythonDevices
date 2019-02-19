#
# LM35 10 mv per degree C
#
# Call with a reference to an adc function that returns get_volts()
#
# from esp8266 import adc
# import lm35
#
# temp = lm35.get_temp(adc)
#


def get_temp(adc):
    return adc.get_volts() * 100
