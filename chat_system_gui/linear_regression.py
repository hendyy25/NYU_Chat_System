from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
from tkinter import filedialog 

class Predict:
    def __init__(self,root= None):
        self.root = root
        self.photo_button = Button(self.root, text = 'Choose File to Apply Linear Regression', command = self.choose_file)
        self.accuracy = 'Choose a file first'
        self.regression_coefficient = 'Choose a file first'
        self.y_intercept = 'Choose a file first'
        
    
    def choose_file(self):
        self.root.filename = filedialog.askopenfilename(title = 'Open your file', filetypes = [("csv files","*.csv")]) # to guarantee that the file's type is an image
        global file_name
        file_name = self.root.filename
        self.apply_regression(file_name)
        
        
    
    def apply_regression(self,file_name):
        
        # necessary libraries for linear regression 
        import pandas as pd # to read the csv file 
        from sklearn import linear_model # a python built-in library for linear regression
        
        df = pd.read_csv(file_name) 
        area_df = df.drop('price', axis = 'columns')
        price_df = df.drop('area',axis='columns')
        
        # create a linear regression object 

        reg = linear_model.LinearRegression() # an instance of the linear regression model

        # reg is the regression model 

        reg.fit(area_df,price_df) # fits data as (x,y)
        self.accuracy = reg.score(area_df,price_df)
        self.regression_coefficient = reg.coef_
        self.y_intercept = reg.intercept_ 
        root.geometry("800x570")
        Label(root, text = 'The accuracy of our lienar model = ' + str("{:.2f}".format(app.accuracy))).grid(row=2,column=0)
        Label(root, text = ' The reg coef of our lienar model = ' + str("{:.2f}".format(app.regression_coefficient[0][0]))).grid(row=3,column=0)
        Label(root, text = '       The intercep of our lienar model = ' + str("{:.2f}".format(app.y_intercept[0]))).grid(row=4,column=0)
        
        e  = Entry(root, width = 20,fg = "blue")
        e.grid(row=6,column=0)
        e.insert(0, 'Enter your area (Delete this!)') # default text
        def clicked():
            label = Label(root, text = "The predicted price = " + str("{:.2f}".format(reg.predict([[int(e.get())]])[0][0])))
            label.grid(row=8,column=0)

        my_button = Button(root, text = 'Predict price',command = clicked, fg = "blue") # no () after the function's name, fg, forground color, bg, background color
        my_button.grid(row=7, column=0)
        Button(root,text='Exit',fg='red',command=root.destroy).grid(row=9,column=1)




root = Tk()
root.geometry("700x430")
root.title('Linear Regression')
#root.iconbitmap('icon.jpg')
app = Predict(root)



linear_regression_img = ImageTk.PhotoImage(Image.open("/Users/hendy/Desktop/AI/AI_files/opencv-course/Section #3 - Faces/machine_learning.jpeg"))
linear_regression_label = Label( image = linear_regression_img).grid(row=0,column=0,columnspan=3)
app.photo_button.grid(row=1,column=1)




root.mainloop()
       
        