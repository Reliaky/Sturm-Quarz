import urllib.request

Link=input('Please provide a URL to look at')
try:
    with urllib.request.urlopen(Link) as Tagesschau:
        Text=Tagesschau.read(600)
except:
    print('Please provide a valid input')

print(Text)
