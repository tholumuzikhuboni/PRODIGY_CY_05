from scapy.all import sniff

# Function to handle packets
def packet_callback(packet):
    if packet.haslayer(IP):
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst
        protocol = packet[IP].proto
        payload = packet.payload

        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {dest_ip}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}\n")

# Start sniffing
print("Packet Sniffer started...")
sniff(prn=packet_callback, store=0)
