from flask import jsonify, request
import cv2
import requests
import os
import numpy as np


APP_ROOT = os.path.dirname(os.path.abspath(__file__)).split("routes")[0]


def deskew_image():

    data = request.get_json()
    url = data["image_path"]

    if "http" in url:
        try:
            response = requests.get(url, stream=True).raw
        except Exception:
            return jsonify({"message": "invalid url."}), 400
        else:
            if response.status == 404:
                return jsonify({"message": "file not found."}), 404
            image = np.asarray(bytearray(response.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            image = np.array(image)
    else:
        image_file_path = os.path.isfile(url)
        if image_file_path:
            image = cv2.imread(url)
        else:
            return jsonify({"message": "file not found."}), 404

    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception:
        return jsonify({"message": "request not processable."}), 422
    else:
        edges = cv2.Canny(gray, 50, 200, apertureSize=3)

        width = 1000

        lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)

        r, theta = lines[0][0]

        x0 = int(r * np.cos(theta))
        y0 = int(r * np.sin(theta))

        x1 = int(x0 + width * (np.sin(theta)))
        y1 = int(y0 - width * (np.cos(theta)))

    try:
        slope = (y1 - y0) / (x1 - x0)
    except Exception:
        return jsonify({"message": "not possible to deskew."}), 406
    else:
        angle = slope * (180 / np.pi)
    
        # cv2.line(image, (x0, y0), (x1, y1), (0, 255, 0), 2).
        
        # draw a line on the image.

        height, width, channel = image.shape
        center = (width // 2, height // 2)

        rotational_matrix = cv2.getRotationMatrix2D(center, angle, scale=1)
        rotated_image = cv2.warpAffine(image, rotational_matrix, (width, height), borderMode=cv2.BORDER_REPLICATE)

        image_path = os.path.join(APP_ROOT, "static", "image.jpg")
        cv2.imwrite(image_path, rotated_image)

        deskewed_image_url = request.host_url + "static/image.jpg"

        return jsonify({"deskewed_image_url": deskewed_image_url, "skewed_angle": angle}), 200
