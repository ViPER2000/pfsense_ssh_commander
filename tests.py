import unittest

from pyssh import SSHClient


class TestCommand(unittest.TestCase):
    def test_ls(self):
        expected = [u'COPYRIGHT\n', u'bin\n', u'boot\n', u'cf\n', u'conf\n',
                    u'conf.default\n', u'dev\n', u'dist\n', u'etc\n',
                    u'home\n', u'kernels\n', u'lib\n', u'libexec\n',
                    u'media\n', u'mnt\n', u'proc\n', u'rescue\n', u'root\n',
                    u'sbin\n', u'scripts\n', u'tank\n', u'tmp\n', u'usr\n',
                    u'var\n']
        with SSHClient('192.168.11.40', 22, 'travis', 'llamas123') as s:
            stdin, stdout, stderr = s.execute('ls /')
            results = stdout.readlines()
            for item in expected:
                self.assertTrue(item in results)

    def test_reboot(self):
        with SSHClient('192.168.11.40', 22, 'travis', 'llamas123') as s:
            stdin, stdout, stderr = s.execute('sudo /etc/rc.reboot')
            print stdout.readlines()
            print stderr.readlines()


if __name__ == '__main__':
    unittest.main()
