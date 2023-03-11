#this is a ytdownloader with a simple gui
from pytube import YouTube
import customtkinter

def submit():
    global yt
    global ys
    url = str(UrlEingabe.get("1.0", UrlEingabe.index("end-1c")))
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Yt Downloader")

anweisung = customtkinter.CTkLabel(root, text="Insert YouTube Url:", font=("Miriam Mono CLM Bold", 24))
anweisung.pack(padx=1, pady=10)

UrlEingabe = customtkinter.CTkTextbox(root, height=1, width=300, font=("Miriam Mono CLM", 24))
UrlEingabe.pack()

submitButton = customtkinter.CTkButton(root,fg_color="#750e19", text="submit", font=("Miriam Mono CLM Bold", 24), command=submit)
submitButton.pack(padx=1, pady=10)

anleitung = customtkinter.CTkLabel(root, text="""Insert your YouTube video URL into the textbox above. 
Click submit to start the download! 
The video will be downloaded in the same path, 
where this progrem is stored!
""", font=("Miriam Mono CLM Bold", 14))
anleitung.pack(padx=1, pady=10)

root.mainloop()