import time
from PIL import Image, ImageDraw, ImageFont
import board
import busio
import adafruit_ssd1306

# --- Inisialisasi OLED ---
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Bersihkan layar
oled.fill(0)
oled.show()

# Siapkan kanvas gambar
width = oled.width
height = oled.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Fungsi untuk teks tengah
def center_text(text, y=24):
    text_width = draw.textlength(text, font=font)
    x = (width - text_width) // 2
    draw.text((x, y), text, font=font, fill=255)

# Animasi loading
def loading_animation():
    for i in range(1, 13):
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        center_text("Starting...", 16)
        dots = "." * (i % 4)
        center_text(dots, 36)
        oled.image(image)
        oled.show()
        time.sleep(0.2)

# Efek scroll teks
def scroll_text(message, delay=0.02):
    text_width = draw.textlength(message, font=font)
    for x in range(width, -text_width, -2):
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, 24), message, font=font, fill=255)
        oled.image(image)
        oled.show()
        time.sleep(delay)

# Efek blink
def blink_text(text, times=5, delay=0.3):
    for i in range(times):
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        if i % 2 == 0:
            center_text(text)
        oled.image(image)
        oled.show()
        time.sleep(delay)

# --- Jalankan animasi ---
loading_animation()
scroll_text("Hello Raspberry Pi!")
blink_text("Welcome!", 6)
center_text("🎉 Ready to Go 🎉")
oled.image(image)
oled.show()
