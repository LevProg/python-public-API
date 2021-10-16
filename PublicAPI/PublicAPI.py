import os
import torch
import pandas as pd
import numpy as np
from PIL import Image
from torchvision import models,transforms
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

DEVICE = 'cpu'
model=torch.load('model')
model=model.to(DEVICE)
model.eval()
UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_test_transform():
    tran = [
        transforms.Resize((128,128)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ]
    return transforms.Compose(tran)
tr=get_test_transform()
def get_label_replacers(df_path: str = 'train.csv'):
    label2int = {}
    int2label = {}
    data = pd.read_csv(df_path)
    was = sorted(data.label.unique())
    will = sorted(data.label.astype('category').cat.codes.unique())
    for i in range(len(will)):
        label2int[was[i]], int2label[will[i]] = will[i], was[i]

    return label2int, int2label

label2int, int2label = get_label_replacers('train.csv')

def get_class(path, model,  transform=tr):
    x = Image.open(path)
    x = x.convert('RGB')
    if transform:
        x = transform(x)
    x = x[np.newaxis, :]
    x = x.to(DEVICE)
    with torch.no_grad():
        pred = model(x)
    return int2label[pred.argmax(1).numpy()[0]]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            y=get_class(os.path.join(app.config['UPLOAD_FOLDER'], filename),model)
            return y
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
