import pyshorteners as sh
import customtkinter as custom
from tkinter import messagebox
import webbrowser
import tkinter as tk

app = custom.CTk()
app.geometry("300x120")
app.iconbitmap("favicon.ico")
app.title("ENCURTADOR DE LINK")

texto = custom.CTkLabel(app, text="Link: ")
texto.place(x=10, y=15)

urll = custom.CTkEntry(app, placeholder_text="Link longo", width=240)
urll.place(x=55, y=15)

def ctrlC(text):
    app.clipboard_clear()
    app.clipboard_append(text)
    app.update() 

def click ():
    try:
        if urll is not None:
            
            url = urll.get()
            link = sh.Shortener()
            surl = link.tinyurl.short(url)
            
            def callback(url):
                webbrowser.open(url)
                
            app = tk.Tk()
            app.title("Link curto")
            app.geometry("200x70")
            app.iconbitmap('favicon.ico')
            
            short = tk.Label(app, text=surl, fg="blue", cursor="hand2")
            short.pack()
            short.bind("<Button-1>", lambda e: callback(url))
            short.place(x=10, y=10)           
            
            ctrlC(surl)
    
        else:
            print("urll é None")
            
    except Exception as e:
        messagebox.showerror('ERRO!', f'Erro ao gerar link: {str(e)}')

btn = custom.CTkButton(app, text="Encurtar", command=click
).place(x=80, y=65)


app.mainloop()
