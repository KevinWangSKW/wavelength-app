from torchvision import models, transforms
from PIL import Image
import torch

model = models.mobilenet_v2(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

imagenet_classes = [line.strip() for line in open("imagenet_classes.txt")]

def predict_image(image_path):
    img = Image.open(image_path).convert('RGB')
    input_tensor = transform(img).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
        _, predicted = torch.max(output, 1)
    return imagenet_classes[predicted.item()]
