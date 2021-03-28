import requests
import re 

url=input("Enter Url [ex: example.com]: ")
def getSubDomain(url):
    url=url.replace("www.","").replace("https://","").replace("http://","")
    pattern = "[\w]{1,256}\.[a-zA-Z0-9()]{1,6}"
    _l = re.compile(pattern)
    if _l.match(url):
        response = requests.get(f"https://sonar.omnisint.io/subdomains/{url}").text
        urls = response.split("\n")
        for u in set(urls):
            if u=="" or len(u)<=3:
                pass
            print("[+] ",u.replace("\"","").replace("'","").replace(",","").replace("    ",""))

getSubDomain(url)