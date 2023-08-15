from flask import Flask, request, jsonify

app = Flask(__name__)
video_url = "https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8"

@app.route('/inteligence/activity/', methods=['POST'])
def count():
    data = {"A": video_url, "B": video_url, "C": video_url, "D": video_url, "E": video_url}
    # return jsonify({'message': 'Success'})
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)