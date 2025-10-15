# LAPORAN PRAKTIKUM SENSOR ULTRASONIK HC-SR04 DENGAN RASPBERRY PI
Mencoba mengoperasikan Raspberry Pi dan integrasi sensor
## Anggota Kelompok
|Nama|NRP|
|----|---|
|Rayka Dharma Pranandita  | 5027241039|
|Muhammad Khosyi Syehab   | 5027241089|
|Zaenal Mustofa        | 5027241018|

### **Overview:**     
Dalam penugasan ini kami melakukan dua project atau dua tes, pertama implementasi sensor ultrasonik pada raspberry pi (**success**) dan implementasi sensor ultrasonik yang dioutput ke layar OLED (**gagal**)

### **Pendahuluan**      
Sensor ultrasonik HC-SR04 merupakan sensor yang digunakan untuk mengukur jarak suatu objek dengan memanfaatkan gelombang suara ultrasonik. Prinsip kerjanya adalah dengan memancarkan gelombang ultrasonik melalui pin *trigger* dan menerima pantulan gelombang tersebut melalui pin *echo*. Lama waktu pantulan kembali digunakan untuk menghitung jarak objek terhadap sensor.

Dalam praktikum ini, Raspberry Pi digunakan sebagai mikrokontroler yang mengatur pengiriman dan penerimaan sinyal ultrasonik, serta menampilkan hasil pengukuran jarak pada terminal.

---

### **Tujuan**
Tujuan dari percobaan ini adalah:
1. Memahami cara kerja sensor HC-SR04 dalam mengukur jarak menggunakan gelombang ultrasonik.  
2. Mengimplementasikan komunikasi input-output digital pada Raspberry Pi menggunakan pustaka `RPi.GPIO`.  
3. Menampilkan hasil pengukuran jarak secara real-time melalui terminal.
---

### **Dasar Teori**
Sensor ultrasonik HC-SR04 bekerja berdasarkan **prinsip pantulan gelombang suara (echo)**. Sensor ini terdiri dari dua bagian utama, yaitu:
- **Transmitter (Trigger)**: Mengirimkan gelombang ultrasonik dengan frekuensi sekitar 40 kHz.
- **Receiver (Echo)**: Menerima pantulan gelombang dari objek.

Waktu tempuh gelombang dari transmitter ke objek dan kembali ke receiver diukur, kemudian dikonversi menjadi jarak dengan rumus:
``
Jarak (cm) = Waktu tempuh (sekon) * 34300 / 2
``
dengan 34300 cm/s adalah kecepatan suara di udara

---
### **Alat dan Bahan**
- 1 unit Raspberry Pi (misalnya Raspberry Pi 4 Model B)
- 1 sensor ultrasonik **HC-SR04**
- Kabel jumper (male-female)
- Breadboard (opsional)
- Layar monitor atau SSH terminal untuk menampilkan output

---

### **Rangkaian**
Hubungkan pin sensor HC-SR04 ke Raspberry Pi sebagai berikut:

| Pin HC-SR04 | Pin Raspberry Pi (BCM) | Keterangan |
|--------------|-------------------------|-------------|
| VCC          | 5V                      | Tegangan daya sensor |
| GND          | GND                     | Ground |
| TRIG         | GPIO 23                 | Pin output pemicu gelombang |
| ECHO         | GPIO 24                 | Pin input penerima pantulan |

---

### **Kode Program**
```python
import RPi.GPIO as GPIO
import time

# Gunakan penomoran BCM
GPIO.setmode(GPIO.BCM)

# Atur GPIO
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def hitung_jarak():
    # Set TRIG rendah untuk memastikan tidak ada pulsa
    GPIO.output(TRIG, False)
    time.sleep(0.5)

    # Kirim pulsa selama 10 mikrodetik
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Waktu sinyal mulai
    while GPIO.input(ECHO) == 0:
        waktu_mulai = time.time()

    # Waktu sinyal diterima kembali
    while GPIO.input(ECHO) == 1:
        waktu_akhir = time.time()

    durasi = waktu_akhir - waktu_mulai

    # Kecepatan suara = 34300 cm/s
    jarak = durasi * 17150
    jarak = round(jarak, 2)

    return jarak

try:
    while True:
        jarak = hitung_jarak()
        print(f"Jarak: {jarak} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Menghentikan program")
    GPIO.cleanup()
```

### Eksperimen menggunakan sensor ultrasonik dengan output terminal:
#### Hasil Akhir:
![](assets/dist-output.jpeg)
Bisa dilihat hasil perhitungan jarak dioutput secara real-time di terminal
```
Jarak: 24.7 cm
Jarak: 24.7 cm
Jarak: 26.7 cm

```
![](assets/dist.jpeg)
### Eksperimen menggunakan sensor ultrasonik dengan output OLED:
#### Hasil Akhir:
![](assets/oled1.jpeg)
![](assets/oled.jpeg)    
Layar menghasilkan output bintik bintik hitam dengan background putih saja, tidak menampilkan output jarak sensor ultrasonik
## Documentation:
![fotbar](assets/fotbar.jpeg)
![fotbar2](assets/fotbar1.jpeg)
