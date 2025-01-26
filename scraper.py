from bs4 import BeautifulSoup
import requests
import csv 
import pandas as pd
import urllib

indeedWebsite = "https://www.indeed.co.uk/jobs?"

def loadJobs(jobTitle, location, website):
    getVars = {'q' : jobTitle, 'l' : location, 'fromage' : 'last', 'sort' : 'date'}
    url = ( website + urllib.parse.urlencode(getVars))
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    job_soup = soup.find(id="resultsCol")
    return job_soup

