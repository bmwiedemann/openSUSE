#!/usr/bin/python3
#*******************************************************************************
# Copyright (C) 2008 Novell, Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  - Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
#  - Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  - Neither the name of Novell, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL Novell, Inc. OR THE CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#*****************************************************************************/

from pywbem.mof_compiler import MOFCompiler, MOFWBEMConnection, MOFParseError
from optparse import OptionParser
import os
import errno
import sys
from subprocess import call, PIPE, STDOUT, Popen
from getpass import getpass
import pywbem

sfcb_init_script = None

for filename in ['rcsblim-sfcb', 'rcsfcb']:
    try:
        os.lstat('/usr/sbin/' + filename)
        sfcb_init_script = '/usr/sbin/' + filename
        break
    except OSError:
        # doesn't exist, continue to next filename
        pass

pegasus_init_script = '/etc/init.d/tog-pegasus'
pegasus_cimserver_exe = '/usr/sbin/cimserver'
pegasus_unix_socket = '/var/run/tog-pegasus/cimxml.socket'

scx_home = '/opt/microsoft/scx'
scx_init_script = '/etc/init.d/scx-cimd' 
scx_cimserver_exe = scx_home + '/bin/scxcimserver'
scx_unix_socket = '/var' + scx_home + '/tmp/cim.socket'
scx_provider_dir = scx_home + '/lib/providers'
scx_ext_dir = '/opt/microsoft/scx/lib/providers/ext'

if os.path.isdir('/usr/lib64/cmpi'):
    cmpi_dir = '/usr/lib64/cmpi'
elif os.path.isdir('/usr/lib/cmpi'):
    cmpi_dir = '/usr/lib/cmpi'
else:
    cmpi_dir = None


sfcb_regs = []
peg_regs = []

g_verbose = False
g_restart = True
g_last_output = ''

class Error(Exception):
    pass

class SimpleHandle(object):
    def __init__(self):
        self.default_namespace = 'root/cimv2'

class InstStoringConn(pywbem.WBEMConnection):
    def __init__(self, *args, **kwargs):
        self.instances = {}
        pywbem.WBEMConnection.__init__(self, *args, **kwargs)

    def CreateInstance(self, *args, **kwargs):
        inst = len(args) > 0 and args[0] or kwargs['NewInstance']
        try:
            self.instances[self.default_namespace].append(inst)
        except KeyError:
            self.instances[self.default_namespace] = [inst]
        return pywbem.WBEMConnection.CreateInstance(self, *args, **kwargs)


class SimpleCompiler(MOFCompiler):
    def __init__(self):
        self.first_file = True
        self.handle = MOFWBEMConnection()
        self.handle = SimpleHandle()
        MOFCompiler.__init__(self, self.handle)

    def compile_file(self, filename, ns):
        if self.first_file:
            self.first_file = False
            self.rval = []
            MOFCompiler.compile_file(self, filename, ns)
            return self.rval

        self.rval.append((ns, filename))


def process_sfcb(mof, stage, remove=False):
    mofcomp = SimpleCompiler()
    files = []
    files = mofcomp.compile_file(mof, None)
    for file_ in files:
        dest = stage + '/mofs/' + file_[0]
        src = file_[1]
        if not remove:
            if not os.path.exists(dest):
                os.makedirs(dest)
        dest+= '/' + os.path.basename(src)
        if remove:
            try:
                os.unlink(dest)
            except OSError as e:
                if e.errno != errno.ENOENT:
                    raise
        else:
            if os.path.islink(dest):
                if not os.path.exists(os.readlink(dest)):
                    os.unlink(dest)
            try:
                os.symlink(src, dest)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
                if os.readlink(dest) != src:
                    print('Warning: %s already exists' % dest)
    for src in sfcb_regs:
        dest = stage + '/regs/' + os.path.basename(src)
        if remove:
            try:
                os.unlink(dest)
            except OSError as e:
                if e.errno != errno.ENOENT:
                    raise
        else:
            if os.path.islink(dest):
                if not os.path.exists(os.readlink(dest)):
                    os.unlink(dest)
            try:
                os.symlink(src, dest)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
                if os.readlink(dest) != src:
                    print('Warning: %s already exists' % dest)


    if g_restart:
        sfcb_running = False
        if run([sfcb_init_script, 'status']) == 0:
            sfcb_running = True
            run([sfcb_init_script, 'stop'])
        try:
            run_check(['sfcbrepos','-f'])
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            print("Warning: `sfcbrepos` doesn't exist. Ignoring.")
        finally:
            if sfcb_running:
                run([sfcb_init_script, 'start'])


