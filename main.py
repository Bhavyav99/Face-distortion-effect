import os

import cv2
images=[]
for roots,dirs,files in os.walk('/images'):
    for file in files:
        if file.endswith('.jpg'):
            images.append(os.path.join(roots,file))
#
mage_folder = 'images'
video_name = 'video.avi'
each_image_duration = 5 # in secs
fourcc =  cv2.VideoWriter_fourcc(*'DIVX')

frame = cv2.imread(images[0])
height, width, layers = frame.shape
print(height,width)
video = cv2.VideoWriter(video_name, fourcc, 1.0, (width, height))

for image in images:
    for _ in range(each_image_duration):
        video.write(cv2.imread(image))

# cv2.destroyAllWindows()
video.release()

#

