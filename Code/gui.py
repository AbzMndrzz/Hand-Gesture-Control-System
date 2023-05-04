from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
from PIL import ImageTk, Image
import webbrowser
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(resource_path(r"assets\\frame0"))


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("TEAM 21CSP35")
window.geometry("920x620")
window.configure(bg="#8FC7FF")

# Navbar Frame
navbar_frame = Frame(window, bg="#131212", height=80)
navbar_frame.pack(side="top", fill="x")

# Buttons color change condition
def change_color(button):
    if button == button_1:
        button_1.config(fg="#5aa200")
        button_2.config(fg="white")
        button_3.config(fg="white")
        button_9.config(fg="white")
    elif button == button_2:
        button_1.config(fg="white")
        button_2.config(fg="#5aa200")
        button_3.config(fg="white")
        button_9.config(fg="white")
    elif button == button_3:
        button_1.config(fg="white")
        button_2.config(fg="white")
        button_3.config(fg="#5aa200")
        button_9.config(fg="white")
    elif button == button_9:
        button_1.config(fg="white")
        button_2.config(fg="white")
        button_3.config(fg="white")
        button_9.config(fg="#ff4037")

# control page Frames
controls_frame = Frame(window, bg="black", width=1024, height=600,highlightthickness=0)
controls_frame.pack(side="left", fill="both", expand=True)

