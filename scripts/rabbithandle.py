#!/usr/bin/python3
# use opensuserabbit.py | rabbithandle.py
import datetime
import json
import os
import osc.conf
import subprocess
import sys
import time
from osc.core import get_request, get_source_rev

osc.conf.get_config()
obsbase='https://build.opensuse.org'
outdir='packages'
count=0

def pkgmap(p):
     first=p[0]
     if p.startswith("lib"):
         first=p[0:4]
     return outdir+"/"+first.lower()+"/"+p

for line in sys.stdin:
    change = json.loads(line)
    if not 'package' in change:
        continue
    if change['project'] != 'openSUSE:Factory':
        continue
    package = change['package']
    if 'rev' in change:
        info = 'Update '+package+' to rev '+change['rev']
    else:
        info = 'Delete '+package
    if 'requestid' in change:
        info += ' via SR '+change['requestid']+"\n\n"+obsbase+'/request/show/'+change['requestid']+"\n"
        rqobj = get_request(osc.conf.config['apiurl'], change['requestid'])
        commitdate = rqobj.state.when
        user2 = rqobj.creator
        if 'user' in change and user2 != change['user']:
            change['user'] = user2 + ' + ' + change['user']
    else:
        info += "\n\n"
        if 'rev' in change:
            info += obsbase+'/package/rdiff/'+change['project']+'/'+package+'?linkrev=base&rev='+change['rev']+"\n";
    if 'user' in change:
        info += 'by user '+change['user']+"\n"
    if 'comment' in change:
        info += change['comment']
    info += '\n'
    print(info);
    if 'rev' in change:
        obsrev = get_source_rev(osc.conf.config['apiurl'], "openSUSE:Factory", package, change['rev'])
        commitdate = datetime.datetime.utcfromtimestamp(int(obsrev["time"])).strftime("%Y-%m-%dT%H:%M:%S")
    if commitdate:
        os.environ['GIT_AUTHOR_DATE'] = commitdate
        os.environ['GIT_COMMITTER_DATE'] = commitdate
        print("set commitdate "+commitdate)
    else:
        os.environ.pop('GIT_AUTHOR_DATE', None)
        os.environ.pop('GIT_COMMITTER_DATE', None)
    time.sleep(10)
    subprocess.call(["tail", "-10", "/mounts/work/SRC/openSUSE:Factory/"+package+"/.rev"], shell=False);
    subprocess.call(["lockfile", "-l", "600", ".pkglock"], shell=False)
    subprocess.call(["scripts/syncone", package], shell=False)
    subprocess.call(["git", "add", pkgmap(package)], shell=False)
    process = subprocess.Popen(["git", "commit", "-F", "-"], stdin=subprocess.PIPE)
    process.communicate(info.encode('utf-8'))
    count += 1
    if os.environ.get('SSH_AUTH_SOCK') and (count%4) == 0:
        subprocess.call(["git", "push"])
    try:
        os.unlink(".pkglock")
    except:
        pass
