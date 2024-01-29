from flask import Flask, render_template
import subprocess
import requests
import time
import threading

app = Flask(__name__)

RTMP_PORT = 2000
STREAM_KEY = 'test'
VIDEO_SOURCE = 'koala.mp4'  # Video dosyasının adını buraya ekleyin

def get_random_name():
    # Random User Generator API
    api_url = 'https://randomuser.me/api/'
    response = requests.get(api_url)
    data = response.json()

    # İsim verisi çıkartma
    name_data = data['results'][0]['name']
    full_name = f"{name_data['first']} {name_data['last']}"

    return full_name

def start_stream():
    # RTMP sunucuya yayın başlatma komutu
    subprocess.Popen(['ffmpeg', '-re', '-stream_loop', '-1', '-i', VIDEO_SOURCE, '-c:v', 'libx264', '-b:v', '800k', '-c:a', 'aac', '-vf', 'drawtext=textfile=overlay.txt:fontsize=48:reload=1', '-f', 'flv', f'rtmp://localhost:{RTMP_PORT}/live/{STREAM_KEY}'])

def update_overlay():
    while True:
        # API'den rastgele veri çekme
        overlay_data = get_random_name()

        # Overlay dosyasını güncelleme
        with open('overlay.txt', 'w') as overlay_file:
            overlay_file.write(overlay_data)

        time.sleep(10)  # Her on saniyede bir overlay güncelle bir süre gecikme oluyor değişim olurken.

def start_flask():
    # Flask web sunucusunu başlatma
    app.run(port=2002, host="0.0.0.0")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # RTMP yayınını başlatma işlemini bir thread içinde başlatma
    stream_thread = threading.Thread(target=start_stream)
    stream_thread.start()

    # Overlay güncelleme işlemini bir thread içinde başlatma
    overlay_thread = threading.Thread(target=update_overlay)
    overlay_thread.start()

    # Flask web sunucusunu başlatma işlemini bir thread içinde başlatma
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()
