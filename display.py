import os
import random

def change_wallpaper():
    # change the path in the next line and delete this comment after.
    wallpaper_path = '/media/vinvash/500GB/Wallpapers'
    wallpapers = os.listdir(wallpaper_path)
    
    wallpaper = random.choice(wallpapers)
    command = 'gsettings set org.gnome.desktop.background picture-uri file:///'+ wallpaper_path +"/" + wallpaper
    os.system(command)

    return "wallpaper changed"
