import os
import alert_dlp
import logging_dlp
import Regex_patterns

def file_check(file_path):
    if not os.path.exists(file_path):
        return "File does not exist."

    with open(file_path, 'r') as file:
        data = file.read()

    sensitive_data_found = Regex_patterns.sensitive_data_check(data)
    return sensitive_data_found

def main(file_path):
    sensitive_data = file_check(file_path)
    alert_dlp.alert_dlp_check(sensitive_data)
    logging_dlp.dlp_log(sensitive_data)

if __name__ == "__main__":
    file_path = 'Tushar\Data_Loss_Prevention\sample_data.txt'  # Path to the file
    main(file_path)