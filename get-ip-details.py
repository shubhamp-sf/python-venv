import requests
from tabulate import tabulate

def get_ip_info():
    url = "https://ip.shubhamp.dev"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def format_ip_info(ip_info):
    if ip_info is None:
        return [["Error", "Failed to retrieve IP information"]]
    
    return [[key, value] for key, value in ip_info.items()]

def main():
    ip_info = get_ip_info()
    formatted_info = format_ip_info(ip_info)
    
    print(tabulate(formatted_info, headers=["Field", "Value"], tablefmt="grid"))

if __name__ == "__main__":
    main()