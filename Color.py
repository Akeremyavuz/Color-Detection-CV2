import cv2
from PIL import Image
from util import get_limits

#give values as BGR
green = [0,255,0]
red = [0,0,255]
yellow = [0,255,255]
blue = [255,0,0]

cap = cv2.VideoCapture(0)
while True: 

  ret, frame = cap.read()

  hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   
  #lowerLimit, upperLimit = get_limits(color=yellow)
  #lowerLimit, upperLimit = get_limits(color=green)
  #lowerLimit, upperLimit = get_limits(color=red)
  #lowerLimit, upperLimit = get_limits(color=blue)
  

  mask =cv2.inRange(hsvImage,lowerLimit, upperLimit)

  mask_= Image.fromarray(mask)

  bbox = mask_.getbbox()

  if bbox is not None:
     x1,y1,x2,y2 = bbox
     frame=cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)   

  print(bbox)

  cv2.imshow("Frame", frame)   

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
cap.relase()

cv2.destroyAllWindows()
