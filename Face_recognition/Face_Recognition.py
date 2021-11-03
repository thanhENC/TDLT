import cv2


img = cv2.imread('banner_Bo_Gia.jpg')

#convert img to grayscale: 3D -> 2D
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

#dlib: load face recognition detector


cv2.imshow(winname="Face Recognition App", mat=gray)

cv2.waitKey(delay=0)

cv2.destroyAllWindows()