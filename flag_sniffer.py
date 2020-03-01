#====================================================
#
# flag_sniffer.py
# Author: James Lawson
# Date: 02/05/20
#
# Description: This script will sniff the local network looking for trafic
#              going to the scoring machine and will attempt to extract the flags
#              from the payload of the message.
#====================================================
import swpag_client
import sys
import getopt
import string

import scapy.all as scapy



url = 'http://54.241.76.20'
token = '66978175b387ba7b6dee386d16b40b29'

team_object = swpag_client.Team(url, token)

interface = ""
scoreboard_ip = ""
our_machine_ip = ""


def scoreboard_sniffer(packet):
    print('Found a packet')

    flag = ""
    # Extract flag from packet
    # Dependent on the format of the flags and messages.

    team_object.submit_flag(flag)



def main(argv):

    global interface
    global scoreboard_ip
    global our_machine_ip

    shortargs = "iface:scoreip:ourip"
    longargs = ["interface=", "scoreboard-ip=", "our-machine-ip="]

    try:
        opts, args = getopt.getopt(argv, shortargs, longargs)
    except getopt.GetoptError:
        print('USAGE: python3 sniffer.py --interface eth0'
              + '--scoreboard-ip --ourmachine-ip xxx.xxx.xxx.xxx')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-iface", "--interface"):
            interface = arg
        elif opt in ("-scoreip", "--scoreboard-ip"):
            scoreboard_ip = arg
        elif opt in ("-ourip", "--our-machine-ip"):
            our_machine_ip = arg

    print('Interface is         : ', interface)
    print('Scoreboard IP is     : ', scoreboard_ip)
    print('Our Machine IP is    : ', our_machine_ip)

    scapy.sniff(iface=interface, store=False, filter="ip dst host "+scoreboard_ip, prn=scoreboard_sniffer)


if __name__ == "__main__":
    main(sys.argv[1:])
