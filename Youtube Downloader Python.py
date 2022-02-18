from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Troya Youtube Video Downloader")

Label(root,text = 'Videos Descargables Youtube', font ='arial 20 bold').pack()
##introducir link
link = StringVar()

Label(root, text = 'Pegar Link aqui: ', font='arial 15 bold').place(x = 160 , y = 60)
linken= Entry(root, width = 70, textvar = link).place(x = 32, y = 90)
#funcion de descarga

def Descargable():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download('/Users/Troya/VideosP')
    Label(root, text = 'DESCARGADO', font = 'arial 15').place(x = 180, y = 210)
    
Button(root, text = 'DESCARGAR', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Descargable).place(x = 185, y = 145)


root.mainloop()
