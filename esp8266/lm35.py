#
# LM35 10 mv per degree C
#
from . import adc


def get_temp():
    return adc.get_volts() * 100
