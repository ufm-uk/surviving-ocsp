### Insecure direct object reference

Insecure direct object references occur when an application provides direct access to objects based on input provided by the user. As a result of this vulnerability, attackers can bypass authorization and access system resources directly, for example, database files or logs.

The value of a parameter is used directly to retrieve a database record.

```http://foo.bar/somepage?invoice=12345```

The value of a parameter is used directly to perform an operation in the system

```http://foo.bar/changepassword?user=someuser```

The value of a parameter is used directly to retrieve a file system resource

```http://foo.bar/showImage?img=img00011```

The value of a parameter is used directly to access application functionality

```http://foo.bar/accessPage?menuitem=12```

* Don't ignore hashed and encoded IDs.

* When faced with an encrypted ID, it is possible to decrypt the ID using common encryption schemes.

* If the app uses a random hash id, see if the id is predictable.

Applications sometimes use algorithms that produce insufficient entropy, and as such, IDs can be predicted after careful analysis. In this case, try creating some accounts to explore how these IDs are created. You may be able to find a pattern that allows you to predict the IDs belonging to other users.

* If the object reference IDs seem hit or miss, see if there is anything you can do to manipulate the process of creating or binding these object IDs.