import tkinter
import customtkinter
from pytube import YouTube

def StartDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback = on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text = ytObject.title, text_color = 'white')
        video.download()
        finishLabel.configure(text = 'Download Complete!')
    except:
        finishLabel.configure(text = 'Youtube link is invalid', text_color = 'red')

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion  = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    percentage.configure(text = per + '%')
    percentage.update()

    #update progress bar
    progressBar.set(float(percentage_of_compeletion) / 100)

#System Settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

#Our app frame
app = customtkinter.CTk()
app.geometry('720 x 480')
app.title('Youtube Download')

#Adding UI Elements
title =  customtkinter.CTkLabel(app, text = 'Insert a youtube link')
title.pack(padx = 10, pady = 10)

#Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = url_var)
link.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

#Progress percentage
percentage = customtkinter.CTkLabel(app, text = '0%')
percentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width = 400)
progressBar.set(0)
progressBar.pack(padx = 10, pady = 10)

#Download Button
download = customtkinter.CTkButton(app, text = 'Download', command = StartDownload)
download.pack(padx = 10, pady = 10)

#Run app
app.mainloop()