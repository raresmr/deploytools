# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
from fabric.api import *

#env.hosts = [
#    '10.0.15.21',
#    '10.0.15.22'
#]
# Set the username
env.user   = "vagrant"

# Set the password [NOT RECOMMENDED]
env.password = "vagrant"
ip_ver={}
def web1_dev():
    env.hosts = ['10.0.15.22']

def web2_prod():
    env.hosts = ['10.0.15.21']

def all():
    env.hosts = ['10.0.15.21', '10.0.15.22']

#env.roledefs = { 'stageup' : ['10.0.15.21', '10.0.15.22'], 'produp' : ['10.0.15.21', '10.0.15.22'] }

def new_ver(max_ver):
   run("echo %s > ~/max" % max_ver)
   sudo("npm install -g npm@%s" % max_ver)

def npm_ver():
     npmv = run("npm -v")
     ip_ver[env.host] = npmv
     
     if len(ip_ver) == len(env.hosts):
        print 'ok'
     return ip_ver

#@roles("stageup","produp")
def command():
     dict_v = npm_ver()
     print dict_v

     max_ver = max(list(dict_v.values()))
     print max_ver
      
     for key, value in dict_v.iteritems():
       if value != max_ver:   
        print 'install ' + key + ' ' + max_ver
       # return max_ver
        new_ver(max_ver)          
       else:
        print 'not ' + key + ' ' + value

