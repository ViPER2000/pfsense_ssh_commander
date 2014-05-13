PySSH
=====

Library for basic SSH commands


Usage
-----

    from pyssh import SSHClient

    with SSHClient('127.0.0.1', 22, 'username', 'pass') as s:
        s.execute('ls /')


Or explicitly close the connection:

    from pyssh import SSHClient

    client = SSHClient('127.0.0.1', 22, 'username', 'pass')
    res = client.execute('ls /')
    client.close()
