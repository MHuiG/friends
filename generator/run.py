# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import yaml
from request_data import request
import json
from request_data import myselenium

data_pool = []

def load_config():
    f = open('_config.yml', 'r',encoding='utf-8')
    ystr = f.read()
    ymllist = yaml.load(ystr, Loader=yaml.FullLoader)
    return ymllist

def github_issuse(data_pool):
    print('\n')
    print('------- github issues start ----------')
    baselink = 'https://github.com/'
    config = load_config()
    try:
        for number in range(1, 100):
            print(number)
            if config['issues']['label']:
                label_plus = '+label%3A' + config['issues']['label']
            else:
                label_plus = ''
            github_link = 'https://github.com/' + config['issues']['repo'] + '/issues?q=is%3A' + config['issues']['state'] + str(label_plus) + '&page=' + str(number)
            github = myselenium.get(github_link)
            
            #github = request.get_data(github_link)
            soup = BeautifulSoup(github, 'html.parser')
            linklist = soup.find_all('a', {'data-testid': 'issue-pr-title-link'})
            #print(len(linklist))
            if len(linklist) == 0:
                print('> end')
                break
            for item in linklist:
                issueslink = baselink + item['href']
                print(issueslink)
                issues_page = request.get_data(issueslink)
                issues_soup = BeautifulSoup(issues_page, 'html.parser')
                try:
                    issues_linklist = issues_soup.find_all('pre')
                    source = issues_linklist[0].text
                    if "{" in source:
                        source = json.loads(source)
                        print(source)
                        data_pool.append(source)
                    #else:
                    #    print("******:"+source)
                except:
                    continue
    except Exception as e:
        #raise Exception(e)
        print('> end')

    print('------- github issues end ----------')
    print('\n')


github_issuse(data_pool)
filename='generator/output/v1/data.json'
with open(filename,'w',encoding='utf-8') as file_obj:
   json.dump(data_pool,file_obj,ensure_ascii=False)
