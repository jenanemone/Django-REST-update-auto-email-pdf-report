#!/usr/bin/env python3

"""From Google IT Automation with Python Course 6 Lab 4

Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

Subject line

CPU usage is over 80% | Error - CPU usage is over 80%

Available disk space is lower than 20% | Error - Available disk space is less than 20%

available memory is less than 500MB | Error - Available memory is less than 500MB

hostname "localhost" cannot be resolved to "127.0.0.1" | Error - localhost cannot be resolved to 127.0.0.1

E-mail Body: Please check your system and resolve the issue as soon as possible.
"""

import shutil
import psutil
import socket
import report_email

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free_space = du.free / du.total * 100
    return free_space < 20

def check_memory():
    available_mem = psutil.virtual_memory().available
    available_MB = available_mem / 1024 * 1024
    return available_MB > 500

def check_hostname():
    local_ip = socket.gethostname('localhost')
    return local_ip == "127.0.0.1"

if not check_cpu_usage():
    report_email.send_trouble_email("Error - CPU usage is over 80%")

if not check_disk_usage("/"):
    report_email.send_trouble_email("Error - Available disk space is less than 20%")

if not check_memory():
    report_email.send_trouble_email("Error - Available memory is less than 500MB")

if not check_hostname():
    report_email.send_trouble_email("Error - localhost cannot be resolved to 127.0.0.1")