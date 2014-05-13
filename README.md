pfSense SSH
===========
A simple SSH Client, including utilities for manipulating pfSense.


Installation
------------

    pip install -r requirements.txt



pfSense Configuration
----------------------
In pfSense, delete '/root/.profile' to prevent the menu from conflicting
with root access.


Usage
-----

    from pfsense_ssh import Pfsense, SSHClient

    ssh = SSHClient('192.168.11.40', 22, 'root', 'pfsense')
    pfsense = Pfsense(ssh)

    stdin, stdout, stderr = pfsense.reboot()
    ssh.close()


basic ssh commands

    from pfsense_ssh import SSHClient

    with SSHClient('127.0.0.1', 22, 'username', 'pass') as s:
        stdin, stdout, stderr = s.execute('ls /')


Or explicitly close the connection:

    from pfsense_ssh import SSHClient

    client = SSHClient('127.0.0.1', 22, 'username', 'pass')
    stdin, stdout, stderr = client.execute('ls /')
    client.close()
