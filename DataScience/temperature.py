import requests
city="Ulhasnagar"
url="https://geocoding-api.open-meteo.com/v1/search"
parameters={"name":city,"language":"en","format":"json"}
response=requests.get(url,params=parameters)
mydata=response. json()
latitude=mydata["results"] [0] ["latitude"]
longitude=mydata["results"][0] ["longitude"]
country=mydata["results"][0] ["country"]
print(latitude)