from StringIO import StringIO
import paramiko 


class SSHClient(object):
    def __init__(self, host, port, username, password, key=None,
                 passphrase=None):
        self.__username = username
        self.__password = password
        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if key is not None:
            key = paramiko.RSAKey.from_private_key(StringIO(key),
                                                   password=passphrase)
        self.__client.connect(host, port, username=username,
                              password=password, pkey=key, timeout=30)

    def close(self):
        if self.__client is not None:
            self.__client.close()
            self.__client = None

    def execute(self, command):
        return self.__client.exec_command(command)

    @property
    def sftp(self):
        return self.__client.open_sftp()

    def __enter__(self, *args):
        return self

    def __exit__(self, type, value, traceback):
        self.sftp.close()
        self.close()


class Pfsense(object):
    def __init__(self, ssh_client):
        self.__ssh = ssh_client

    def reboot(self):
        return self.__ssh.execute('/etc/rc.reboot')

    def reload_config(self):
        return self.__ssh.execute('/etc/rc.reload_all')
