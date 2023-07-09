from google.oauth2 import service_account
from bs4 import BeautifulSoup
import gspread
import requests
import random


# Access the JSON key file downloaded from Google service_account.
# Alternatively, define a function that returns the JSON key value.
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
credentials = service_account.Credentials.from_service_account_file(
    "secret_key.json",
    scopes=SCOPES
)


# Scrape data from websites.
class GetData:
    @staticmethod
    def departments(url, headers):
        page = requests.get(url, headers=headers)
        page.raise_for_status()
        soup = BeautifulSoup(page.text, "html.parser")
        elements = soup.find_all(id="post-5527")

        # Locally save the records.
        # file = open(file_name, "w+")
        department_list = []
        for get_h2 in elements:
            h2 = get_h2.find_all("h2")
            h2_list = h2[0:10]
            for get_strong in h2_list:
                strong = get_strong.find_all("strong")
                department_name = strong[0].text.strip()
                department_list.append(department_name)
                # Save records in .txt file.
                # for department in departments:
                #   file.write(record + "\n")
        return department_list

    @staticmethod
    def names(url, code):
        page = requests.get(url)
        page.raise_for_status()
        soup = BeautifulSoup(page.text, "html.parser")
        elements = soup.find_all("tbody")

        name_list = []
        for get_tr in elements:
            tr = get_tr.find_all("tr")
            if code == "last-name":
                # Use 300 last names for both male and female name.
                tr_slice = tr[1:301]
            else:
                tr_slice = tr[1:151]
            for row in tr_slice:
                td = row.find_all("td")
                name = td[1].text.capitalize()  # get second <td> element
                name_list.append([name])
        return name_list


# Pass the file_name argument to create a local .txt file.
# file_name = "departments.txt"

# Use headers to avoid 403: Forbidden Error.
web_headers = {'User-Agent': 'Mozilla/5.0'}
web_url = "https://www.presentationskills.me/" \
      "departments-in-an-organization-and-their-functions/"
GD_departments = GetData.departments(web_url, web_headers)

web_url = "https://namecensus.com/last-names/"
web_code = "last-name"
GD_last_names = GetData.names(web_url, web_code)

web_url = "https://namecensus.com/first-names/common-male-first-names/"
web_code = "male-name"
GD_male_names = GetData.names(web_url, web_code)

web_url = "https://namecensus.com/first-names/common-female-first-names/"
web_code = "female-name"
GD_female_names = GetData.names(web_url, web_code)


class RandomGenerator:
    # Pick a random department from GD_departments to fill out 300 rows.
    @staticmethod
    def department_list():
        i = 0
        department_list = []
        while i < 300:
            choice = random.choice(GD_departments)
            department_list.append([choice])
            i += 1
        return department_list

    # Combine and randomize GD_female_names
    # and GD_male_names to fill out 300 rows.
    @staticmethod
    def first_name_list():
        first_name_list = GD_male_names + GD_female_names
        random.shuffle(first_name_list)
        return first_name_list

    @staticmethod
    def last_name_list():
        random.shuffle(GD_last_names)
        last_name_list = GD_last_names
        return last_name_list

    @staticmethod
    def subscriber_name_list():
        first_name_list = RandomGenerator.first_name_list()
        last_name_list = RandomGenerator.last_name_list()
        subscriber_name_list = []
        for first_name_index, last_name_index in zip(first_name_list, last_name_list):
            for first_name, last_name in zip(first_name_index, last_name_index):
                full_name = first_name + ' ' + last_name
                subscriber_name_list.append([full_name])
        return subscriber_name_list[1:101]


# Authenticate the JSON key with gspread and access the worksheet.
file = gspread.authorize(credentials)

# Insert 300 employee names to Employee Feedback worksheet.
gsheet_file = file.open("Employee Feedback")
sheet = gsheet_file.worksheet("Employee List")
sheet.batch_clear(['A2:C'])
sheet.update('A2:A', RandomGenerator.first_name_list())
sheet.update('B2:B', RandomGenerator.last_name_list())
sheet.update('C2:C', RandomGenerator.department_list())

# Insert 200 subscriber names to Subscriber Status worksheet.
subscriber_gsheet_file = file.open("Subscriber Status")
subscriber_sheet = subscriber_gsheet_file.worksheet("Main")
subscriber_sheet.batch_clear(['A2:A'])
subscriber_sheet.update('A2:A', RandomGenerator.subscriber_name_list())
