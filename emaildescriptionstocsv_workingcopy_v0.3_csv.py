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
# To Do: Put attachmentsupport  in CSV - do a for loop and 2d array
#       Open more levels of directories - Nest those for loops? test for depth?
#       implement 2d arrays
#       
#
# Note: Currently the script functions by opening only the first level of directories in the file, !Current functionality only prints email details not csv file!
# The data will be stored in a general named emaildescriptions.csv file that records the following fields:
# Folder/Directory of Email, Name of Email, FileType of Email, Size of Email in KB, From, To, CC, BCC, Subject, Date, Contents, Attachments,
# and attachment data including attachment name

import sys
import os, os.path
import optparse
import locale
import csv
import time
message=[]
subject = []
dirlist = []
subjectlist= []
namelist= []
typelist= []
sizelist= []
fromlist= []
tolist= []
cclist= []
bcclist= []
textcontentlist = []
htmlcontentlist = []
datelist = []
date2list = []
attachmentdetails = []
attachmentdata = []

try:
    import pyzmail
except ImportError:
    if os.path.isdir('../pyzmail'):
        sys.path.append(os.path.abspath('..'))
    elif os.path.isdir('pyzmail'):
        sys.path.append(os.path.abspath('.'))
    import pyzmail
i = '' # buffer for adding ints to print
number = 0
#function for printing email to csv
def printemail(num1,directory,name,filetype,size,fullname): #print all the email stats
    #print('directory' + directory + ' filename:' + name + '\n filetype:' + filetype + '\n filesize:' + i, size, i + 'kb',)
    msg= pyzmail.PyzMessage.factory(open(fullname, 'rb'))
    """print ('Subject: %r' % (msg.get_subject(), ))
    print ('From: %r' % (msg.get_address('from'), ))
    print ('To: %r' % (msg.get_addresses('to'), ))
    print ('Cc: %r' % (msg.get_addresses('cc'), ))
    print ('BCc: %r' % (msg.get_addresses('bcc'), ))
    print ('body and details:')"""
    for mailpart in msg.mailparts:
        payloader = [directory, name, mailpart.filename,mailpart.sanitized_filename, mailpart.type, mailpart.charset, mailpart.part.get('Content-Description'), len(mailpart.get_payload())]
        attachmentdata.append(payloader)
        
        
    dirlist.append(directory)
    subjectlist.append(msg.get_subject())
    namelist.append(name)
    typelist.append(filetype)
    sizelist.append(size)
    fromlist.append(msg.get_address('from'))
    tolist.append(msg.get_addresses('to'))
    cclist.append(msg.get_addresses('cc'))
    bcclist.append(msg.get_addresses('bcc'))
    datelist.append(msg.get_decoded_header('date'))


    
   # attachentslist
    """
    attachment1namelist
    attachment1typelist
    attachment1partlist
    attachment1sizelist
    attachment1contentlist.append
 """

# and attachment data including attachment name
     
for dirs in os.listdir(): #open all directories scriptis in
    dname, d_extension = os.path.splitext(dirs) #parse filenames to check if they are dirs
    if d_extension == '': # if they are dirs
        for filename in os.listdir(dirs): # for every email print its stats
            fname, file_extension = os.path.splitext(filename)
            fullfilename = dirs + "/" + filename
            if file_extension =='.eml':
                printemail(number,dirs,fname,file_extension,(os.stat(fullfilename).st_size/1000),fullfilename) #the function that will print those stats



with open('emails.csv', 'w',encoding='utf-16') as csvfile:
        fieldnames = [ 'Directory Name', 'filename','filetype','filesize','Subject', 'to','From','cc','bcc','date1']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in subjectlist:
                writer.writerow({'Directory Name' : dirlist[number], 'filename': namelist[number], 'filetype':typelist[number],'filesize' : sizelist[number],
                                 'Subject': subjectlist[number], 'to' : tolist[number], 'From' : fromlist[number], 'cc' : cclist[number], 'date1' : datelist[number] })
                number = number + 1
        writer.writerow({ 'Directory Name' : 'Attachments'})
        writer.writerow({'Directory Name' : 'directory', 'filename': "Email Name", 'filetype': "Attachment Name",'filesize' : "Attachment Name 2",
                                 'Subject': "Attachment Type", 'to' : "Character set", 'From' : "Contents" , 'cc' : "Size" })
        for i in attachmentdata:
            writer.writerow({'Directory Name' : i[0], 'filename': i[1], 'filetype': i[2],'filesize' : i[3],
                                 'Subject': i[4], 'to' : i[5], 'From' : i[6] , 'cc' : i[7] })



