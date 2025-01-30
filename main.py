from flask import Flask, request, render_template, send_file
import qrcode 
import os
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']
    qrc = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4)
    qrc.add_data(url)
    qrc.make(fit=True)
    img = qrc.make_image(fill_color="red", back_color="black")
    img_path = "qr.png"
    img.save(img_path)
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)



