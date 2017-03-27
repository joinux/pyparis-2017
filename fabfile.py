"""Fabfile for PyData Paris."""

from fabric.api import env, task
from fabric.operations import local
from fabtools import require

env.user = 'root'
env.hosts = ['dedibox.abilian.com']

VH_PYDATA = """
server {
  server_name pyparis.org www.pyparis.org;
  root /var/www/pyparis2017;
  index index.html;
  access_log /var/log/nginx/pyparis-access.log;
}
"""


@task
def setup_nginx():
  require.nginx.site("pyparis.org", VH_PYDATA)


@task
def deploy():
  require.directory("/var/www/pyparis2017")
  local("rsync -e ssh -avz build/ root@dedibox.abilian.com:/var/www/pyparis2017")
