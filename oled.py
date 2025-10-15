import time
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont
import board
import busio
import adafruit_ssd1306

# --- Inisialisasi OLED ---
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# --- Inisialisasi HC-SR04 ---
TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# --- OLED setup ---
width = oled.width
height = oled.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

def tampilkan_text(line1, line2=""):
    """Menampilkan dua baris teks di OLED"""
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 16), line1, font=font, fill=255)
    draw.text((0, 32), line2, font=font, fill=255)
    oled.image(image)
    oled.show()

def ukur_jarak():
    """Mengukur jarak dengan HC-SR04"""
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    # Trigger ultrasonic
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Hitung waktu pantulan
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    durasi = pulse_end - pulse_start
    jarak = durasi * 17150  # Kecepatan suara 34300 cm/s dibagi 2
    return round(jarak, 2)

# --- Main Loop ---
try:
    tampilkan_text("HC-SR04", "Memulai...")
    time.sleep(1)

    while True:
        try:
            jarak = ukur_jarak()
            print(f"Jarak: {jarak} cm")
            tampilkan_text("Jarak Terdeteksi:", f"{jarak} cm")
            time.sleep(0.5)
        except Exception as e:
            tampilkan_text("Error:", str(e))
            time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram dihentikan.")
    tampilkan_text("Program", "Dihentikan.")
    GPIO.cleanup()
