## Detection

In the case that the request contains multiple values for the parameter, you can give three possibilities:

1. That the method returns the first value of the parameter.
2. To return the last.
3. Or to return a combination of all values.

The following table illustrates how different web technologies behave in presence of multiple occurrences of the same HTTP parameter.

Given the URL and querystring: ```http://example.com/?color=red&color=blue```

| Web Application Server Backend | Parsing Result	| Example |
| ---- | ---- | ---- |
| ASP.NET / IIS	| All occurrences concatenated with a comma |	color=red,blue
| ASP / IIS |	All occurrences concatenated with a comma | color=red,blue
| .NET Core 3.1 / Kestrel	| All occurrences concatenated with a comma	| color=red,blue
| .NET 5 / Kestrel |	All occurrences concatenated with a comma | color=red,blue
| PHP / Apache |	Last occurrence only |	color=blue |
| PHP / Zeus |	Last occurrence only |	color=blue |
| JSP, Servlet / Apache Tomcat	| First occurrence only	| color=red |
| JSP, Servlet / Oracle Application Server 10g |	First occurrence only |	color=red |
| JSP, Servlet / Jetty |	First occurrence only |	color=red |
| IBM Lotus Domino |	Last occurrence only |	color=blue |
| IBM HTTP Server |	First occurrence only |	color=red |
| node.js / express |	First occurence only |	color=red |
| mod_perl, libapreq2 / Apache |	First occurrence only |	color=red |
| Perl CGI / Apache |	First occurrence only |	color=red |
| mod_wsgi (Python) / Apache	| First occurrence only |	color=red |
| Python / Zope |	All occurrences in List data type |	color=[‘red’,’blue’] |

### Server Side HPP

An attacker could try to add another from parameter to trick the server, and in that case, this parameter would transact from one account to another that is not owned by the attacker.

Normal :
```https://example.com/transfer?from=1377&to=1234&amount=5000```

Exploited :
```https://example.com/transfer?from=1377&to=1234&amount=5000&from=1338```

### Client Side HPP
An attacker could add other "candidate" param and send this to the victim. When the victim open the URL, it won't matter what your vote, this will be always "green" vote.

Normal:
```http://example.com/votation?candidate=green&vote=1```

Exploited:
```http://example.com/votation?candidate=green&vote=1%26candidate=black```

### Email 
```email=victim@example.com&email=attacker@example.com```
