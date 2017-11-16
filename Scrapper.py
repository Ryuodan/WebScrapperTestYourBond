import requests
from bs4 import BeautifulSoup
#get the url and download the html
page = requests.get("https://testyourbond.com/quiz3/6122253")
#parse the html (formating)
soup=BeautifulSoup(page.content,"html.parser")
#get all the questions
questions=soup.find_all(class_="question hidden unanswered")
question=[]
for item in questions:
	question.append(item.find('h3').get_text())
#get all the correct answers
answers=soup.find_all(class_="answer correct")
answer=[]
for item in answers:
	answer.append(item.get_text())
for i in range(0,15):
	print(str(i+1)+"-Q: "+question[i]+" A: "+answer[i]+"\n")