import requests
txt = input("Enter something ")
url = 'http://text-processing.com/api/sentiment/'
myobj = {'text': txt}
response = requests.post(url, data = myobj)
print(response.json())