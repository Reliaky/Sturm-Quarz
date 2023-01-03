import urllib.request
def Link_analyser(Link):
    try:
        with urllib.request.urlopen(Link) as file:
            print(file.read(600))
    except:
        print('Please provide a valid input')


Link_analyser('https://www.wetterstation-goettingen.de/analysen/noaa/112022.txt')