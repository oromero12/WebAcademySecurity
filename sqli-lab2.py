import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli(s, url, payload):
    True    

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("Error ingresando parametros: ingresar url y payload")

    s = requests.Session()

    if exploit_sqli(s, url, payload):
        print("+ injection succesfull")
    else:
        print("- injection unsuccesfull")


    

