# topip

topip is a small piece of code that help you find the most talkative ip addresses in a log file

usage: topip.py [-h] -file FILE [-pcap] [-top TOP]

Arguments:

  -h, --help  show help message 
  
  -file FILE  Your file to parse. Text file by default.
  
  -pcap       If set, will assume you are providing a pcap file, and decode it as text. 
  
  -top TOP    Number of top hits to display. 10 by default.
  
