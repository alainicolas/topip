import argparse
import re
import subprocess
from collections import Counter

#Setup the parameters
parser = argparse.ArgumentParser(description='IP Top talker decoder')
parser.add_argument("-file", required=True, type=str, help="Your text file to parse")
parser.add_argument("-pcap", action="store_true", help="If set, will decode your pcap file to a text file")
parser.add_argument("-top", default=10, type=int, help="Number of top hits to display. 10 by default")

#Load the parameters
args = parser.parse_args()
file = args.file
pcap = args.pcap
top = args.top

#If its a pcap file, decode it using tshark, parse it, delete de temp file
# tshark -V -r file.pcap > file.txt

if pcap:
    print("transforming pcap...")
    #Create a temp text file from the pcap
    proc = subprocess.Popen('tshark -V -r' + file + ' > tmpFileIpTop.txt',
                            shell=True,
                            stdout=subprocess.PIPE)
    proc.wait()
    with open("tmpFileIpTop.txt", 'r') as fp:
        #Create a list of IP in a text file, with a counter
        ip_count = Counter()
        for ip in re.findall(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)', fp.read()):
            ip_count[ip] += 1

        #Display the top IP
        print(f'{"IP address":<20}{"hits"}')
        for ip, count in ip_count.most_common(top):
            print(f'{ip:<20}{count}')

    #Deleting the temp text file
    subprocess.call(["rm", "-f", "tmpFileIpTop.txt"])
else:
    # If its not a pcap file, parse the file directly :
    with open(file) as fp:
        # Create a list of IP in a text file, with a counter
        ip_count = Counter()
        for ip in re.findall(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)', fp.read()):
            ip_count[ip] += 1

        # Display the top IP
        print(f'{"IP address":<20}{"hits"}')
        for ip, count in ip_count.most_common(top):
            print(f'{ip:<20}{count}')




