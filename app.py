from flask import Flask, request, jsonify
import threading
import os

from TimeControl import time_check

app = Flask(__name__)
VIDEO_FOLDER = 'videos'
app.config['VIDEO_FOLDER'] = VIDEO_FOLDER
if not os.path.exists(VIDEO_FOLDER):
    os.makedirs(VIDEO_FOLDER)

# 라우트 생성 (실제로 사용하지 않지만 Flask 서버를 동작시키기 위해 빈 라우트 추가)
@app.route('/')
def home():
    return "Flask Server is Running"

# 스레드로 동작할 함수

if __name__ == '__main__':
    # Flask 서버 스레드 시작
    server_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000, 'debug': False, 'threaded': True})
    server_thread.start()

    # 시간 확인 스레드 시작
    time_check_thread = threading.Thread(target=time_check)
    time_check_thread.start()
