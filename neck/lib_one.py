# -*- coding: utf-8 -*-

"""
Grab-bag of utility functions for:

Controlling time values between serializable (show) format and internal (calc)
format.

Manage data in standard files:

    email_confirm.json - holds reserved email address during confirmation
    id_email.idx - index keyed by email address with account # value
    inbox.idx - index keyed by inbox code with account # value
    userDB.json - full user record
    inbox.log - log entry of every BMlet inbox request (mm and user)
    inbox.txt - inbox log entries to add to Inbox.mkm

Utility functions to retrieve user directory names


"""
import datetime
import json
import os

def show_now():
    """
    :return: Human-readable representation of datetime.datetime.now()

    This is the data format stored in files and databases.  Equivalent
    to show_time(datetime.datetime.now())
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

def show_time(calctime):
    """
    :param calctime: Time value in datetime.datetime format
    :return: Time value in .strftime('%Y-%m-%d %H:%M:%S.%f') format

    Inverse function of calc_time(showtime)
    """
    return calctime.strftime('%Y-%m-%d %H:%M:%S.%f')

def calc_now():
    """
    :return: datetime.datetime.now()
    """
    return datetime.datetime.now()

def calc_time(showtime):
    """
    :param showtime: Time value in .strftime('%Y-%m-%d %H:%M:%S.%f') format
    :return: calc_time in datetime.datetime format

    Inverse function of show_time(calctime)
    """
    return datetime.datetime.strptime(showtime, '%Y-%m-%d %H:%M:%S.%f')

def json_add_keyed_record(fname, index, record):
    """
    :param fname: NAME of the file to be updated
    :param index: KEY value of the new record
    :param record: VALUE associated with the INDEX
    :return: record parameter or None
    """
    if index is None:
        return None
    try:
        with open(fname, 'w+') as add_file:
            json_dict = json.loads(add_file.read())
            json_dict[index] = record
            add_file.write(json.dumps(json_dict))
            return record
    except:
        return None

def json_get_with_index(fname, index):
    """
    :param fname: NAME of file to open
    :param index: INDEX (value) to access
    :return: value associated with the INDEX or None

    Assumes that file is stored in JSON format

    """
    if index is None:
        return None
    try:
        with open(fname, 'r') as retrieve_file:
            json_dict = json.loads(retrieve_file.read())
            if index not in json_dict:
                return None
            return json_dict[index]
    except:
        return None

def json_update_keyed_record(fname, index, record):
    """
    :param fname: NAME of file to be updated
    :param index: KEY value of the record to update
    :param record: VALUE associated with the index
    :return: record parameter or None
    """
    if index is None:
        return None
    try:
        with open(fname, 'w+') as update_file:
            json_dict = json.loads(update_file.read())
            if index not in json_dict:
                return None
            json_dict[index] = record
            update_file.write(json.dumps(json_dict))
            return record
    except:
        return None

def append_record(fname, record):
    """
    :param fname: NAME of file to be updated
    :param record: CONTENTS to be appended to file
    :return: record parameter or None
    """
    if fname is None:
        return None
    try:
        with open(fname, 'a+') as append_file:
            append_file.write(record)
            return record
    except:
        return None

def get_raw_contents(fname):
    """
    :param fname: NAME of file to read
    :return: complete contents of file
    """
    try:
        with open(fname, 'r') as read_file:
            return read_file.read()
    except:
        return None

def user_directory(userID):
    """
    :param userID: identifies the name of the user directory
    :return: full path to the base user directory
    """
    from . import ms_app
    return os.path.join(ms_app.config['MM_BASE_DIRECTORY'] + '/Accounts/' + userID)

def user_mark_directory(userID):
    """
    :param userID: identifies the name of the user directory
    :return: full path to MarkSet directory
    """
    return os.path.join(user_directory(userID) + '/mark/')

def user_log_directory(userID):
    """
    :param userID: identifies the name of the user directory
    :return: full path to user-logs directory
    """
    return os.path.join(user_directory(userID) + '/logs/')

def user_backup_directory(userID):
    """
    :param userID: identifies the name of the user directory
    :return: full path to user-logs directory
    """
    return os.path.join(user_mark_directory(userID) + '/backups/')