def run_check(command, *args, **kwargs):
    if g_verbose:
        po = Popen(command, *args, **kwargs)
        output = ''
    else:
        po = Popen(command, stdout=PIPE, stderr=STDOUT, *args, **kwargs)
        output = po.communicate()[0]
    rc = po.wait()
    if rc != 0:
        if isinstance(command, list):
            command = ' '.join(command)

        err = Error("Error running '%s', returned %s" %(command, rc))
        err.last_output = output
        raise err
    return 0

def run(command, *args, **kwargs):
    if command == None or (isinstance(command, list) and command[0] == None):
        # No command to execute
        return 1

    global g_last_output
    if g_verbose:
        return call(command, *args, **kwargs)
    po = Popen(command, stdout=PIPE, stderr=STDOUT, *args, **kwargs)
    output = po.communicate()[0]
    rc = po.wait()
    if rc != 0:
        g_last_output = output
    return rc


def process_pegasus(mof, mofcomp, init_script, cimserver_exe, remove=False,
        provider_dir=None, env=None):
    """ Handle Pegasus

    Arguments:
    mofs -- list of MOF files
    mofcomp -- instance of MOFCompiler
    init_script -- Init script for Pegasus
    cimserver_exe -- Full path to cimserver executable
    remove -- True if we're uninstalling providers / removing schema
    """

    peg_running = True
    if (run([init_script, 'status']) != 0):
        peg_running = False
        run_check([cimserver_exe, 
            'enableIndicationService=false',
            'enableHttpsConnection=false',
            'enableHttpConnection=false'], env=env)

    try:
        mofcomp.compile_file(mof, 'root/cimv2')
        for reg in peg_regs:
            mofcomp.compile_file(reg, 'root/PG_InterOp')
        if remove:
            mofcomp.rollback(verbose=g_verbose)
    finally:

        if not peg_running:
            run_check([cimserver_exe, '-s'], env=env)

    if provider_dir:
        try:
            insts = mofcomp.handle.instances['root/PG_InterOp']
        except KeyError:
            insts = []
        providers = [inst['Location'] for inst in insts 
                if inst.classname.lower() == 'pg_providermodule']
        providers = list(set(providers))

        for reg in peg_regs:
            dest = provider_dir + '/' + os.path.basename(reg)
            if not dest.endswith('.mof'):
                dest += '.mof'
            if not remove:
                if not os.path.exists(dest):
                    try:
                        os.symlink(reg, dest)
                    except OSError as e:
                        print(e)
            else:
                if os.path.islink(dest):
                    try:
                        os.unlink(dest)
                    except OSError as e:
                        print(e)

        for provider in providers:
            libname = 'lib' + provider + '.so'
            src = cmpi_dir + '/' + libname
            dest = provider_dir + '/' + libname
            if not remove:
                if os.path.exists(src) and not os.path.exists(dest):
                    try:
                        os.symlink(src, dest)
                    except OSError as e:
                        print(e)
            # don't remove, in case the provider is shared with other 
            # packages (like pyCmpiProvider)
            #
            #else:
            #    if os.path.islink(dest):
            #        try:
            #            os.unlink(dest)
            #        except OSError as e:
            #            print(e)



def sfcb_installed():
    return os.path.exists(sfcb_init_script)

def pegasus_installed():
    return os.path.exists(pegasus_init_script) and \
            os.path.exists(pegasus_cimserver_exe)

def scx_installed():
    return os.path.exists(scx_init_script) and \
            os.path.exists(scx_cimserver_exe)

