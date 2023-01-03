import urllib.request
import logging
from Logging_setup import log_setup

if __name__ == "__main__":
    logs = log_setup("URL_log.txt")

    logger=logging.getLogger('Download')
def download_file(url,path):
    test=url
    loc=path
    if test.endswith('.txt'):
        try:
            urllib.request.urlretrieve(url, loc + 'Macbeth.txt')  # proceed with download
        except :
            logger.error('Please check the provided url and path.')
    else:
        print('Please enter an URL leading to a .txt file')
        logger.info('Wrong file extension.')


download_file('https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt',
              'C:/Users/Tobia/Desktop/Archiv/Programmieren/')

