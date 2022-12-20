import os
import  numpy as np
import cv2
import random
images=[]
for roots,dirs,files in os.walk('/Users/osama-mac/Downloads/img_align_celeba'):
    for file in files:
        if file.endswith('.jpg'):
            images.append(os.path.join(roots,file))
#

video_name = 'video.mp4'
each_image_duration = 2 # in secs
fourcc =  cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

frame = cv2.imread(images[0])
height, width, layers = frame.shape
print(height,width)
cross_image=cv2.resize(cv2.imread('cross.jpg'),(width,height),interpolation=cv2.INTER_NEAREST)
video = cv2.VideoWriter(video_name, fourcc, 1.0, (534, 218))
choosen_images=[]
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


    print(choosen_images.__len__())
    concated_images = np.concatenate([
        cv2.imread(selected_image1), cross_image, cv2.imread(selected_image2)
        ], axis=1)

    for _ in range(each_image_duration):
        video.write(concated_images)

# cv2.destroyAllWindows()
video.release()

#

