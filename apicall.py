import requests

# query = {'lat':'45', 'lon':'180'}
# response = requests.get("http://api.open-notify.org/iss-pass.json",params=query)
# print (response.json())

# response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# print(response.headers["date"]) 


#countries name and capital
# base_url = 'https://restcountries.eu/rest/v2/all'
# resp = requests.get(base_url)

# data = resp.json()
# # print(type(data))

# for key in data:
#     print(key['name'], key['capital'])


#swapi calling
base_url = 'https://swapi.dev/api/people/1/'
resp = requests.get(base_url)

data = resp.json()
# print(type(data))

for key in data:
    print(key)