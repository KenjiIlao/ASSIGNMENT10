import cv2
import datetime
from pyzbar.pyzbar import decode 

Cam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:


    _,img=Cam.read()
    data,one, _=detector.detectAndDecode(img)
    success, frame = Cam.read()
    if data:


        a=data
        break

    cv2.imshow('TUMINGIN KA SAKIN!',img)
    if cv2.waitKey(1)==ord('v'):
        continue

    for captureinfomartions in decode(frame):
        
        #coverting information to text file

        Make_txt_file = open("Information.txt", "w")
        Make_txt_file.write(f"{captureinfomartions.data.decode('utf-8')}\n" )
        
 #the time when scan the qr code    
        Date = datetime.datetime.now()
        Make_txt_file.write(Date.strftime("Date: %m/%d/%y \n"))
        Make_txt_file.write(Date.strftime("Time: %H:%M:%S"))  
        Make_txt_file.close()

Cam.release(a)
cv2.destroyAllWindows()