import logging
import urllib.request

logger= logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format= logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler= logging.FileHandler('URL.log')
file_handler.setFormatter(format)


stream_handler= logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)



Link=input('Please provide a URL to look at')
try:
    with urllib.request.urlopen(Link) as Tagesschau:
        logger.error(Tagesschau.read(600))
except:
    print('Please provide a valid input')

logging.shutdown()
