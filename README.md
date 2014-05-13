pfSense SSH Commander
===========
A simple SSH Client, including utilities for manipulating pfSense.
Although Fabric could do this job, this small library gives more control
over SSH.


Installation
------------

    python setup.py install



pfSense Configuration
----------------------
In pfSense, delete '/root/.profile' to prevent the menu from conflicting
with console access.


Usage
-----

```python
from pfsense_ssh import Pfsense, SSHClient

ssh = SSHClient('127.0.0.1', 22, 'username', 'pass')
pfsense = Pfsense(ssh)

stdin, stdout, stderr = pfsense.reboot()
ssh.close()
```

basic ssh commands

```python
from pfsense_ssh import SSHClient

with SSHClient('127.0.0.1', 22, 'username', 'pass') as s:
    stdin, stdout, stderr = s.execute('ls /')
```


Explicitly close the connection when using SSHClient:

```python
from pfsense_ssh import SSHClient

client = SSHClient('127.0.0.1', 22, 'username', 'pass')
stdin, stdout, stderr = client.execute('ls /')
client.close()
```
