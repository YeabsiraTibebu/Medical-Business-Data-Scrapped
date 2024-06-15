import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHand
class App_Logger:
    logging.basicConfig(filename='../log/scraper.log',
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
    
    )
    
     
    

    
  