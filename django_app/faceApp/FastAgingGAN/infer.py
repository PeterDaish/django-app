import os
import random
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import torch
import numpy as np
from PIL import Image
from torchvision import transforms


from faceApp.FastAgingGAN.gan_module import Generator

parser = ArgumentParser()
parser.add_argument('--image_dir', default='/Downloads/WIN_20210730_12_14_02_Pro.jpg', help='The image directory')


@torch.no_grad()
def main():
    args = parser.parse_args()
    image_paths = [os.path.join(args.image_dir, x) for x in os.listdir(args.image_dir) if
                   x.endswith('.png') or x.endswith('.jpg')]
    model = Generator(ngf=32, n_residual_blocks=9)
    ckpt = torch.load('pretrained_model/state_dict.pth', map_location='cpu')
    model.load_state_dict(ckpt)
    model.eval()
    trans = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])
    fig, ax = plt.subplots(2, 6, figsize=(20, 10))
    random.shuffle(image_paths)
    for i in range(0,1):
        img = Image.open(image_paths[i])
        img = trans(img).unsqueeze(0)
        aged_face = model(img)
        aged_face = (aged_face.squeeze().permute(1, 2, 0).numpy() + 1.0) / 2.0
        ax[0, i].imshow((img.squeeze().permute(1, 2, 0).numpy() + 1.0) / 2.0)
        ax[1, i].imshow(aged_face)
    plt.show()


if __name__ == '__main__':
    main()

#predict is an extension of the original main function, used within the django application
#predict takes in the image we want as input and returns the processed image as output.
def predict(image):
    #args = parser.parse_args()
    #image_paths = [os.path.join(args.image_dir, x) for x in os.listdir(args.image_dir) if
    #               x.endswith('.png') or x.endswith('.jpg')]
    print("predict opened")
    model = Generator(ngf=32, n_residual_blocks=9)
    ckpt = torch.load('faceApp/FastAgingGAN/pretrained_model/state_dict.pth', map_location='cpu')
    model.load_state_dict(ckpt)
    model.eval()
    trans = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])
    print("model opened and initialised")
    #fig, ax = plt.subplots(2, 6, figsize=(20, 10))
    #random.shuffle(image_paths)
    for i in range(0,1):
        img = image
        img = trans(img).unsqueeze(0)
        print("image squeezed 1")
        aged_face = model(img)
        print("image predicted")
        squeezed_aged_face = aged_face.squeeze()
        print("face squeezed")
        permuted_squeezed_aged_face = ((squeezed_aged_face.permute(1, 2, 0).detach().numpy() + 1.0) / 2.0)
        print("face permutated")
        print("image predicted 2")
        im = Image.fromarray((permuted_squeezed_aged_face * 255).astype(np.uint8))
        
        image = im
        #
        # ax[0, i].imshow((img.squeeze().permute(1, 2, 0).numpy() + 1.0) / 2.0)
        #ax[1, i].imshow(aged_face)
    print("returning image")

    return image