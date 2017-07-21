import logging
import paramiko


def test():
    client = paramiko.SSHClient()
    print client


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test()
