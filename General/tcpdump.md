# Display a pcap file
tcpdump -r passwordz.pcap

# Display ips and filter and sort
tcpdump -n -r passwordz.pcap | awk -F" " '{print $3}' | sort -u | head

# Grab a packet capture on port 80
tcpdump tcp port 80 -w output.pcap -i eth0

# Check for ACK or PSH flag set in a TCP packet
tcpdump -A -n 'tcp[13] = 24' -r passwordz.pcap

