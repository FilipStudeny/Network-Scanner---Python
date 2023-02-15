from scapy.all import ARP, Ether, srp

target_ip = input("Enter target IP address: ")

# create ARP request packet
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

# send the packet and receive the response
result = srp(packet, timeout=3, verbose=0)[0]

# parse the response and print the results
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
print("IP" + " "*18 + "MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
