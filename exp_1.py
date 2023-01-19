def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)



from PIL import Image
import cv2
import os
import  numpy as np
import cv2
import random
from numpy import asarray

images=[]
for roots,dirs,files in os.walk('C:/Users/resu/Desktop/celeba/face distortion'):
    for file in files:
        if file.endswith('.jpg'):
            images.append(os.path.join(roots,file))


video_name = 'exp1_1.mp4'
fourcc =  cv2.VideoWriter_fourcc('m', 'p', '4', 'v')


video = cv2.VideoWriter(video_name, fourcc, 1, (1846,926))

choosen_images=[]

img1 = Image.open("C:/Users/resu/Desktop/CVP Project/Face-distortion-effect/cross_background.png")
print(img1.size)
for img  in range(0,20):
    selected_image1=None
    selected_image2=None

    while images:
        selected_image1 = random.choice(images)
        if selected_image1 not in choosen_images:
            choosen_images.append(selected_image1)
            break

    while images:
        selected_image2 = random.choice(images)
        if selected_image2 not in choosen_images:
            choosen_images.append(selected_image2)
            break


    img1 = Image.open("C:/Users/resu/Desktop/CVP Project/Face-distortion-effect/cross_background.png")
    #img2 = Image.open(selected_image1)

    img2 = change_contrast(Image.open(selected_image1), 100)
    img3 = change_contrast(Image.open(selected_image2), 100)
    #img3 = Image.open(selected_image2)

    new_width = 400
    new_height = 500
    img2 = img2.resize((new_width, new_height), Image.ANTIALIAS)
    img3 = img3.resize((new_width, new_height), Image.ANTIALIAS)

    img1.paste(img2, (200,200))
    img1.paste(img3, (1250, 200))
    numpydata = np.asarray(img1)
    #img1.show()

    video.write(cv2.cvtColor(np.array(numpydata), cv2.COLOR_RGB2BGR))
    print("done")

video.release()
print("video done")

