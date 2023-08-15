from flask import Flask, request, jsonify

app = Flask(__name__)
video_url = "https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8"

@app.route('/inteligence/activity/', methods=['POST'])
def count():
    data = {"TEST_A": video_url, "TEST_B": video_url, "TEST_C": video_url, "TEST_D": video_url, "TEST_E": video_url}
    # return jsonify({'message': 'Success'})
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)