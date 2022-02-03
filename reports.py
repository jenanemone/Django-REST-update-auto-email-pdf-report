#!/usr/bin/env python3

"""From google IT Automation with Python Course 6 lab 4
reports.py will generate a report for the 'client' to detail
our successful changes and posts to their site through the Django framework.

Processed Update on <Today's date>

[blank line]

name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]
"""

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, file_title, fruits_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  empty_line = Spacer(1,20)
  report_title = Paragraph(file_title, styles['h1'])
  report_info = Paragraph(fruits_data,styles["BodyText"])
  report.build([report_title, empty_line, report_info])

