import unittest

from pfsense_ssh import Pfsense, SSHClient

# SSH server of pfSense
HOST = '192.168.11.40'
USER = 'root'
PASS = 'pfsense'


class TestCommand(unittest.TestCase):
    def test_ls(self):
        expected = [u'COPYRIGHT\n', u'bin\n', u'boot\n', u'cf\n', u'conf\n',
                    u'conf.default\n', u'dev\n', u'dist\n', u'etc\n',
                    u'home\n', u'kernels\n', u'lib\n', u'libexec\n',
                    u'media\n', u'mnt\n', u'proc\n', u'rescue\n', u'root\n',
                    u'sbin\n', u'scripts\n', u'tank\n', u'tmp\n', u'usr\n',
                    u'var\n']
        with SSHClient(HOST, 22, USER, PASS) as s:
            stdin, stdout, stderr = s.execute('ls /')
            results = stdout.readlines()
            for item in expected:
                self.assertTrue(item in results)


class TestSftp(unittest.TestCase):
    def test_download_file(self):
        with SSHClient(HOST, 22, USER, PASS) as s:
            s.sftp.get("/conf/config.xml", '/tmp/config.xml')


class TestPfsenseCommands(unittest.TestCase):
    def test_reboot(self):
        ssh = SSHClient(HOST, 22, USER, PASS)
        pfsense = Pfsense(ssh)
        pfsense.reboot()
        ssh.close()


if __name__ == '__main__':
    unittest.main()
