from tkinter import *
from tkinter import ttk
import poke_api
import image_lib
import os
import ctypes

# Get The Path Of The Script And Its Parent Directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cache_dir = os.path.join(script_dir, 'images')

# Make The Dir Path
if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)

# Create The Window
root = Tk()
root.title("Pokémon Viewer")
root.minsize(700, 700)

# Set The Window Icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
icon_path = os.path.join(script_dir, 'pokeball.ico')
root.iconbitmap(icon_path)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create The Frame
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Add The Image To The Frame
img_poke = PhotoImage(file=os.path.join(script_dir,'Pokemonpik.png'))
lbl_poke_image = ttk.Label(frame,image=img_poke)
lbl_poke_image.grid(row=0, column=0)

# Add The Pokemon Names Pull-Down Menu 
pokemon_names_list = poke_api.get_pokemon_names()
cbox_poke_names = ttk.Combobox(frame, values=pokemon_names_list, state='readonly')
cbox_poke_names.set("Select a Pokemon")
cbox_poke_names.grid(row=1, column=0, padx=10, pady=10)


def handle_pokemon_sel(event):

    # Get The Name Of The Selected Pokemon
    pokemon_name = cbox_poke_names.get()

    # Download And Save The Artwork For The Selected Pokemon
    global image_path
    image_path = poke_api.download_pokemon_artwork(pokemon_name, image_cache_dir)

    # Display The Pokemon Artwork
    if image_path is not None:
        img_poke['file'] = image_path
    # Allows Use Of Button    
    btn_get_info.state(['!disabled'])

cbox_poke_names.bind('<<ComboboxSelected>>', handle_pokemon_sel)


def set_pokemon_background():

    pokemon_background = image_lib.set_desktop_background_image(image_path)
   
    return pokemon_background

# Create The Button
btn_get_info = ttk.Button(frame, text='Set as Desktop Image', command=set_pokemon_background, state=DISABLED)
btn_get_info.grid(row=2, column=0, padx=10, pady=10)




root.mainloop()