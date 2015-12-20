#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import sys
import ConfigParser
import ZLWebSign

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0] + os.sep
RUNNING_PATH = sys.path[0] + os.sep


def read_users(filename):
    result = list()
    if os.path.isfile(filename):
        conf = ConfigParser.ConfigParser()
        conf.read(filename)
        for session in conf.sections():
            url = conf.get(session, 'url')
            usr = conf.get(session, 'usr')
            pwd = conf.get(session, 'pwd')
            result.append((url, usr, pwd))
    return result

if __name__ == '__main__':
    config_filename = RUNNING_PATH + 'UserSetting.conf'
    user_data = read_users(config_filename)
    web_sign = ZLWebSign.ZLWebSign()
    for url, username, password in user_data:
        web_sign.start(url, username, password)
