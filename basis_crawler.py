import requests
from bs4 import BeautifulSoup
import re
import os, csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

memberLinks=[]
errorpages = []
def getMemberLinks():
    memberLinks.clear()
    for x in range(0,1040,20):
        page = requests.get('https://www.basis.org.bd/index.php/members_area/member_list/'+str(x))
        if page.status_code == requests.codes.ok:
           soup = BeautifulSoup(page.content,"lxml")
           links = soup.find_all("td",class_="bodytext")
           for link in links:
               anchor  = link.select('a[href^="http://www.basis.org.bd/index.php/members_area/member_detail/"]')
               if(anchor):
                  memberDetails         = {}
                  memberDetails["url"]  = anchor[0]['href']
                  memberDetails["name"] = anchor[0].find("b").text
                  memberLinks.append(memberDetails)
        else:
           print("Getting error for page number " + str(x) )
           errorpages.append(str(x))
    return
if __name__ == "__main__":
  getMemberLinks()

