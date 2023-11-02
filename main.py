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
    #print(get_users(header, domain))
    tel_nums = get_telnums(header, domain)
    print(tel_nums['info'])


def get_users(header, domain):
    response = requests.get(f"https://{domain}/crmapi/v1/users", headers=header)
    response.raise_for_status()
    return response.json()


def get_telnums(header, domain):
    params = {
        'search': '',
        'start' : 10,
        'limit' : 100
    }
    response = requests.get(f"https://{domain}/crmapi/v1/telnums", headers=header)
    print(response.url)
    response.raise_for_status()
    print(response.content)
    return response.json()

if __name__=='__main__':
    main()