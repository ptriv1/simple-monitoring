import urllib.request
import hashlib

def fetch(url):
   with urllib.request.urlopen(url) as response:
        return response.read()
   
def compute_hash(contents):
    return hashlib.sha256(contents).hexdigest()

def load_previous_hash(filename):
    try:
        with open(filename, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None
    
def save_hash(filename, hash_value):
    with open(filename, "w") as f:
        f.write(hash_value)

url = input("Enter a URL to check: ")

contents = fetch(url)
print("Content length:", len(contents))

current_hash = compute_hash(contents)

previous_hash = load_previous_hash("hash.txt")

if previous_hash is None:
    print("First run. Saving hash.")
elif current_hash != previous_hash:
    print("Change detected!")
else:
    print("No change.")

save_hash("hash.txt", current_hash)