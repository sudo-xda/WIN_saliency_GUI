import MR
import matplotlib.pyplot as plt


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
root.title('Image Saliency OUTR')
frame = tk.Frame(root, bg='#45aaf2')


lbl_pic_path = tk.Label(frame, text='Enter Image Path :', padx=25, pady=25,
                        font=('verdana',16), bg='#45aaf2')
lbl_show_pic = tk.Label(frame, bg='#45aaf2')
entry_pic_path = tk.Entry(frame, font=('verdana',16))
btn_browse = tk.Button(frame, text='Select Image to saliency',bg='grey', fg='#ffffff',
                       font=('verdana',16))


def selectPic():
    global img
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("png images","*.png"),("jpg images","*.jpg")))
    img = Image.open(filename)
    mr = MR.MR_saliency() # initialization
    sal = mr.saliency(filename)
    plt.imshow(sal) # if you want to see result in gray mode
    plt.show()


btn_browse['command'] = selectPic

frame.pack()

lbl_pic_path.grid(row=0, column=0)
entry_pic_path.grid(row=0, column=1, padx=(0,20))
btn_browse.grid(row=2, column=0, columnspan="2", padx=10, pady=10)

root.mainloop()



