from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
from tkinter import filedialog 
import cv2 as cv 

class Vision:
    def __init__(self,root):
        self.root = root
        self.photo_button = Button(self.root, text = 'File to be visioned', command = self.choose_file)
        self.number_of_images= None
        self.img = ImageTk.PhotoImage(Image.open("/Users/hendy/Desktop/AI/AI_files/opencv-course/Section #3 - Faces/imgreco.png"))
        Label( self.root, image = self.img).grid(row=0,column=0,columnspan=3)
       
    def choose_file(self):
        self.root.filename = filedialog.askopenfilename(title = 'Open your file', filetypes = [("jpg files","*.jpg")]) # to guarantee that the file's type is an image
        img_name = self.root.filename
        
        img = cv.imread(img_name)
        haar_cascade = cv.CascadeClassifier('haar_face.xml')
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.9, minNeighbors=1)
        
        # 1.1 and 1 in the above code are conventional values

        for (x,y,w,h) in faces_rect:
            cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        #plt.imshow(img , cmap="gray")
        cv.imshow('Detected Faces', img)
        self.root.geometry("800x530")
        number_of_images = 'Number of faces found = ' + str(len(faces_rect))
        Label(self.root, text=number_of_images).grid(row=2,column=1)
        cv.waitKey(0)
        cv.destroyAllWindows()
        cv.waitKey(1)  

        

def run_face_recognition(root):
    root.geometry("700x430")
    root.title('Computer Vision Interface')
    app = Vision(root)
    
    app.photo_button.grid(row=1,column=1)
    
    


        