import os, sys, time, apsw, csv
import argparse
#print(apsw.sqlitelibversion())
motd = '''
       Kitty Magician
       IceKitty - https://github.com/kittymagician/FireKitty
       Version 1.0 - Developed by Oliver Bryant
       '''
print(motd)
print(" ")
parser = argparse.ArgumentParser()                                               
parser.add_argument("--file", "-f", type=str, required=False, help="Specify your .localstorage file. typically located at AppData\Roaming\discord\Local Storage")
parser.add_argument("--output", "-o", type=str, required=False, help="Specify output file eg: -o /directory/file.csv")
args = parser.parse_args()
key = []
item = []
argdis = False


def connect():
    try:
        connection=apsw.Connection(args.file)
    except:
        print('\x1b[1;31m'+'ERROR! Unable to open SQL file '+ args.file +'are you specifying the correct http_discordapp.com_0.localstorage file?' + '\x1b[0m')
        print('Press ENTER to terminate the application.')
        input()
        exit()

    cursor=connection.cursor()

    try:
        for row in cursor.execute("SELECT * FROM ItemTable"):
            cItem = row[0]
            key.append(cItem)
            tItem = row[1].decode('utf-16')
            item.append(tItem)
    except:
        print('\x1b[1;31m'+'ERROR! The input file specified is invaild '+ args.file +'are you specifying the correct http_discordapp.com_0.localstorage file?' + '\x1b[0m')
        print('Press ENTER to terminate the application.')
        input()
        exit()
            
    try:
        if args.output is None:
            f = open("report.csv", 'w')
        else:
            f = open(args.output, 'w')
            argdis = True
    except:
        print('\x1b[1;31m'+'ERROR! Unable to open' + args.output + 'are you specifying the correct path?' + '\x1b[0m')
        print('\x1b[1;31m'+'Be sure to specify the ABSOLUTE path. You can use PWD on linux to find the Absolute Path' + '\x1b[0m')
        print('\x1b[1;31m'+'Here\'s an example of a pathway searchcli.py -f file.localstorage -o /home/ubuntu/workspace/test/file.csv'+ '\x1b[0m')
        print('Press ENTER to terminate the application.')
        input()
        exit()

    with f:
        fnames = ['key', 'item']
        writer = csv.writer(f)
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        maxNum = len(key) # Get the MAX number of Keys.
        counter = 0 
        while counter < maxNum:
            writer.writerow({'key':key[counter],'item':item[counter]})
            counter = counter + 1

    f.close()
    if argdis == True:
        print('\x1b[6;30;42m' + 'Exported local discord data to ' + args.output + '\x1b[0m')
    else:
        print('\x1b[6;30;42m' + 'Exported local discord data to ' + 'report.csv' + '\x1b[0m')


if args.file != None:
    connect()
    