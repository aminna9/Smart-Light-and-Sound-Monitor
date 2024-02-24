from machine import Pin, ADC, PWM
from time import sleep

led = Pin(10, Pin.OUT)
buzzer_num = 12
buzzer_start_freq = 600
buzzer_end_freq = 1400
buzzer = PWM(Pin(buzzer_num))
buzzer.freq(100)
buzzer.duty_u16(int(30 * 655.36))
sound_pin = Pin(21, Pin.IN)
ldr = ADC(26)
led.off()

sound_threshold = 0.5

while True:
    sound_level = sound_pin.value()
    if sound_level > sound_threshold:
        led.on()
        buzzer.freq(1000)
        buzzer.duty_u16(int(30 * 655.36))
    else:
        led.off()
        buzzer.freq(100)
        buzzer.duty_u16(int(30 * 655.36))

    light_intensity = ldr.read_u16()
    print(light_intensity)

    if light_intensity < 15000:  # if low light intensity
        led.off()  # turn off LED
        buzzer.duty_u16(0)  # turn off buzzer
    elif light_intensity > 20000:  # if high light intensity
        led.on()  # turn on LED
        buzzer.duty_u16(int(30 * 655.36))  # turn on buzzer
    else:  # if medium light intensity
        if led.value() == 1:  # if LED is currently on
            led.off()  # turn off LED
            buzzer.duty_u16(0)  # turn off buzzer

    sleep(0.1)
