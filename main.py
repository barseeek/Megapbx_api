import requests
import os
from dotenv import load_dotenv

def main():
    token = os.environ["MEGAPBX_TOKEN"]
    header = {
        'X-API-KEY' : token
}
    domain = "vats730382.megapbx.ru"    
    load_dotenv()
    current_number = input('Input ext number\n').strip()
    while not(current_number.isdigit()):
        current_number = input('Input ext number\n')
    users = get_users(header, domain)
    print(is_number_free(users,current_number))


def get_users(header, domain):
    params = {
        'search': '',
        'start' : 0,
        'limit' : 200
    }
    response = requests.get(f"https://{domain}/crmapi/v1/users", headers=header, params=params)
    response.raise_for_status()
    return response.json()['items']


def is_number_free(employees, number):
    for employee in employees:
        if employee['ext'] == number:
            return False
    return True

def get_telnums(header, domain):
    params = {
        'search': '',
        'start' : 101,
        'limit' : 99
    }
    response = requests.get(f"https://{domain}/crmapi/v1/telnums", headers=header, params=params)
    return response.json()

if __name__=='__main__':
    main()