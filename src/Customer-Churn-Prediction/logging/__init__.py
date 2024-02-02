import os 
import sys 
import logging

logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s]"#This will format the logs
log_dir = "Logs"#This will create the directory for the logs
log_filepath = os.path.join(log_dir,"logfile.log")#This will create the path for the log file
os.makedirs(log_dir,exist_ok=True)#This will create the directory if it does not exist

logging.basicConfig(
    level = logging.INFO,#This will set the level of the logs
    format = logging_str,#This will format the logs
    handlers = [
        logging.FileHandler(log_filepath),#This will save the logs to a file
        logging.StreamHandler(sys.stdout) #This will print the logs to the console
    ]
)

logger = logging.getLogger("Customer-Churn-Logger")
