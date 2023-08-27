import random

from flask import Flask, jsonify, request

app = Flask(__name__)

the_number = 23
start_number = 1
end_number = the_number + 1
video_url = "https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8"

def random_number(Number_):
    min_value = 10 ** (Number_ - 1)
    max_value = (10 ** Number_) - 1
    random_number = random.randint(min_value, max_value)
    return int(random_number)

@app.route('/video/server/', methods=['POST'])
def video():
    global start_number
    global end_number
    data = {}
    for i in range(start_number, end_number):
        file_name = "TEST_" + str(i).zfill(5)
        data[file_name] = video_url
    start_number = end_number
    end_number = end_number + the_number
    return jsonify(data)

@app.route('/inteligence/activity', methods=['POST'])
def api_send():
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
