import requests
from bs4 import BeautifulSoup




def latest_python_articles():
 url = "https://www.python.org/"
 response = requests.get(url)
 
 if response.status_code==200:
     soup =BeautifulSoup(response.text,"html.parser")
     latest_arcticles=[]
     
     for article in soup.select(".blog-widget li"):
         title = article.a.text.strip()
         latest_arcticles.append(title)
         
     return latest_arcticles
 
 else:
     print(f"Fail to retrieve data.status code:{response.status_code}") 

     


if __name__=="__main__": 
 python_articles= latest_python_articles()

 
 if python_articles:
      print("New News in the python.org section")
      for index,articles in enumerate(python_articles, 1):
        print(f"{index}.{articles}")




   

else:
     print("No articles found..")      
     
     
 
     
     
# python web_scraping.py > word_frequency.txt - Command to print the output in the text file     