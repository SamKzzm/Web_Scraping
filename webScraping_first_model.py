import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("section", class_="job_list")

python_jobs = soup.find_all(
  "h1", string = lambda text: "python" in text.lower()
)

python_job_elements = [
   h1_element.parent for h1_element in python_jobs
]

for python_jobs in python_job_elements:
  title_element = python_jobs.find("h1")
  location_element = python_jobs.find("span")
  date_element = python_jobs.find_all("span")[1]
  contractType_element = python_jobs.find_all("span")[2]
  company_element = python_jobs.find_all("span")[3]
  print(title_element.text.strip())
  print(location_element.text.strip())
  print(date_element.text.strip())
  print(contractType_element.text.strip())
  print(company_element.text.strip())
  print()
