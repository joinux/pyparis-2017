"""Fabfile for PyData Paris."""

from fabric import task, Connection
from invoke import run

HOST = 'pyparis.org'


@task
def deploy():
    c = Connection(HOST)
    c.directory("/var/www/pyparis2018")
    c.run("rsync -e ssh -avz build/ root@dedibox.abilian.com:/var/www/pyparis2018")
