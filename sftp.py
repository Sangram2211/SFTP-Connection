#Packages and libraries
import pysftp
import csv
# Creds
myHostname = "000.000.000.000"
myport = 0000
myUsername = "admin"
myPassword = "admin"

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


##================================ File Upload using SFTP ===============================##

with pysftp.Connection(host=myHostname, port=myport, username=myUsername, password=myPassword, private_key=".ppk", cnopts=cnopts) as sftp:
    directory_structure = sftp.listdir_attr()
    
    #Define Local path
    localFilePath = '/root/myproject/myfile.csv'

    # Define the remote path where the file will be uploaded
    remoteFilePath = './root/remotepath/addyourfilehere'

    sftp.put(localFilePath, remoteFilePath)





##=================== File Fetch from SFTP to local or in project =======================##

with pysftp.Connection(host=myHostname, port=myport, username=myUsername, password=myPassword, private_key=".ppk", cnopts=cnopts) as sftp:
    directory_structure = sftp.listdir_attr("root/")
    myFileList = sftp.listdir("root/")
    for first in directory_structure:
        file_data = first.filename
        if file_data.startswith('myfile'):
            sftp.get('root/'+first.filename)
            # Open file and choose mode Read
            with open(first.filename, mode ='r')as file:
                #reading the CSV file
                csvFile = csv.reader(file)
                for lines in csvFile:
                    if lines[0] != 'Sr. No.':
                        print(lines['Sr. No.'])