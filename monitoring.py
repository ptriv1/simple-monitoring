import urllib.request
import hashlib

def fetch(url):
   with urllib.request.urlopen(url) as response:
        return response.read()

url = input("Enter a URL to check: ")

contents = fetch(url)
print("Content length:", len(contents))

hash_value = hashlib.sha256(contents).hexdigest()
print("Hash:", hash_value)