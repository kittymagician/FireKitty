# FireKitty ![FireKitty](https://github.com/kittymagician/FireKitty/blob/master/img/firekitty.png)
Digital Artefact Extractor for Discord

Developed as part of my B.Sc. (Hons.) Dissertation entitled "Retrieval of Digital Artefacts from TeamSpeak and Discord: A Forensic Investigation and Analysis of the Malicious Use of Gaming Communication Clients"

In citing the use of this tool in any future publications please use the correct citiation "Bryant, O. (2018). Retrieval of Digital Artefacts from TeamSpeak and Discord: A Forensic Investigation and Analysis of the Malicious Use of Gaming Communication Clients."

This script can be used to automate the extraction of localizsed data from the Discord local storage database into a readable CSV format.


## The Findings
During the dissertation study a file called "https_discordapp.com_0.localstorage" was discovered in the AppData/Discord folder, this database included the local user's email address, Emoji Statistics, Draft Messages and the last time the user client interacted with channels.



## Installation Guide
This script has been run and tested with Python3 only, If you do not have a copy of Python3 on your machine please visit [python.org](http://python.org) and download a fresh copy.
In addition the script also requires the third party python package "Another Python SQLite wrapper" also known as ["apsw"](https://rogerbinns.github.io/apsw/). 

Simply run ```"pip install apsw"``` to get this package.

## User Guide
In order to extract the https_discordapp.com_0.localstorage file you must have a copy of the file. This can be found at the following folder directory ```"C:\Users\USERNAME\AppData\Roaming\discord\Local Storage".```

Once you have a copy of the file on your local machine you can run this example command.
```python3 firekitty.py -f https_discordapp.com_0.localstorage -o https_discordapp.com_0.csv```

This will generate a CSV of the data found in the https_discordapp.com_0.localstorage database.

To view all the flags available run the -h command.


## Disclosure
This tool is for RESEARCH PURPOSES ONLY! I am not responsible for any damages of misuse of this tool. Please use with caution. 

## Artwork
The "FireKitty" branding is copyright of © Kitty Magician 2018.

## Licence
This tool is licenced under MIT License.

## With Thanks
I wish to thank the following people/organisations who helped me during my Dissertation.
- Giri, Chris, Nicki, Peter, Dan, Peter, Clare and Sophie
- Ms. Georgina Humphries
- Mr. Danny Webb
- Dr. Ian Kennedy
- Canterbury Christ Church University, School of Law, Criminal Justice and Computing
- Thanks also goes out to Discord LLC and TeamSpeak GmBH for providing me permission to conduct my Dissertation on Gaming Communication Clients.
