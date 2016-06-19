# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
from fabric.api import *


env.hosts = [
    '10.0.15.21',
    '10.0.15.22'
  # 'ip.add.rr.ess
  # 'server2.domain.tld',
]
# Set the username
env.user   = "vagrant"

# Set the password [NOT RECOMMENDED]
env.password = "vagrant"
list=[]
def update_npm():
     npmv = run("npm -v")
     list.append(npmv)
     return max(list)

def npm_ver():
    z = update_npm()
    print 'asta' + z 
    run("echo %s > ~/test" % z)
    run("sudo npm install -g npm@%s" % z)
	
