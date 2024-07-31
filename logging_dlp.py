import logging  #https://realpython.com/python-logging/

def dlp_log(sensitive_data):
    logging.basicConfig(filename='Tushar\Data_Loss_Prevention\sample_log.txt', level=logging.INFO)
    if sensitive_data:
        for labels, obj in sensitive_data.items():
            logging.info(f"Sensitive data detected - {labels}: {obj}")
