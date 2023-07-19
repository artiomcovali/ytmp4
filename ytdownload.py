import plistlib
import tkinter
from PIL import Image
import os, sys, subprocess
import customtkinter
from pytube import YouTube
from tkinter import filedialog
import urllib.request

filenameOut = ""
filename = ""

def downloadVid():
   
        filename = filedialog.askdirectory()
        if len(filename)==0:
            title1.configure(text="Please Select a Valid Directory" + filename, text_color="red", corner_radius=5,)
            return
        title1.configure(text = "0 %", text_color = "white")
        progress.set(0)
        title1.update()
        ytLink = link.get()
        try:
            ytObj = YouTube(ytLink, on_progress_callback=on_progress)
        except:
            title1.configure(text="Invalid URL. Please try again", text_color="red")
        vidImg = ytObj.thumbnail_url
        vidTitle = ytObj.title
        ytVid = ytObj.streams.get_highest_resolution()
        if filename!="":
            
                ytVid.download(filename)
                urllib.request.urlretrieve(
  vidImg,
   "thumbnail.png")
                my_image = customtkinter.CTkImage(light_image=Image.open("thumbnail.png"),
                                  dark_image=Image.open("thumbnail.png"),
                                  size=(180, 100))

                image_label = customtkinter.CTkLabel(app, image=my_image, text="", bg_color="grey") 
                image_label.place(relx=0.5, rely=0.83, anchor=tkinter.CENTER)
                title1.configure(text="Video Downloaded to: " + filename, text_color="white")
                title2.configure(text=vidTitle, fg_color="grey", corner_radius=5)
        

def downloadAud():
    
        filename = filedialog.askdirectory()
        if len(filename)==0:
            title1.configure(text="Please Select a Valid Directory" + filename, text_color="red", corner_radius=5,)
            return
        title1.configure(text = "0 %", text_color = "white")
        progress.set(0)
        title1.update()
        ytLink = link.get()
        try:
            ytObj = YouTube(ytLink, on_progress_callback=on_progress)
        except:
            title1.configure(text="Invalid URL. Please try again", text_color="red")
        vidImg = ytObj.thumbnail_url
        vidTitle = ytObj.title
        ytVid = ytObj.streams.get_audio_only()
        if filename!="":
            
                output = ytVid.download(filename)
                base, ext = os.path.splitext(output)
                new_file = base + '.mp3'
                os.rename(output, new_file)
                urllib.request.urlretrieve(
  vidImg,
   "thumbnail.png")
                my_image = customtkinter.CTkImage(light_image=Image.open("thumbnail.png"),
                                  dark_image=Image.open("thumbnail.png"),
                                  size=(180, 100))

                image_label = customtkinter.CTkLabel(app, image=my_image, text="", bg_color="grey") 
                image_label.place(relx=0.5, rely=0.83, anchor=tkinter.CENTER)
                title1.configure(text="Audio Downloaded to: " + filename, text_color="white")
                title2.configure(text=vidTitle, fg_color="grey", corner_radius=5)   
    
   
def on_progress(stream,chunk, bytes_remaining):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytes_remaining
    percentage = bytesDownloaded / totalSize * 100
    per = str(int(percentage))
    title1.configure(text=per+" %")
    title1.update()
    progress.set(float(percentage/100))


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("650x400")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(master=app, text="Enter a YouTube Link",width=200, height=25,)
title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)



linkVar = tkinter.StringVar()
link = customtkinter.CTkEntry(master=app, width=350, height=40, textvariable=linkVar)
link.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

buttonVid = customtkinter.CTkButton(master=app, text="Download Video", fg_color="red", corner_radius=5, hover_color="Orange", command=downloadVid)
buttonVid.place(relx=0.38, rely=0.32, anchor=tkinter.CENTER)

buttonAud = customtkinter.CTkButton(master=app, text="Download Audio", fg_color="red", corner_radius=5, hover_color="Orange", command=downloadAud)
buttonAud.place(relx=0.62, rely=0.32, anchor=tkinter.CENTER)

title1 = customtkinter.CTkLabel(master=app, text="0 %")
title1.place(relx=0.5, rely=0.445, anchor=tkinter.CENTER)

title2 = customtkinter.CTkLabel(master=app, text="")
title2.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

progress = customtkinter.CTkProgressBar(master=app, width=400)
progress.set(0)
progress.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


app.mainloop()