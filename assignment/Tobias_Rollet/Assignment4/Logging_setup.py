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

