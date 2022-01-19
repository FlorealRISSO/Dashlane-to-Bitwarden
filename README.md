## Dashlane-to-Bitwarden
# A simple script useful to switch from Dashlane to Bitwarden by converting the password file to the right format.
When I wanted to change my password manager, I noticed that each software had its own data format, so I wrote this little python script to convert Dashlane password files into Bitwarden format.

# How to get your password
Go to the [Dashlane](https://www.dashlane.com/)  website, connect you, and click on **My Account**, Export the data and choose **CSV**.
Then, unarchived the file downloaded and run the python script on the file named "./credentials.csv". 


> Usage : Python3 csvConvertor.py
> Enterthe path of the source _.csv (./credentials.csv by default) 
> $ ./credentials.csv
> Enterthe path of the destination _.csv (./bitwarden.csv by default)
> $ ./bitwarden.csv

Then go to the [Bitwarden](bitwarden.com) website, Tools, Importing data, Select BITWARDEN (CSV), and upload the csv file made by the script.

