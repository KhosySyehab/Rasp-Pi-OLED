import time
import board
import busio
import adafruit_ssd1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

# --- Setup GPIO untuk HC-SR04 ---
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# --- Setup I2C untuk OLED ---
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# --- Font dan tampilan ---
font = ImageFont.load_default()

while True:
    # Kirim pulsa ultrasonik
    GPIO.output(TRIG, False)
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    duration = pulse_end - pulse_start
    distance = round(duration * 17150, 2)

    # Bersihkan layar OLED
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Tulis teks
    draw.text((10, 20), f"Jarak: {distance} cm", font=font, fill=255)

    # Tampilkan ke OLED
    oled.image(image)
    oled.show()

    print(f"Jarak: {distance} cm")
