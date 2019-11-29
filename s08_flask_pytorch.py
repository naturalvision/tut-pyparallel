from flask import Flask
from flask import request
from PIL import Image
import torch
from torchvision import models
from torchvision import transforms


app = Flask(__name__)

have_cuda = torch.cuda.is_available()
model = models.mobilenet_v2(pretrained=True).eval()
if have_cuda:
    model = model.cuda()
labels = open('imagenet-classes.txt').read().strip().splitlines()


def transform(image):
    transform = transforms.Compose([
        transforms.Resize(224, interpolation=2),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
            ),
        ])
    tensor = transform(image)
    tensor = tensor.reshape([1, *tensor.shape])
    if have_cuda:
        tensor = tensor.cuda()
    return tensor


@app.route('/predict', methods=['POST'])
def predict():
    buf = request.files['image'].stream
    image = Image.open(buf)
    tensor = transform(image)
    probas = model(tensor)
    label = labels[probas[0].argmax()]
    return "It's a {}!".format(label)
