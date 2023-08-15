from flask import Flask, jsonify, request

app = Flask(__name__)
the_number = 20
video_url = "https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8"

@app.route('/inteligence/activity/', methods=['POST'])
def count():
    data = {}
    for i in range(1, the_number + 1):
        if i < 10:
            data["TEST_00"+str(i)] = video_url
        else:
            data["TEST_0"+str(i)] = video_url
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)