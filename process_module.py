from output_module import output
from time_module import get_time, get_date  # for displaying the time to the console.
from input_module import take_input
from database import *
from internet import check_internet_connection, check_on_wikipedia  # for performing actions related to internet surfing.
import assistant_details
from web_jobs import open_facebook, open_google, open_youtube, close_browser
from music import play_music, pause_music, stop_music, next_song, previous_song, play_specific_song  # for playing music
from display import change_wallpaper
from news_module import get_news

def process(query):

    if 'play' in query and 'music' not in query:
        answer = get_answer_from_memory('play')
    else:
        answer = get_answer_from_memory(query)


    if answer == "get time details":
        return ("Time is " + get_time())

    elif answer == "check internet connection":
        if check_internet_connection():
            return "Internet is connected."
        else:
            return "Internet is not connected."

    elif answer == "tell date":
        return "Date is " + get_date()

    elif answer == "on speak":
        return turn_on_speech()
   
    elif answer == "off speak":
        return turn_off_speech()

    elif answer == "close browser":
        close_browser()
        return "closing browser"        

    elif answer == "open facebook":
        open_facebook()
        return "opening facebook"

    elif answer == "open google":
        open_google()
        return "opening google"

    elif answer == "open youtube":
        open_youtube()
        return "opening youtube"

    elif answer == "play music":
        return play_music()

    elif answer == 'play':
        return play_specific_song(query)

    elif answer == "pause music":
        return pause_music() 

    elif answer == "stop music":
        return stop_music() 
    
    elif answer == "next song":
        return next_song()

    elif answer == "previous song":
        return previous_song()

    elif answer == 'change wallpaper':
        return change_wallpaper()

    elif answer == 'get news':
        return get_news()

    elif answer == 'change name':
        output("Okay! what do you want to call me")
        temp = take_input()
        if temp == assistant_details.name:
            return "Can't change. I think you're happy with my old name"
        else:
            update_name(temp)
            assistant_details.name = temp
            return "Now you can call me " + temp

    else:
        output("I dont know this one. Should I search it on the internet?")
        ans = take_input()
        if "yes" in ans.lower():
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer

        else:
            output("May you please tell me what it means?")
            ans = take_input()
            if "it means" in ans.lower():
                ans = ans.replace("it means", "")
                ans = ans.strip()

                value = get_answer_from_memory(ans)
                if value == "":
                    return "I can't help with this one "
                
                else:
                    insert_question_and_answer(query, value)
                    return "Thanks, I will remember it from the next time"
            
            else:
                return "I can't help with this one."
        