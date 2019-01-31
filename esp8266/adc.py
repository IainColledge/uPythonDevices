#
# ADC, return voltage from reading
#
from machine import ADC


def get_raw():
    adc = ADC(0)
    off = 0
    t = 0

    for x in range(10):
        t += (adc.read())

    return (t/10) + off


def get_volts():
    # The HiLetgo NodeMCU 1.0 seems to have a reference voltage of 3.12 volts, not 3.3
    div = 3.12/1024

    return get_raw() * div
