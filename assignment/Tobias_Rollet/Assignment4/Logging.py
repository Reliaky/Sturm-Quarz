import logging
import urllib.request

class log_setup:
    log_file=None

    def __init__(self, log_file):
        self.log_file= log_file
        self.loggingconfig(log_file)
        
    def loggingconfig(self,log_file):
        logging.basicConfig(level= logging.ERROR, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                    datefmt='%m-%d %H:%M',
                                    filename=log_file,
                                    filemode='w')

        #set handlers
        stream_handler= logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        #set formatters
        format= logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(format)


        #add handlers
        logging.getLogger('').addHandler(stream_handler)



logs= Log_setup('URL_log.txt')
logger1 = logging.getLogger('URL_Reader')

Link=input('Please provide a URL to look at')
try:
    with urllib.request.urlopen(Link) as Tagesschau:
        print(Tagesschau.read(600)

except:
    logger1.error('The input is either not a URL or flawed.')
    print('Please provide a valid input')


logging.shutdown()
