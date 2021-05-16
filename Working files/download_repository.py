
import requests
import csv
import os

#github credentials
username="alok275"
token="af967d9b49a618351cc05461653b66d25c662058"

page_number = 1
#https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}
search_repo_url = f"https://api.github.com/search/repositories?q=language:python&page={page_number}&per_page=100&sort=stars&order=desc"



repo_url = requests.get(search_repo_url, auth = (username, token)).json()

count = 1
dir_name = os.listdir('repo/')

print("Writing the repository information such as name, description, url in the file")
with open("data_scrap_url.csv", mode='w') as file:
    writer = csv.writer(file, delimiter=',') 
    writer.writerow(['Id', 'Name', 'Description' ,'Repo Url'])
    while repo_url:
        if 'items' in repo_url:
            for value in repo_url['items']:
                if value['name'] not in dir_name and value['archived'] == False:
                    print(count,"Downloading the ", value['name'], " repository in the file")
                    writer.writerow([count, value['name'], value['description'], value['html_url']])
                    #git command to clone the repository
                    clone = "git -C repo clone {}".format(value["html_url"])
                    os.system(clone)
                    count += 1
                else:
                    if value['archived'] == False:
                        print(count, value['name'], " directory already downloaded")
                        writer.writerow([count, value['name'], value['description'], value['html_url']])
                        count += 1
                dir_name = os.listdir('repo/')
            
            page_number += 1
            search_repo_url = f"https://api.github.com/search/repositories?q=language:python&page={page_number}&per_page=100&sort=stars&order=desc"
            repo_url = requests.get(search_repo_url, auth = (username, token)).json()
        else:
            print("The extraction of github repositories url completed!")
            break

