import requests

payload = {'key': 'value'}
r = requests.post('https://httpbin.org/post', json=payload)


response = requests.get('https://api.github.com')
print(response.status_code)
input("Press Enter to continue...")
print(response.json())
input("Press Enter to continue...")
print(response.headers)
input("Press Enter to continue...")
print(response.text)


