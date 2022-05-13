import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2", string = lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for python_jobs in python_job_elements:
    title_element = python_jobs.find("h2", class_="title")
    company_element = python_jobs.find("h3", class_="company")
    location_element = python_jobs.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

    link_url = python_jobs.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
