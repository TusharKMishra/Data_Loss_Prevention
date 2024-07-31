def alert_dlp_check(sensitive_data_found):
    if sensitive_data_found:
        for labels, obj in sensitive_data_found.items():
            print(f"Alert: Sensitive data detected - {labels}: {obj}")
    else:
        print("No sensitive data detected in the file.")
