import cv2
import os
from natsort import natsorted
import pickle
import math

def push_image_in_second(frame, duration_in_s):
    for i in range(duration_in_s):
        video.write(frame)
        
image_folder = './image'
video_name = '../video_combine/input.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".PNG")]
images = natsorted(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

with open('mylist', 'rb') as f: 
    duration_list = pickle.load(f)

for i, e in enumerate(duration_list):
    duration_list[i] = math.ceil(duration_list[i])

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

frame_cover = cv2.imread("cover.PNG")
push_image_in_second(frame_cover, 5)

for index, image in enumerate(images):
    print("Processing: "+ image + " "+ str(round(index*100/len(images), 2)) +"% finish", end='\r')
    frame = cv2.imread(os.path.join(image_folder, image))
    push_image_in_second(frame, duration_list[index])

push_image_in_second(frame_cover, 20)    

cv2.destroyAllWindows()
video.release()
for i,e in enumerate(images):
    os.remove(os.path.join(image_folder, e))
os.remove("cover.PNG")