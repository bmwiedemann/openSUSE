#!/usr/bin/python

import os, os.path, glob

outdir_base = '/srv/www/eximstats'

def main():
    os.chdir('/var/log/exim')
    reports = glob.glob('main.log-*.gz') + glob.glob('main.log-*.bz2')

    for report in reports:
        (base, ext) = os.path.splitext(report)
        daystr = base[-8:]

        outdir = os.path.join(outdir_base, daystr)

        if os.path.exists(outdir):
            continue
        print 'processing', daystr
        os.mkdir(outdir)

        if ext == '.gz':
            catprg = 'zcat'
        elif ext == '.bz2':
            catprg = 'bzcat'



        os.system('%s %s | eximstats -html -charts -chartdir %s > %s/index.html' \
            % (catprg, report, outdir, outdir))






if __name__ == '__main__':
        main()

