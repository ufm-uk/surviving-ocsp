## Online Password Cracking
https://crackstation.net/ http://finder.insidepro.com/

## Hashcat Needed to install new drivers to get my GPU Cracking to work on the Kali linux VM and I also had to use the --force parameter.
apt-get install libhwloc-dev ocl-icd-dev ocl-icd-opencl-dev
apt-get install pocl-opencl-icd

## Crack with hashcat
hashcat --force -m 500 -a 0 -o found1.txt --remove puthasheshere.hash /usr/share/wordlists/rockyou.txt



## Crack Raw MD5
john --format=raw-md5 -w=/usr/share/wordlists/rockyou.txt hashfilepath

## Crack ZIP/RAR
zip2john zipfile > output.txt
rar2john rarfile > output.txt
-> than john

### characters a 1-8 length
fcrackzip -b -c a -l 1-8 -u -v lmao.zip

### dictionary 
fcrackzip -u -D -p passwordlist.txt lmao.zip 

### generate password list
https://charlesreid1.com/wiki/John_the_Ripper/Password_Generation

cewl www.megacorpone.com -m 6 -w megacorp-cewl.txt
-> -m min word length 6
-> -w output to file

nano /etc/john/john.conf
john --wordlist=megacorp-cewl.txt --rules --stdout > mutated.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
john --rules --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
john --rules --wordlist=/usr/share/wordlists/rockyou.txt unshadowed.txt
john --format=descrypt --wordlist /usr/share/wordlists/rockyou.txt hash.txt
john --format=descrypt hash --show


## using Crunch

crunch 6 6 0123456789ABCDEF -o crunch1.txt
crunch 4 4 -f /usr/share/crunch/charset.lst mixalpha
