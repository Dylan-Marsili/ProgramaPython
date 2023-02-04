import tkinter
import pyautogui as pag
import time
import customtkinter
import os
import webbrowser
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("600x440")
app.title('Login')



def button_function():

    app.destroy()
    ventana = customtkinter.CTk()
    ventana.geometry("1200x600")
    ventana.title("Bienvenido")
    
    
    # Grid 1x2
    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)

    ventana.tabview = customtkinter.CTkTabview(ventana, width=700, height=450)
    ventana.tabview.grid(row=0, column=0, sticky="nsew")
    ventana.tabview.add("Home")
    ventana.tabview.add("2")
    ventana.tabview.add("Password Cracker")
    ventana.tabview.add("Tab 4")
    ventana.tabview.add("Tab 5")
    ventana.tabview.add("Tab 6")

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

img1=ImageTk.PhotoImage(Image.open("pattern.png"))
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


img2=customtkinter.CTkImage(Image.open("Google__G__Logo.svg.webp").resize((20,20), Image.ANTIALIAS))
img3=customtkinter.CTkImage(Image.open("124010.png").resize((20,20), Image.ANTIALIAS))
button2= customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290)

button3= customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button3.place(x=170, y=290)




# You can easily integrate authentication system 

app.mainloop()