# Micropython devices

A small library of micropython devices.

## ESP8266

* adc - returns a smoothed 10 sample raw ADC reading or voltage, calibrated for the [HiLetgo ESP8266 NodeMCU](https://www.amazon.co.uk/gp/product/B0791FJB62/ref=ppx_yo_dt_b_asin_title_o08__o00_s00?ie=UTF8&psc=1)

## Generic 

* [LM35](http://www.ti.com/lit/ds/symlink/lm35.pdf) one wire temp sensor, hook up to the ADC.
* [Adafruit BM280](https://www.adafruit.com/product/2652) I2C Temperature Humidity Pressure Sensor.