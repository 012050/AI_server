from flask import Flask, jsonify

app = Flask(__name__)

the_number = 23
video_url = "https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8"

@app.route('/video/server/', methods=['POST'])
def count():
    data = {}
    for i in range(1, the_number + 1):
        file_name = "TEST_" + str(i).zfill(5)
        data[file_name] = video_url
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
