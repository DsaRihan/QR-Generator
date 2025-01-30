from flask import Flask, request, render_template, send_file
import qrcode as qr
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']
    qrc = qr.QRCode(version=1, error_correction=qr.ERROR_CORRECT_H, box_size=10, border=4)
    qrc.add_data(url)
    qrc.make(fit=True)
    img = qrc.make_image(fill_color="red", back_color="black")
    img_path = os.path.join('qr_images', 'qr.png')  # Updated path to save in qr_images directory
    img.save(img_path)
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
