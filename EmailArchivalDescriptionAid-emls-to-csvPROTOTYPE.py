#!/bin/env python
#
#  Heavily borrowed from pyzmail/pyzinfomail (c) Alain Spineux <alain.spineux@gmail.com>
#  and Pyzmail library http://www.magiksys.net/pyzmail/
#
# Developed by Domenic Rosati with the aid of Andrea Kampen for Dalhousie University Archives
# GPL license 
#
# Application of Script: Script will read and display email info for all emails that are located in the proceeding direcories that this script is run in
# The script is intended to help archivists in archival description of large swaths of email by placing email data and contents in csv file
#
# To Do: Put all details in CSV
#       Open more levels of directories - Nest those for loops? test for depth?
#
#
#
# Note: Currently the script functions by opening only the first level of directories in the file, !Current functionality only prints email details not csv file!
# The data will be stored in a general named emaildescriptions.csv file that records the following fields:
# Folder/Directory of Email, Name of Email, FileType of Email, Size of Email in KB, From, To, CC, BCC, Subject, Date, Contents, Attachments,
# and attachment data including attachment name



import sys
import os
import optparse
import locale
import csv

try:
    import pyzmail
except ImportError:
    if os.path.isdir('../pyzmail'):
        sys.path.append(os.path.abspath('..'))
    elif os.path.isdir('pyzmail'):
        sys.path.append(os.path.abspath('.'))
    import pyzmail
i = '' # buffer for adding ints to print
#function
def printemail(directory,name,filetype,size,fullname): #print all the email stats
    print('directory' + directory + ' filename:' + name + '\n filetype:' + filetype + '\n filesize:' + i, size, i + 'kb',)
    msg= pyzmail.PyzMessage.factory(open(fullname, 'rb'))
    print ('Subject: %r' % (msg.get_subject(), ))
    print ('From: %r' % (msg.get_address('from'), ))
    print ('To: %r' % (msg.get_addresses('to'), ))
    print ('Cc: %r' % (msg.get_addresses('cc'), ))
    print ('BCc: %r' % (msg.get_addresses('bcc'), ))
    print ('body and details:')
    for mailpart in msg.mailparts:
        print (
            mailpart.filename,  
            mailpart.sanitized_filename, 
            mailpart.type, 
            mailpart.charset, 
            mailpart.part.get('Content-Description'), 
            len(mailpart.get_payload()) )
        if mailpart.type.startswith('text/'):
            # display first line of the text
            payload, used_charset=pyzmail.decode_text(mailpart.get_payload(), mailpart.charset, None)
            print ( payload.split('\\n')[0])
     
for dirs in os.listdir(): #open all directories scriptis in
    dname, d_extension = os.path.splitext(dirs) #parse filenames to check if they are dirs
    if d_extension == '': # if they are dirs
        for filename in os.listdir(dirs): # for every email print its stats
            fname, file_extension = os.path.splitext(filename)
            if file_extension =='.eml':
                printemail(dirs,fname,file_extension,(os.stat(filename).st_size/1000),filename) #the function that will print those stats
              

"""# CSV Module
message = [msg.get_subject(), msg.get_addresses('to'),
 msg.get_address('from'),
msg.get_addresses('cc'),
 msg.get_addresses('bcc'), msg.text_part.get_payload() ]

with open('emails.csv', 'w') as csvfile:
    fieldnames = [ 'Subject', 'to','From','cc','bcc','contents']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({ 'Subject': message[0], 'to' : message[1], 'From': message[2], 'cc' : message[3], 'bcc' : message[4], 'contents' : message [5] })
    writer.writerow({ 'Subject': message[0], 'to' : message[1], 'From': message[2], 'cc' : message[3], 'bcc' : message[4], 'contents' : message [5] })

