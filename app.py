import pyshorteners as sh
import customtkinter as custom
from tkinter import messagebox
import webbrowser

app = custom.CTk()
app.geometry("300x160")
app.iconbitmap("favicon.ico")
app.title("ENCURTADOR DE LINK")

texto = custom.CTkLabel(app, text="Link: ")
texto.place(x=10, y=15)

texto2 = custom.CTkLabel(app, text="Link gerado e já copiado: ")
texto2.place(x=80, y=90)

urll = custom.CTkEntry(app, placeholder_text="Link longo", width=230)
urll.place(x=45, y=15)

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
                
            
            
            short = custom.CTkLabel(app, text=surl)
            short.place(x=70, y=120)           
            
            ctrlC(surl)
    
        else:
            print("urll é None")
            
    except Exception as e:
        messagebox.showerror('ERRO!', f'Erro ao gerar link: {str(e)}')

btn = custom.CTkButton(app, text="Encurtar", command=click
).place(x=80, y=55)


app.mainloop()
