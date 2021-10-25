import os 
import assistant_details as ad
import file_search



music_path = "/home/vinvash/Music/Songs"


def play_music():
    if ad.is_ubuntu():
        os.system("rhythmbox-client --play")
        return "Playing Music"

    else:
        #windows code 
        return "For windows os, it's not available right now."



def pause_music():
    if ad.is_ubuntu():
        os.system("rhythmbox-client --pause")
        return "Music paused"
    else:
        #windows code 
        return "For windows os, it's not available right now."

def stop_music():
    if ad.is_ubuntu():
        os.system("rhythmbox-client --stop")
        return "Music stopped"

    else:
        return "Not available for windows yet"



def next_song():
    if ad.is_ubuntu():
        os.system("rhythmbox-client --next")
        return "Playing next song"
    else:
        return "Not availble for windows yet"

def previous_song():
    if ad.is_ubuntu():
        os.system("rhythmbox-client --previous")
        return "Playing previous song"
    else:
        return "Not availble for windows yet"



def play_specific_song(song_name):

    song_name = song_name.replace('play', '')
    if ad.is_ubuntu():
        file_search.set_root(music_path)
        songs = file_search.searchFile(song_name)
        try:
            song_uri = songs[0]
            command = 'rhythmbox-client --play-uri="' + song_uri + '"'
            os.system(command)
            return ("playing " + song_name)
        except:
            return("Specified song not found on your computer")
            
    else:
        return "Not availble for windows yet"




play_specific_song("Gun Label")