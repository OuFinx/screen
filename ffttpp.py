import os
from ftplib import FTP
# -----------------------------
directory = '/'
files = os.listdir(directory)
# -----------------------------
filesFTP = []
ftp = FTP('***')
ftp.login("***", "***")
ftp.cwd('sites/***/image/photos/1/')
ftp.retrlines("NLST", filesFTP.append)
# -----------------------------
ftp_list = set(filesFTP)
pc_list = set(files)
c_list = pc_list.difference(ftp_list)
# -----------------------------
for file_name in c_list:
    local_filename = os.path.join(directory, file_name)
    ftp.retrbinary("STOR " + file_name, open(local_filename, 'r').write)
