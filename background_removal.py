import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
output = change_bg.color_bg("C:/Users/resu/Desktop/celeba/face distortion/00007.jpg", colors = (0, 128, 0))
cv2.imwrite("7.jpg", output)