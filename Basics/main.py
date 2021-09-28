from bs4 import BeautifulSoup
import lxml
with open('home.html','r') as file:
    content = file.read()
    #print(content)

soup = BeautifulSoup(content,'lxml')
course_cards = soup.find_all('div',class_='card')
new_dict ={ course.h5.text: course.a.text.split()[-1]  for course in course_cards}

{ print(f'{key} costs {value}') for (key,value) in new_dict.items()  }