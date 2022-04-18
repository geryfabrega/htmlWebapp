import re
from flask import Flask, request, jsonify, after_this_request
import cv2
import numpy as np
import base64
from torchvision.models import detection
import torch

app = Flask(__name__)

@app.route('/test', methods=['GET','POST'])
def test():
    print(request.method)
    if request.method == 'POST':
        request.get_data()
        print("Data Recieved")
        names = saveImage(request.data)
        jsonResp = names
        response = jsonify(jsonResp)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        
    if request.method == 'GET':
        print("GOAT IN THE WATER!")
        jsonResp = {'FLSGHJRLGJRSHGKRSJG': 'fglkrjghkrghrkgj'}
        return jsonify(jsonResp)

def saveImage(data):
    data = data.decode("utf-8")
    data = data.replace("data:image/png;base64,","")
    imgdata = base64.b64decode(data)
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    cascade_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    print("PROGRAM START")
    print("Open Image in local images directory")
    showImg(face_cascade)

def showImg(face_cascade):
    path = "some_image.jpg"
    img = cv2.imread(path, 0)
    faces = face_cascade.detectMultiScale(img)
    color = (255,0,255)
    color2 = (0,255,255)
    thickness = 1
    box_ratio = .22
    for (x, y, w, h) in faces:
        print("new Image!")
        h2 = int(h * box_ratio)
        cv2.rectangle(img, (x, y-h2), (x+w, y+h2), color2, thickness)
        cv2.imwrite("output.jpg",img)




if __name__ == '__main__':
    app.run(host='localhost', port=8989, debug=True, threaded=True)