# Other Element's canvas in the main frame
canvas_main = Canvas(
    controls_frame,
    bg="black",
    height=600,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas_main.pack(side="top", pady=0)

# Text
canvas_main.create_text(
    59.0,
    20.0,
    anchor="nw",
    text="WELCOME",
    fill="#5aa200",
    font=("Tajawal", 45 * -1,"bold")
)
canvas_main.create_text(
    310.0,
    20.0,
    anchor="nw",
    text="TO",
    fill="white",
    font=("Tajawal", 45 * -1,"bold")
)
canvas_main.create_text(
    59.0,
    70.0,
    anchor="nw",
    text="AUGMENTED REALITY",
    fill="white",
    font=("Tajawal", 45 * -1,"bold")
)
canvas_main.create_text(
    59.0,
    130.0,
    anchor="nw",
    text="Gone are the days of clunky input devices and cumbersome buttons",
    fill="#FFFFFF",
    font=("Inter Regular",  16* -1)
)
 
# Hand photo
img = Image.open(resource_path("assets\\frame0\\main_image.png"))
img = img.resize((500, 500), Image.LANCZOS) # resize the image
photo = ImageTk.PhotoImage(img)
canvas_main.create_image(
    500,
    -10,
    anchor="nw",
    image=photo
)

# team text
canvas_main.create_text(
    60.0,
    190.0,
    anchor="nw",
    text="Designed and Made by Team 21CSP-35",
    fill="#FFFFFF",
    font=("Inter Regular",  16* -1)
)

# canvas line
canvas_main.create_line(
    60, 220, 120, 220,width=5,fill="#5aa200"
    )

# Start Text
canvas_main.create_text(
    59.0,
    275.0,
    anchor="nw",
    text="CLICK TO START THE MODULE",
    fill="#FFFFFF",
    font=("Inter Regular",  20* -1,"bold")
)
from a import volume
from bright import brightness
from mouse import mouse_button
from media import StartMedia
from FINAL import Start

# create a cpntrol button frame inside controls_frame
buttons_frame = Frame(controls_frame, bg="black", width=1024, height=80,highlightthickness=0)
buttons_frame.pack(side="bottom", padx=0, pady=0)

# buttons to module
button_image_4 = PhotoImage(file=relative_to_assets("volumecard.png"))
button_image_4_small = button_image_4.subsample(2, 2)

button_4 = Button(
    buttons_frame,
    image=button_image_4_small,
    borderwidth=0,
    highlightthickness=0,
    command=volume,
    relief="flat",
    activebackground="#210535", 
    activeforeground="#210535"
)
button_4.pack(side="left", padx=5, pady=0)

button_image_5 = PhotoImage(file=relative_to_assets("brightnesscard.png"))
button_image_5_small = button_image_5.subsample(2, 2)
button_5 = Button(
    buttons_frame,
    image=button_image_5_small,  
    borderwidth=0,
    highlightthickness=0,
    command=brightness,
    relief="flat",
    activebackground="#210535", 
    activeforeground="#210535"
)
button_5.pack(side="left", padx=5, pady=0)

button_image_6 = PhotoImage(file=relative_to_assets("mousecard.png"))
button_image_6_small = button_image_6.subsample(2, 2)
button_6 = Button(
    buttons_frame,
    image=button_image_6_small,
    borderwidth=0,
    highlightthickness=0,
    padx=2,
    pady=2,
    command=mouse_button,
    relief="flat",
    activebackground="#210535", 
    activeforeground="#210535"
)
button_6.configure(highlightbackground="red")
button_6.pack(side="left", padx=5, pady=0)

button_image_7 = PhotoImage(file=relative_to_assets("mediacard.png"))
button_image_7_small = button_image_7.subsample(2, 2)
button_7 = Button(
    buttons_frame,
    image=button_image_7_small,
    borderwidth=0,
    highlightthickness=0,
    command=StartMedia,
    relief="flat",
    activebackground="#210535", 
    activeforeground="#210535"
)
button_7.pack(side="left", padx=5, pady=0)

# add buttons_frame to canvas_main using create_window
canvas_main.create_window(40, 320, anchor="nw", window=buttons_frame)

# About frames
about_frame = Frame(window, bg="#8FC7FF", width=1024, height=1024)
about_frame.pack(side="left", fill="both", expand=True)

# Create a scrollbar and canvas
scrollbar = Scrollbar(about_frame)
scrollbar.pack(side=RIGHT, fill=Y)
canvas = Canvas(about_frame, bg="black", yscrollcommand=scrollbar.set,width=900, height=800,highlightthickness=0)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Link the scrollbar to the canvas
scrollbar.config(command=canvas.yview)

# Create a frame inside the canvas
frame = Frame(canvas, bg="#8FC7FF")
canvas.create_window(0, 0, anchor=NW, window=frame)

# Star image
image = PhotoImage(file=resource_path("assets\\frame0\\stars.png"))
canvas.create_image(-20, 40, image=image, anchor=NW)

# Add the widgets to the frame
canvas.create_rectangle(
    700.0,
    0.0,
    400.0,
    500.0,
    fill="#FFD280",
    outline="")

canvas.create_rectangle(
    1010,
    0,
    710,
    500,
    fill="#ef6c4c",
    outline="")

# Add the image to the canvas
image = PhotoImage(file=resource_path("assets\\frame0\\main_image2.png"))
image = image.subsample(2)
canvas.create_image(350, -30, image=image, anchor=NW)

# TEXT IN ABOUT FRAME
canvas.create_text(
    50.0,
    50.0,
    anchor="nw",
    text="HAND GESTURE",
    fill="#FFD280",
    font=("Inter ExtraBold", 32 * -1,"bold","bold")
)
canvas.create_text(
    50.0,
    90.0,
    anchor="nw",
    text="CONTROL SYSTEM",
    fill="#FFD280",
    font=("Inter ExtraBold", 28 * -1)
)
canvas.create_text(
    50.0,
    150.0,
    anchor="nw",
    text="This is the future of augmented reality (AR) interaction - where hand gestures reign supreme! ",
    fill="#FFFFFF",
    font=("Inter Regular", 20 * -1),
    width=350,
    justify="left")
canvas.create_text(
    50.0,
    230.0,
    anchor="nw",
    text="Our system takes a leap forward, harnessing the power of state-of-the-art computer vision techniques, such as OpenCV and MediaPipe, to create a sleek and efficient hand detection model",
    fill="#FFFFFF",
    font=("Inter Regular", 20 * -1),
    width=350,
    justify="left")

# Github Button
def open_link_git():
    webbrowser.open("https://github.com/nabin012/Hand-Gesture-Control-System")
button_image = PhotoImage(file=resource_path("assets\\frame0\\Github Button.png"))
button = canvas.create_image(50, 380, image=button_image, anchor=NW)
canvas.tag_bind(button, "<Button-1>", lambda event: open_link_git())
button_image = button_image.subsample(1)
canvas.itemconfig(button, image=button_image)

# developer text
canvas.create_text(
    50.0,
    470.0,
    anchor="nw",
    text="OUR TEAM",
    fill="#FFD280",
    font=("Inter Regular", 24 * -1,"bold","bold","bold"),
    width=350,
    justify="left")

# canvas line
canvas.create_line(
    50, 510, 120, 510,width=5,fill="#ef6c4c"
    )

# developers button 1
def open_link_dev1():
    webbrowser.open("www.linkedin.com/in/avay-kushwaha-a721531b3")
button_image_dev1 = PhotoImage(file=resource_path("assets\\frame0\\dev1.png"))
button = canvas.create_image(50, 540, image=button_image_dev1, anchor=NW)
canvas.tag_bind(button, "<Button-1>", lambda event: open_link_dev1())
button_image_dev1 = button_image_dev1.subsample(2)
canvas.itemconfig(button, image=button_image_dev1)

# developers button 2
def open_link_dev2():
    webbrowser.open("https://www.linkedin.com/in/abhash-khanal-3b03b1195")
button_image_dev2 = PhotoImage(file=resource_path("assets\\frame0\\dev2.png"))
button = canvas.create_image(250, 540, image=button_image_dev2, anchor=NW)
canvas.tag_bind(button, "<Button-1>", lambda event: open_link_dev2())
button_image_dev2 = button_image_dev2.subsample(2)
canvas.itemconfig(button, image=button_image_dev2)

# developers button 3
def open_link_dev3():
    webbrowser.open("https://www.linkedin.com/in/aabhash-manandhar-b4ba30248")
button_image_dev3 = PhotoImage(file=resource_path("assets\\frame0\\dev3.png"))
button = canvas.create_image(450, 540, image=button_image_dev3, anchor=NW)
canvas.tag_bind(button, "<Button-1>", lambda event: open_link_dev3())
button_image_dev3 = button_image_dev3.subsample(2)
canvas.itemconfig(button, image=button_image_dev3)

# developers button 4
def open_link_dev4():
    webbrowser.open("https://www.linkedin.com/in/nabin-kc-138871194/")
button_image_dev4 = PhotoImage(file=resource_path("assets\\frame0\\dev4.png"))
button = canvas.create_image(650, 540, image=button_image_dev4, anchor=NW)
canvas.tag_bind(button, "<Button-1>", lambda event: open_link_dev4())
button_image_dev4 = button_image_dev4.subsample(2)
canvas.itemconfig(button, image=button_image_dev4)

# Bind the mousewheel event to the canvas
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Experiemental frame
experimental_frame = Frame(window, bg="#131212", width=960, height=600)
experimental_frame.pack(side="left", fill="both", expand=True)

canvas_exp = Canvas(
    experimental_frame,
    bg="#131212",
    height=1000,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas_exp.pack(side="top", pady=0)

# Add the image to the canvas
image_exp = PhotoImage(file=resource_path("assets\\frame0\\experimental.png"))
image_exp = image_exp.subsample(2)
canvas_exp.create_image(-50, -68, image=image_exp, anchor=NW)

canvas_exp.create_text(
    570.0,
    0.0,
    anchor="nw",
    text="3 MODULE IN 1 ",
    fill="#58c09f",
    font=("Inter Regular", 28 * -1,"bold"),
    width=350,
    justify="left")

# Experimental launch button
# Create a PhotoImage object from an image file
image_button = PhotoImage(file=resource_path("assets\\frame0\\launch.png"))

# Resize the image to be larger
image_button = image_button.subsample(1) # Increase the size by a factor of 2

# Create a button with the image
button_exp = Button(
    experimental_frame,
    image=image_button,
    bg="#131212",
    bd=0,
    command=Start,
    highlightthickness=0,
    activebackground="#131212", 
    activeforeground="#131212",
    padx=0,
    pady=0,
)

# Keep a reference to the image to avoid garbage collection
button_exp.image = image_button

# Set the position of the button
button_exp.place(x=550, y=400) # Move the button down by 50 pixels

# All the available modules in experimental
image_exp1 = PhotoImage(file=resource_path("assets\\frame0\\volumeexp.png"))
image_exp1 = image_exp1.subsample(1)
canvas_exp.create_image(520, 60, image=image_exp1, anchor=NW)

image_exp2 = PhotoImage(file=resource_path("assets\\frame0\\brightnessexp.png"))
image_exp2 = image_exp2.subsample(1)
canvas_exp.create_image(520, 140, image=image_exp2, anchor=NW)

image_exp3 = PhotoImage(file=resource_path("assets\\frame0\\mouseexp.png"))
image_exp3 = image_exp3.subsample(1)
canvas_exp.create_image(520, 220, image=image_exp3, anchor=NW)

image_exp4 = PhotoImage(file=resource_path("assets\\frame0\\mediaexp.png"))
image_exp4 = image_exp4.subsample(1)
canvas_exp.create_image(520, 300, image=image_exp4, anchor=NW)

# page frames
user_manual_frame = Frame(window, bg="#171717", width=960, height=540)
user_manual_frame.pack(side="left", fill="both", expand=True)

canvas_manual = Canvas(
    user_manual_frame,
    bg="#171717",
    height=600,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas_manual.pack(side="top", pady=0)

# user Manual text
canvas_manual.create_text(
    50.0,
    20.0,
    anchor="nw",
    text="USER MANUAL",
    fill="#23A6F0",
    font=("Inter Regular", 32 * -1,"bold"),
    width=350,
    justify="left")
canvas_manual.create_text(
    50.0,
    70.0,
    anchor="nw",
    text="Welcome to our user manual section, where you can find detailed instructions on how to make the most out of our products.",
    fill="white",
    font=("Inter Regular", 14 * -1),
    width=250,
    justify="left")
canvas_manual.create_text(
    50.0,
    150.0,
    anchor="nw",
    text="In this user manual, you'll discover step-by-step guides, helpful tips, and troubleshooting advice that will help you get started with our products quickly and easily.",
    fill="white",
    font=("Inter Regular", 14 * -1),
    width=250,
    justify="left")
canvas_manual.create_text(
    50.0,
    250.0,
    anchor="nw",
    text="Please Contact us on out linkedin if any queries. The link is available in About tab",
    fill="white",
    font=("Inter Regular", 14 * -1),
    width=250,
    justify="left")
canvas_manual.create_text(
    50.0,
    320.0,
    anchor="nw",
    text="Click the buttons available in the frame to learn how to use particular control system and access the documentation such as report.",
    fill="white",
    font=("Inter Regular", 14 * -1),
    width=250,
    justify="left")

# documentation button
def open_link_documentation():
    webbrowser.open("https://docs.google.com/document/d/1Jw1V1KYq4Z2aGlyiZcPccakB4L6hF5ZV/edit?usp=share_link&ouid=108880190849985482336&rtpof=true&sd=true")

image_docmanual = PhotoImage(file=resource_path("assets\\frame0\\docmanual.png"))
image_docmanual = image_docmanual.subsample(2)

button_docmanual = Button(
    user_manual_frame,
    image=image_docmanual,
    bg="#131212",
    bd=0,
    highlightthickness=0,
    activebackground="#131212", 
    activeforeground="#131212",
    padx=0,
    pady=0,
    command=open_link_documentation,
)
button_docmanual.image = image_docmanual
button_docmanual.place(x=60, y=420) 

# volume manual button
def open_link_volmanual():
    webbrowser.open("https://docs.google.com/document/d/1u2ulNWP9ty5srC-FUuobSdK7sWRnUIhE/edit?usp=sharing&ouid=108880190849985482336&rtpof=true&sd=true")

image_volmanual = PhotoImage(file=resource_path("assets\\frame0\\volumemanual.png"))
image_volmanual = image_volmanual.subsample(2)

button_volmanual = Button(
    user_manual_frame,
    image=image_volmanual,
    bg="#131212",
    bd=0,
    highlightthickness=0,
    activebackground="#131212", 
    activeforeground="#131212",
    padx=0,
    pady=0,
    command=open_link_volmanual,
)
button_volmanual.image = image_volmanual
button_volmanual.place(x=350, y=30) 

# brightness manual button
def open_link_brightnessmanual():
    webbrowser.open("https://docs.google.com/document/d/1UM3v3Yk4MuTRbpY6ChkBDkDV51apbkfj/edit?usp=sharing&ouid=108880190849985482336&rtpof=true&sd=true")

image_brightness = PhotoImage(file=resource_path("assets\\frame0\\brightnessmanual.png"))
image_brightness = image_brightness.subsample(2)

button_brightness = Button(
    user_manual_frame,
    image=image_brightness,
    bg="#131212",
    bd=0,
    highlightthickness=0,
    activebackground="#131212", 
    activeforeground="#131212",
    padx=0,
    pady=0,
    command=open_link_brightnessmanual,
)
button_brightness.image = image_brightness
button_brightness.place(x=350, y=170) 

# mouse manual button
def open_link_mousemanual():
    webbrowser.open("https://docs.google.com/document/d/191U7ly-1yUuxdZ68JcRpF7LPy9MtDAnG/edit?usp=share_link&ouid=108880190849985482336&rtpof=true&sd=true")

image_mouse = PhotoImage(file=resource_path("assets\\frame0\\mousemanual.png"))
image_mouse = image_mouse.subsample(1)

button_mouse = Button(
    user_manual_frame,
    image=image_mouse,
    bg="#131212",
    bd=0,
    highlightthickness=0,
    activebackground="#131212", 
    activeforeground="#131212",
    padx=0,
    pady=0,
    command=open_link_mousemanual,
)
button_mouse.image = image_mouse
button_mouse.place(x=600, y=70) 

# media manual button
def open_link_mediamodule():
    webbrowser.open("https://docs.google.com/document/d/1sjc4U-9NCFBjmxZo1bGYr4rHCgLbdL5j/edit?usp=share_link&ouid=108880190849985482336&rtpof=true&sd=true")

image_media = PhotoImage(file=resource_path("assets\\frame0\\mediamodule.png"))
image_media = image_media.subsample(2)

button_media = Button(
    user_manual_frame,
    image=image_media,
    bg="#131212",
    bd=0,
    highlightthickness=0,
    activebackground="#131212", 
    activeforeground="#131212",
    padx=0,
    pady=0,
    command=open_link_mediamodule,
)
button_media.image = image_media
button_media.place(x=620, y=320) 

# All in 1 button
def open_link_allin1():
    webbrowser.open("https://docs.google.com/document/d/1zo5xxdIK9GvYmogDUGgVmYEQQ31Jfi73/edit?usp=share_link&ouid=108880190849985482336&rtpof=true&sd=true")

image_allin1 = PhotoImage(file=resource_path("assets\\frame0\\allin1module.png"))
image_allin1 = image_allin1.subsample(1)

button_allin1 = Button(
    user_manual_frame,
    image=image_allin1,
    bg="#131212",
    bd=0,
    highlightthickness=0,
    activebackground="#131212", 
    activeforeground="#131212",
    padx=0,
    pady=0,
    command=open_link_allin1,
)
button_allin1.image = image_allin1
button_allin1.place(x=350, y=300) 

# canvas line
canvas_manual.create_line(
    320, 600, 320, 0, width=5, fill="#5aa200"
)

# Navbar Buttons
def raise_controls():
    controls_frame.tkraise()
def raise_user_manual():
    user_manual_frame.tkraise()
def raise_about():
    about_frame.tkraise()
def raise_experimental():
    experimental_frame.tkraise()

button_1 = Button(
    text="Controls",
    bg="#131212",
    fg="white",
    activebackground="#131212",
    activeforeground="white",
    font=("Arial", 16),
    borderwidth=0,
    highlightthickness=10,
    command=raise_controls,
    relief="flat"
)
button_1.place(
    x=400.0,
    y=20.0,
    width=120.0,
    height=40.0
)
button_1.bind("<Button-1>", lambda event: change_color(button_1))

button_2 = Button(
    text="User Manual",
    bg="#131212",
    fg="white",
    activebackground="#131212",
    activeforeground="white",
    font=("Arial", 16),
    borderwidth=0,
    highlightthickness=0,
    command=raise_user_manual,
    relief="flat"
)
button_2.place(
    x=520,
    y=20.0,
    width=140.0,
    height=40.0
)
button_2.bind("<Button-1>", lambda event: change_color(button_2))

button_3 = Button(
    text="About",
    bg="#131212",
    fg="white",
    activebackground="#131212",
    activeforeground="white",
    font=("Arial", 16),
    borderwidth=0,
    highlightthickness=0,
    command=raise_about,
    relief="flat"
)
button_3.place(
    x=650.0,
    y=20.0,
    width=120.0,
    height=40.0
)
button_3.bind("<Button-1>", lambda event: change_color(button_3))

button_9 = Button(
    text="Experimental",
    bg="#131212",
    fg="white",
    activebackground="#131212",
    activeforeground="white",
    font=("Arial", 16),
    borderwidth=0,
    highlightthickness=0,
    command=raise_experimental,
    relief="flat"
)
button_9.place(
    x=750.0,
    y=20.0,
    width=140.0,
    height=40.2
)
button_9.bind("<Button-1>", lambda event: change_color(button_9))

# Pack Pages on top of each other
controls_frame.place(x=0, y=80)
user_manual_frame.place(x=0, y=80)
about_frame.place(x=0, y=80)
experimental_frame.place(x=0, y=80)

# Raise Controls Frame by default
controls_frame.tkraise()

window.resizable(False, False)
window.mainloop()