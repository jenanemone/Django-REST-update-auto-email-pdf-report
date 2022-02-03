#!/usr/bin/env python3

"""From Google IT Automation with Python course 6 lab 4
report_email calls generates a report using reports.py
and sends the report via email to the 'client'."""

import email.message
import mimetypes
import os
import emails
import reports
import datetime

def make_pdf(files):
  string_for_pdf = ""
  for file in files:
    with open(source_dir + file,"r") as f:
      info = f.readlines()
      fruit_name = info[0].strip()
      fruit_weight = info[1].strip()
      string_for_pdf += "name" + fruit_name + "<br/>" + "weight" +  fruit_weight + "<br/><br/>"
  return string_for_pdf

if __name__ == "__main__":
  date = datetime.date.today()
  report_date = date.strftime("%B %-d, %Y")
  sender = "automation@example.com"
  receiver = "student-03-444c626601e1@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email." 
  source_dir = "supplier-data/descriptions/"
  files_to_process = os.listdir(source_dir)
  attachment = "/tmp/processed.pdf"
  reports.generate_report(attachment, "Processed update on " + report_date, make_pdf(files_to_process))
  report_message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(report_message)

