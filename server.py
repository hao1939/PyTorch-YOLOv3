
from PIL import Image
from flask import Flask, escape, request, jsonify
from score import init, preprocess, predict, postprocess

import io

CONFIG = {
    "model_def": "config/yolov3.cfg",
    "weights_path": "weights/yolov3.weights",
    "class_path": "data/coco.names",
    "conf_thres": 0.8,
    "nms_thres": 0.4,
    "batch_size": 1,
    "n_cpu": 0,
    "img_size": 416,
}

# init model
# TODO need to passing config
init()

app = Flask(__name__)

CONFIG = {
    "model_def": "config/yolov3.cfg",
    "weights_path": "weights/yolov3.weights",
    "class_path": "data/coco.names",
    "conf_thres": 0.8,
    "nms_thres": 0.4,
    "batch_size": 1,
    "n_cpu": 0,
    "img_size": 416,
}


@app.route("/")
def live():
    return "OK!"


@app.route('/score', methods=['POST'])
def score():
    data = request.data
    buffer = io.BytesIO()
    buffer.write(data)
    buffer.seek(0)
    img = Image.open(buffer)
    detections = predict(img)
    return jsonify(detections)


@app.route('/metadata')
def metadata():
    return CONFIG


if __name__ == "__main__":
    app.run()
