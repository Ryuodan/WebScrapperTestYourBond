import requests
from bs4 import BeautifulSoup
#get the url and download the html
page = requests.get(input("Enter the url of the quiz :"))
#parse the html (formating)
soup=BeautifulSoup(page.content,"html.parser")
#get all the questions
questions=soup.find_all(class_="question hidden unanswered")
question_text=[]
for item in questions:
	question_text.append(item.find('h3').get_text())
#get all the correct answers
answers=soup.find_all(class_="answer correct")
answer_text=[]
for item in answers:
	answer_text.append(item.get_text())
#making the output 
for i in range(0,15):
	print(str(i+1)+"-Q: "+question_text[i]+" A: "+answer_text[i]+"\n")
