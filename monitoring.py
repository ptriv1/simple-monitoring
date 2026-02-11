import urllib.request
import hashlib

def fetch(url):
   with urllib.request.urlopen(url) as response:
        return response.read()
   
def compute_hash(contents):
    return hashlib.sha256(contents).hexdigest()

url = input("Enter a URL to check: ")

contents = fetch(url)
print("Content length:", len(contents))

print(compute_hash(contents))