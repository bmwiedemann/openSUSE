#!/usr/bin/python3
# use opensuserabbit.py | rabbithandle.py
import json
import os
import subprocess
import sys

obsbase='https://build.opensuse.org'
outdir='packages'

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
    info = 'Update '+package+' to rev '+change['rev']
    if 'requestid' in change:
        info += ' via SR '+change['requestid']+"\n\n"+obsbase+'/request/show/'+change['requestid']+"\n"
    else:
        info += "\n\n"+obsbase+'/package/rdiff/'+change['project']+'/'+package+'?linkrev=base&rev='+change['rev']+"\n";
    info += 'by user '+change['user']+"\n"
    if 'comment' in change:
        info += change['comment']
    info += '\n'
    print(info);
    subprocess.call(["tail", "-10", "/mounts/work/SRC/openSUSE:Factory/"+package+"/.rev"], shell=False);
    subprocess.call(["lockfile", "-l", "600", ".pkglock"], shell=False)
    subprocess.call(["scripts/syncone", package], shell=False)
    subprocess.call(["git", "add", pkgmap(package)], shell=False)
    process = subprocess.Popen(["git", "commit", "-F", "-"], stdin=subprocess.PIPE)
    process.communicate(info.encode('utf-8'))
    try:
        os.unlink(".pkglock")
    except:
        pass
