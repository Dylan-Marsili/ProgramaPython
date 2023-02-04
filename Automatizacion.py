from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
ventana=Tk()
width_of_window = 427
height_of_window = 250
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
ventana.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
ventana.overrideredirect(1)



Frame(ventana, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(ventana, text='AUTOMATIZACION', fg='white', bg='#272727')  
label1.configure(font=("Game Of Squids", 24, "bold"))   
label1.place(x=80,y=90)

label2=Label(ventana, text='Cargando...', fg='white', bg='#272727') 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

image_a=ImageTk.PhotoImage(Image.open('C:/Users/Dylan/Documents/python/imagenes/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('C:/Users/Dylan/Documents/python/imagenes/c1.png'))




for i in range(3):
    l1=Label(ventana, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    ventana.update_idletasks()
    time.sleep(0.5)

    l1=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(ventana, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    ventana.update_idletasks()
    time.sleep(0.5)

    l1=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(ventana, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    ventana.update_idletasks()
    time.sleep(0.5)

    l1=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(ventana, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(ventana, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    ventana.update_idletasks()
    time.sleep(0.5)



ventana.destroy()
import tkinter
import pyautogui as pag
import time
import customtkinter
import os
import webbrowser
from PIL import ImageTk,Image
app = customtkinter.CTk()
app.geometry("600x440")
app.title('Login')



def button_function():

    app.destroy()
    ventana = customtkinter.CTk()
    ventana.geometry("1200x600")
    ventana.resizable(0,0)
    ventana.title("Bienvenido")
    
    
    # Grid 1x2
    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)

    ventana.tabview = customtkinter.CTkTabview(master=ventana, width=1200, height=600, bg_color="black")
    ventana.tabview.grid(row=0, column=0, sticky="nsew")
    ventana.tabview.add("Home")
    ventana.tabview.add("Juegos")
    ventana.tabview.add("Aplicaciones")
    ventana.tabview.add("Otros")
    ventana.tabview.add("Optimizacion")
    ventana.tabview.add("Password Cracker")

    # Crear tercer frame

    #Funciones
    def password():
        import random

        letras = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"
        numeros = "0123456789"

        unir = f'{letras}{numeros}'
        longitud = 10
        contraseña = random.sample(unir, longitud)
        password = "".join(contraseña)
        ventana.tercer_frame_textbox = customtkinter.CTkTextbox(ventana.tabview.tab("Password Cracker"), height=30, width=30)
        ventana.tercer_frame_textbox.grid(row=3, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        ventana.tercer_frame_textbox.insert("0.0", password)
    #BOTONES

    ventana.tercer_frame_boton_1 = customtkinter.CTkButton(ventana.tabview.tab("Password Cracker"), text="Generar Password",font=customtkinter.CTkFont(size=20, weight="bold"),height=50, width=300, command =password)
    ventana.tercer_frame_boton_1.grid(row=1, column=2, padx=20, pady=20)

    ventana.mainloop()

img1=ImageTk.PhotoImage(Image.open("C:/Users/Dylan/Documents/python/imagenes/pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

l3=customtkinter.CTkLabel(master=frame, text="Forgot password?",font=('Century Gothic',12))
l3.place(x=155,y=195)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)


img2=customtkinter.CTkImage(Image.open("C:/Users/Dylan/Documents/python/imagenes/Google__G__Logo.svg.webp").resize((20,20), Image.ANTIALIAS))
img3=customtkinter.CTkImage(Image.open("C:/Users/Dylan/Documents/python/imagenes/124010.png").resize((20,20), Image.ANTIALIAS))
button2= customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290)

button3= customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button3.place(x=170, y=290)

app.mainloop()