if __name__ == '__main__':
    usage = 'usage: %prog [options] -d <Data Dir>'
    oparser = OptionParser(usage=usage)
    oparser.add_option('-s', '--search', dest='search', 
            help='Search path to find missing schema elements.  This option can be present multiple times.', 
            metavar='Path', action='append')
    oparser.add_option('-n', '--namespace', dest='ns', 
            help='Specify the namespace', metavar='Namespace',
            default='root/cimv2')
    oparser.add_option('-u', '--url', dest='url', 
            help='URL to the CIM Server', metavar='URL')
    oparser.add_option('-d', '--dir', dest='dir', 
            help='Directory containing MOF and registration files', 
            metavar='Dir')
    oparser.add_option('-v', '--verbose',
            action='store_true', dest='verbose', default=False,
            help='Print more messages to stdout')
    oparser.add_option('-r', '--remove',
            action='store_true', dest='remove', default=False,
            help='Remove elements found in MOF, instead of create them')
    oparser.add_option('-x', '--no-restart',
            action='store_true', dest='no_restart', default=False,
            help="Don't run 'sfcbrepos', don't restart sfcbd")
    oparser.add_option('-l', '--username',
            dest='username', metavar='Username',
            help='Specify the username')
    oparser.add_option('-p', '--password', 
            dest='password', metavar='Password',
            help='Specify the password')
    oparser.add_option('-g', '--stage', 
            dest='stage', metavar='SFCB stage',
            help='Specify the SFCB stage directory',
            default='/var/lib/sfcb/stage')

    (options, args) = oparser.parse_args()

    try:
        if options.dir is None: 
            oparser.error('No directory given')
        options.dir = os.path.abspath(options.dir)
        if not os.path.isdir(options.dir):
            print('Error: %s is not a directory' % options.dir)
            sys.exit(1)

        moffile = options.dir + '/deploy.mof'
        if not os.path.exists(moffile):
            print('Error: missing file:', moffile)
            sys.exit(1)

        elems = os.listdir(options.dir)
        for elem in elems:
            if elem.endswith('.sfcb.reg'):
                sfcb_regs.append(options.dir + '/' + elem)
            elif elem.endswith('.peg.reg'):
                peg_regs.append(options.dir + '/' + elem)

        g_verbose = options.verbose
        g_restart = not options.no_restart

        do_pegasus = pegasus_installed() and peg_regs
        do_scx = scx_installed() and peg_regs

        do_scx = do_scx and (options.url == ':scx:' or not options.url)
        do_pegasus = do_pegasus and (options.url == ':tog-pegasus:' or 
                            not options.url)

        if sfcb_regs:
            process_sfcb(moffile, options.stage, options.remove)

        search = options.search
        if args:
            oparser.error('Extra arguments given')

        pegs = []

        if not pegasus_installed() and options.url == ':tog-pegasus:':
            print('Error: tog-pegasus is not installed')
            sys.exit(1)
        if not scx_installed() and options.url == ':scx:':
            print('Error: SCX is not installed')
            sys.exit(1)

        if do_pegasus:
            pegs.append({'url':pegasus_unix_socket,
                         'exe':pegasus_cimserver_exe,
                         'init':pegasus_init_script,
                         'provider_dir':None,
                         'env':None,
                         })
        if do_scx:
            env = os.environ.copy()
            ldp = '%(h)s/lib:%(h)s/lib/providers:%(h)s/lib/providers/ext' % \
                            {'h':scx_home}
            if 'LD_LIBRARY_PATH' in env and env['LD_LIBRARY_PATH']:
                ldp+= ':' + env['LD_LIBRARY_PATH']
            env['LD_LIBRARY_PATH'] = ldp

            pegs.append({'url':scx_unix_socket,
                         'exe':scx_cimserver_exe,
                         'init':scx_init_script,
                         'provider_dir':scx_ext_dir,
                         'env':env,
                         })

        if not pegs and options.url:
            pegs = [{'url':options.url,
                     'exe':None,
                     'init':None,
                     }]

        passwd = options.password
        if options.username and not passwd:
            passwd = getpass('Enter password for %s: ' % options.username)
        if options.username:
            creds = (options.username, passwd)
        else:
            creds = None

        if search is None:
            search = ['/usr/share/mof/cim-current']

        search.append(os.path.abspath(options.dir))

        # if removing, we'll be verbose later when we actually remove stuff.
        # We don't want MOFCompiler to be verbose, as that would be confusing. 
        verbose = options.verbose and not options.remove


        for peg in pegs:
            if options.remove:
                conn = pywbem.WBEMConnection(peg['url'], creds)
                conn = MOFWBEMConnection(conn=conn)
            else:
                conn = InstStoringConn(peg['url'], creds)
            #conn.debug = True
            conn.default_namespace = options.ns

            mofcomp = MOFCompiler(handle=conn, search_paths=search, verbose=verbose)

            try:
                process_pegasus(moffile, mofcomp, peg['init'], peg['exe'], 
                        remove=options.remove, provider_dir=peg['provider_dir'],
                        env=peg['env'])
            except MOFParseError as pe:
                sys.exit(1)
            except pywbem.CIMError as ce:
                sys.exit(1)

    except Error as e:
        print(str(e))
        if hasattr(e, 'last_output'):
            print(e.last_output)
        sys.exit(1)

