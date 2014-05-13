from StringIO import StringIO
import paramiko 


class SSHClient(object):
    """
    Basic SSH client.
    """
    def __init__(self, host, port, username, password, key=None,
                 passphrase=None):
        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if key is not None:
            key = paramiko.RSAKey.from_private_key(StringIO(key),
                                                   password=passphrase)
        self.__client.connect(host, port, username=username,
                              password=password, pkey=key, timeout=30)

    def close(self):
        """
        Closes the SSH connection.
        """
        if self.__client is not None:
            self.__client.close()
            self.__client = None

    def execute(self, command):
        """
        Runs a command on the remote machine.

        Returns a tuple: (stdin, stdout, stderr)
        """
        return self.__client.exec_command(command)

    @property
    def sftp(self):
        """
        Returns paramiko.SFTPClient based upon the created SSH connection.
        """
        return self.__client.open_sftp()

    def __enter__(self, *args):
        return self

    def __exit__(self, type, value, traceback):
        self.sftp.close()
        self.close()


class Pfsense(object):
    """
    Contains commands for manipulating a pfSense box.
    """
    def __init__(self, ssh_client):
        self.__ssh = ssh_client

    def reboot(self):
        """
        Reboots the machine.
        """
        return self.__ssh.execute('/etc/rc.reboot')

    def reload_config(self):
        """
        Reloads the configuration files.
        """
        return self.__ssh.execute('/etc/rc.reload_all')
