Here's a couple of scripts that do the sweet python virtualenv thing.

- build1-basepython -- build a base python with virtualenv.
- build2-instantclient -- install oracle libraries. skip if you don't care.
- build3-virtualenv -- create a virtual environment based on build1 python.

Assumes these files in dist/.  You don't need instantclient if you
don't care about Oracle.

```
$ ls -l dist
-rw-r-----. 1 mh wheel  1412744 May  5 08:53 get-pip.py
-rw-r--r--. 1 mh wheel 63352239 May  5 08:57 instantclient-basic-linux.x64-12.1.0.2.0.zip
-rw-r-----. 1 mh wheel 16856409 Apr 29 15:38 Python-2.7.11.tgz
```
