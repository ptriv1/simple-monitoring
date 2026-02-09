import urllib.request

def fetch(url):
    response = urllib.request.urlopen(url)
    contents = response.read()
    return contents

contents = fetch(url)
print(len(contents))