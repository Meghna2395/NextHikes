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


# Assuming you have a list of byte strings
# byte_strings = [
#     b'Announcing Python Software Foundation Fellow Members for Q3 2023! \xf0\x9f\x8e\x89',
#     b'Announcing the Deputy Developer in Residence and the Supporting Developer in Residence',
#     b'Python 3.13.0 alpha 3 is now available.',
#     b'EU\xe2\x80\x99s Cyber Resilience Act Passes with Wins for Open Source',
#     b'Python Software Foundation - December 2023 Newsletter'
# ]
     


if __name__=="__main__": 
 python_articles= latest_python_articles()
 byte_strings = latest_python_articles()
 
 if python_articles:
      print("New News in the python.org section")
      for index,articles in enumerate(python_articles, 1):
        print(f"{index}.{articles.encode('utf-8')}")


# if python_articles:
#     print("New News in the python.org section")
#     for index, article in enumerate(python_articles, 1):
#         try:
#             print(f"{index}.{article}")
#         except UnicodeEncodeError:
#             print(f"{index}.{article} [Unicode character not printable]")

   

else:
     print("No articles found..")      
     
     
 
     
     
# python web_scraping.py > word_frequency.txt - Command to print the output in the text file     