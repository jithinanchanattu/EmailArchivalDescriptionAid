# EmailArchivalDescriptionAid
# Project Description: This python script reads all .eml emails in a directory and creates a .csv file that contains information about the .eml files for easy archival description
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
# Note: Currently the script functions by opening only the first level of directories in the file, 
# !Current functionality only prints email details not csv file!
# The data will be stored in a general named emaildescriptions.csv file that records the following fields:
# Folder/Directory of Email, Name of Email, FileType of Email, Size of Email in KB, From, To, CC, BCC, Subject, Date, Contents, Attachments,
# and attachment data including attachment name
