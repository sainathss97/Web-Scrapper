import time

from bs4 import BeautifulSoup
import requests

unfamiliar_skill = input("Enter the skills that should not be included: ")
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=django&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all(name = 'li' ,class_= "clearfix job-bx wht-shd-bx" )


    for index, job in  enumerate(jobs):


        recent = job.find('span', class_='sim-posted').span.text

        if "few" in recent:
            comp_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            link =      job.header.h2.a['href']
            skills =    job.find('span', class_='srp-skills').text.replace(' ', '')
            if unfamiliar_skill not in skills:
                with open(f'job_{index}.txt','w') as file:
                    file.write(f' Company Name: {comp_name.strip()}  \n  Required Skills:{skills.strip()}  \n  Link:{link}');
                    # file.write((f' Required Skills:{skills.strip()}');
                    # file.write((f' Link:{link}\n')
                print(f"File Saved!{index}")
        else:
            pass


if __name__ =='__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} seconds ....")
        time.sleep(time_wait*60)