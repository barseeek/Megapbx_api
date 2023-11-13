import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    megapbx_token = os.environ["MEGAPBX_TOKEN"]
    header = {
        'X-API-KEY': megapbx_token
    }
    domain = "vats730382.megapbx.ru"
    users = get_users(header, domain)
    free_numbers = get_free_numbers(users)
    print(free_numbers)


def get_users(header, domain):
    params = {
        'search': '',
        'start': 0,
        'limit': 200
    }
    response = requests.get(f"https://{domain}/crmapi/v1/users",
                            headers=header,
                            params=params)
    response.raise_for_status()
    return response.json()['items']


def is_number_free(employees, number):
    for employee in employees:
        if employee['ext'] == str(number):
            return False
    return True


def get_free_numbers(users):
    free_numbers = []
    for number in range(105, 500):
        if is_number_free(users, number):
            free_numbers.append(number)
    return free_numbers


def get_telnums(header, domain):
    params = {
        'search': '',
        'start': 101,
        'limit': 99
    }
    response = requests.get(f"https://{domain}/crmapi/v1/telnums",
                            headers=header,
                            params=params)
    return response.json()


if __name__ == '__main__':
    main()
