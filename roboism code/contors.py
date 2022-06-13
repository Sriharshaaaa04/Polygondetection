import cv2
def coun(image):
      imgGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
      contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
      for contour in contours:
       approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    
       x = approx.ravel()[0]
       y = approx.ravel()[1] - 5

       if len(approx) == 4:
           x1 ,y1, w, h = cv2.boundingRect(approx)
           aspectRatio = float(w)/h
           # print(aspectRatio)
           if aspectRatio >= 0.95 and aspectRatio <= 1.05:
               contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
               print(len(contours))
              #  cv2.drawContours(image, [approx], 0, (0, 0,255), 1)
              #  # contours,hierarchies= cv2.findContours(Canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
           
              #  cv2.putText(image, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0),2)
               n = approx.ravel() 
               i = 0
            


               for j in n : 
                 if(i % 2 == 0): 
                   x = n[i] 
                   y = n[i + 1] 

               # String containing the co-ordinates. 
                 string = str(x)+ " " +str(y) 

                #  if(i == 0): 
                #    # text on topmost co-ordinate. 
                #    cv2.putText(image, "", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0,255)) 
                #  else: 
                #    # text on remaining co-ordinates. 
                #    cv2.putText(image, string, (x, y),cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0,255)) 
                #  i = i + 1