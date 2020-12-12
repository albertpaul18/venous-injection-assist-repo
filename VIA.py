from tkinter import *
from tkinter import filedialog
import cv2


root = Tk()
root.title("VIA")
root.geometry("710x394")
root.resizable(width = False, height = False)

# Here you must specify the path, where the image 'VIA.png' is saved by you i.e. (file= "path where you saved the VIA.png")

photoImage = PhotoImage(file="C:/Users/albta/PycharmProjects/ProjectVeinScanner/VIA.png")
Head = Label(root, image=photoImage)
Head.place(x = 5, y = 8)

# Here you can change the (initialdir="the directory or folder which you want to be opened when fetch button is clicked")

def button_fetch():
    root.filename = filedialog.askopenfilename(initialdir="/Users/albta/OneDrive/Desktop/InputVIA", title="FETCH",
                                               filetypes=(("JPEG", "*.jpeg"),("PNG", "*.png"), ("All files", "*.*")))
    button_2 = Button(root, text="OUTPUT", padx=30, pady=8, fg="white", bg="black", borderwidth=0.1, command=button_output)
    button_2.place(x=300, y=330)

def button_output():

    imgg = cv2.imread(root.filename, 0)
    img1 = cv2.GaussianBlur(imgg, (5, 5), 0)
    clahe = cv2.createCLAHE(clipLimit=5)
    resultclahe = clahe.apply(img1)

    thresh4 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 4)
    edges = cv2.Canny(thresh4, 100, 200)
    Out = cv2.hconcat([thresh4, edges, resultclahe])
    cv2.imshow("Output", Out)



#define button
button_1 = Button(root, text = "FETCH ",padx =33, pady =8.5, fg = "white", bg = "black", borderwidth = 0.1, command = button_fetch)

#put on screen
button_1.place(x = 300, y = 280)

root.mainloop()














