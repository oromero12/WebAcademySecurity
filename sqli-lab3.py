import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit_sqli(url,payload):
      print("Hi")

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[1].strip()
    except IndexError:
        print("error ingresando información")


    if  exploit_sqli(url,payload):
        print('[+] SQL injection successful!!')
    else:
        print('[-] SQL injection unsuccessful!')

