import requests     
from output_module import output 
from internet import check_internet_connection 
  
def get_news(): 
    if check_internet_connection():
      
        # BBC news api 
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=6bdbce7bee4c4520bd4a95eedf19bcd0"
    
        # fetching data in json format 
        open_bbc_page = requests.get(main_url).json() 
    
        # getting all articles in a string article 
        article = open_bbc_page["articles"] 
    
        # empty list which will  
        # contain all trending news 
        results = [] 
        
        for ar in article: 
            results.append(ar["title"]) 
            
        # change the range to 3 for demo.
        # for i in range(3):
        for i in range(len(results)): 
            
            # printing all trending news 
            output(str(i + 1) + ".) " +results[i]) 
        

        return "So these were the top news today!"
    else:
        return "Please check your internet connection!"
    
     
  
