import sys
import argparse
import datetime as dt
from datetime import datetime
import csv
import logging as log

LOG_FILE_COLUMNS = ['cookie', 'timestamp']

def get_parser_args():
    '''

    :return: Return arguments from the command line parser
    '''
    parser = argparse.ArgumentParser(description='Most Active Cookie - Quantcast Coding Challenge')

    # Command Line Argument Parser
    parser.add_argument('-l', '--logfile', type=str, required=True, help='Cookie Log File')
    parser.add_argument('-d', '--date', type=str, required=True, help='Cookie Log Date')

    arguments = parser.parse_args()
    return arguments

def preprocess_log_file(log_file, date_string):
    '''

    :param log_file:
    :param date_string:
    :return: headers, log_data
    Check if the log file has correct format and return the log
    names of specified date
    '''
    try:
        log_date = dt.datetime.fromisoformat(date_string)
        with open(log_file, 'r') as file:
            reader = list(csv.reader(file))
            headers = reader.pop(0)
            if headers != LOG_FILE_COLUMNS:
                e = "[ERROR] : Wrong Header names in CSV"
                log.error(e)
                raise Exception(e)

            log_data = []
            for row in reader:
                cookie = row[0]
                timestamp = dt.datetime.fromisoformat(row[1])

                if(log_date.date() == timestamp.date()):
                    log_data.append((cookie))

            return headers, log_data

    except FileNotFoundError:
        log.error("[ERROR] : Please enter the correct file")
        raise FileNotFoundError
    except ValueError:
        log.error("[ERROR]: Format Error")
        raise ValueError


def get_active_cookie(column_name, data):
    '''

    :param column_name:
    :param data:
    :return: list of active cookies
    '''
    cookie_dict = {}
    for cookie in data:
        cookie_dict[cookie] = cookie_dict.get(cookie,0) + 1

    max_value = max(cookie_dict.values())
    return [c for c in set(cookie_dict) if cookie_dict[c] == max_value]

if __name__ == '__main__':
    args = get_parser_args()

    date = args.date
    file = args.logfile

    #preprocess file
    headers, log_data = preprocess_log_file(file,date)


    # Get most active cookie
    if len(log_data) > 0:
        result = get_active_cookie(headers, log_data)

        # print Most active cookies
        print("\n".join(result))
    else:
        print("No Logs")
        log.info("No Logs")










