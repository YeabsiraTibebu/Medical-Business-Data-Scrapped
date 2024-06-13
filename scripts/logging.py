import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
def main() -> None:
    
   
    logging.basicConfig(filename='scraper.log',
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
    
    )
    
     
    
    def get_file_handler(self) -> logging.FileHandler :
        # create logs folder if it doesn't exist
        Path("../logs").mkdir(parents=True, exist_ok=True)
        file_handler = TimedRotatingFileHandler(f"../logs/app.log", when='d')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(App_Logger.log_formatter)
        return file_handler
    
  