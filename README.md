Yo Python
=====

A Python client for the Yo platform. This is pretty pointless, but I want to try to overengineer it as much as possible, just for fun.

Pull Requests are actively encouraged!

Installation
==

`pip install yo-client`

Usage
==

````
import yo

API_TOKEN = '...'

yo_client = yo.Yo(API_TOKEN)

yo_client.yo()     # Send a Yo to all your subscribers

yo_user = 'mcos'

yo_client.yo(username=yo_user)     # Send a Yo to a specific user

````

Roadmap
==

Since I want to overengineer this in the future, the following needs to be done:

* Full test coverage
* Travis integration
* Updated documentation
* A landing page on Github pages
* Full git-flow workflow
