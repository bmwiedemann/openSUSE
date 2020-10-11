#!/usr/bin/python3
# use opensuserabbit.py | rabbithandle.py
import datetime
import io
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

def watchtail(fp):
    try:
        fp.seek(0, os.SEEK_END)
    except io.UnsupportedOperation:
        pass # allow pipes
    while True:
        new = fp.readline()
        if new:
            yield new
        else:
            time.sleep(0.25)

for line in watchtail(sys.stdin):
    change = json.loads(line)
    if not 'package' in change:
        continue
    if change['project'] != 'openSUSE:Factory':
        continue
    package = change['package']
    commitdate = datetime.datetime.utcfromtimestamp(int(change["time"])).strftime("%Y-%m-%dT%H:%M:%S")
    if 'rev' in change:
        info = 'Update '+package+' to rev '+change['rev']
    else:
        info = 'Delete '+package
    if not 'user' in change and 'sender' in change:
        change['user'] = change['sender']
    author = change['user']
    if 'requestid' in change:
        info += ' via SR '+change['requestid']+"\n\n"+obsbase+'/request/show/'+change['requestid']+"\n"
        rqobj = get_request(osc.conf.config['apiurl'], change['requestid'])
        commitdate = rqobj.state.when
        user2 = rqobj.creator
        if 'user' in change and user2 != change['user']:
            change['user'] = user2 + ' + ' + change['user']
            author = user2
    else:
        info += "\n\n"
        if 'rev' in change:
            info += obsbase+'/package/rdiff/'+change['project']+'/'+package+'?linkrev=base&rev='+change['rev']+"\n";
            try:
                obsrev = get_source_rev(osc.conf.config['apiurl'], "openSUSE:Factory", package, change['rev'])
                commitdate = datetime.datetime.utcfromtimestamp(int(obsrev["time"])).strftime("%Y-%m-%dT%H:%M:%S")
            except urllib.error.HTTPError:
                pass
    if 'user' in change:
        info += 'by user '+change['user']+"\n"
    if 'comment' in change:
        info += change['comment']
    info += '\n'
    print(info);
    os.environ['GIT_AUTHOR_NAME'] = author
    os.environ['GIT_AUTHOR_EMAIL'] = ''
    if commitdate:
        os.environ['GIT_AUTHOR_DATE'] = commitdate
        print("set commitdate "+commitdate)
    else:
        os.environ.pop('GIT_AUTHOR_DATE', None)
    time.sleep(10)
    try:
        version = subprocess.run(["scripts/getversion", "/mounts/work/SRC/openSUSE:Factory/"+package], shell=False,stdout=subprocess.PIPE).stdout.decode()
        if version and version != "unknown":
            info = info.replace(" to rev ", " to version "+version+" / rev ", 1)
    except:
        pass
    subprocess.call(["tail", "-10", "/mounts/work/SRC/openSUSE:Factory/"+package+"/.rev"], shell=False);
    subprocess.call(["lockfile", "-l", "600", ".pkglock"], shell=False)
    subprocess.call(["scripts/syncone", package], shell=False)
    subprocess.call(["git", "add", pkgmap(package)], shell=False)
    process = subprocess.Popen(["git", "commit", "-F", "-"], stdin=subprocess.PIPE)
    process.communicate(info.encode('utf-8'))
    count += 1
    #if os.environ.get('SSH_AUTH_SOCK') and (count%4) == 0:
    #    subprocess.call(["git", "push"])
    try:
        os.unlink(".pkglock")
    except:
        pass
