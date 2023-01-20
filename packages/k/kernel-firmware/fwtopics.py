#!/usr/bin/python3

import sys, string, os, re, subprocess, tempfile, fnmatch

class FWTopics(object):
    def __init__(self):
        self.topics = {}
        self.firmwares = {}
        self.aliases = {}
        self.modules = {}
        self.modmap = {}
        self.dirty = False
        self.read_topics()

    def kernel_binary_rpm(self, file):
        file = os.path.basename(file)
        if not fnmatch.fnmatch(file, 'kernel*.rpm'):
            return False
        blacklist = ( '*.noarch.rpm', '*.src.rpm', '*.nosrc.rpm',
                      '*-debuginfo*', '*-debugsource*',
                      '*-devel-*', '*-hmac-*',
                      'kernel-docs*', 'kernel-syms-*' )
        for p in blacklist:
            if fnmatch.fnmatch(file, p):
                return False
        return True

    def modinfo(self, ko, attr):
        return subprocess.check_output(['/usr/sbin/modinfo', '-F', attr, ko]).decode('utf-8').split('\n')
    
    def canon_module(self, name):
        return re.sub('-', '_', name)

    def read_topics(self):
        with open('topics.list', 'r') as f:
            for t in f.read().split('\n'):
                t.rstrip()
                if t == '':
                    continue
                if re.match('#', t):
                    continue
                l = t.split()
                first = re.sub(r':$', '', l.pop(0))
                topic = l.pop(0)
                self.topics[first] = topic
                if l == []:
                    m = self.canon_module(first)
                    self.modules[first] = [ m ]
                    self.modmap[m] = topic
                else:
                    self.modules[first] = []
                    for m in l:
                        m = self.canon_module(m)
                        self.modules[first].append(m)
                        self.modmap[m] = topic
                # print(first, topic, self.modules[first])

    def read_aliases(self):
        with open('aliases.list', 'r') as f:
            for t in f.read().split('\n'):
                t.rstrip()
                if t == '':
                    continue
                l = t.split()
                module = re.sub(r':$', '', l.pop(0))
                if self.aliases.get(module) == None:
                    self.aliases[module] = []
                self.aliases[module].append(l.pop(0))

    def write_aliases(self):
        if self.dirty:
            print('updating aliases...')
            with open('aliases.list', 'w') as f:
                for t in sorted(self.aliases.keys()):
                    for m in sorted(self.aliases[t]):
                        f.write(t + ': ' + m + '\n')
            self.dirty = False

    def parse_whence(self, file):
        with open(file, 'r') as f:
            for t in f.read().split('\n'):
                t.rstrip()
                if t == '':
                    continue
                if re.match('----', t):
                    first = None
                elif re.match('Driver:', t):
                    t = re.sub(r'^Driver: *', '', t)
                    first = t.split()[0]
                    first = re.sub(r':.*$', '', first)
                    if self.topics.get(first) == None:
                        print('No matching topic entry for:', t)
                        first = None
                    elif re.match(r'File:', t):
                        if first == None:
                            continue
                        t = re.sub(r'^File: *', '', t)
                        t = re.sub('"', '', t)
                        self.firmwares[t] = first
                    elif re.match(r'Link:', t):
                        if first == None:
                            continue
                        t = re.sub(r'^Link: *', '', t)
                        t = re.sub(r' ->.*$', '', t)
                        t = re.sub('"', '', t)
                        self.firmwares[t] = first

    def check_module(self):
        def __check_module(ko, name):
            for f in self.modinfo(ko, 'firmware'):
                if f == '':
                    continue
                first = self.firmwares.get(f)
                if first != None:
                    if self.topics[first] == 'SKIP':
                        continue
                    if not name in self.modules[first]:
                        print('Module', name, 'is missing for', first)
                        print('  firmware:', f)
        return __check_module

    def update_alias(self):
        def __update_alias(ko, name):
            if self.modmap.get(name) != None and self.modmap[name] != 'SKIP':
                for f in self.modinfo(ko, 'alias'):
                    if f == '':
                        continue
                    if re.match(r'^acpi', f):
                        f = re.sub(r'([^:]*):([^:]*)$', r'\1%3A\2', f)
                    if self.aliases.get(name) == None:
                        self.aliases[name] = []
                    if not f in self.aliases[name]:
                        self.aliases[name].append(f)
                        self.dirty = True
                        print('adding alias', name, f)
        return __update_alias

    def scan_firmware_dir(self, dir, proc):
        for root, dirs, files in os.walk(dir):
            for p in files:
                ko = os.path.join(root, p)
                name = re.sub(r'\.xz$', '', p)
                name = re.sub(r'\.zst$', '', p)
                if not fnmatch.fnmatch(name, '*.ko'):
                    continue
                name = re.sub(r'\.ko$', '', name)
                name = self.canon_module(name)
                proc(ko, name)

    def scan_firmware_rpm(self, rpm, proc):
        if not self.kernel_binary_rpm(rpm):
            return
        with tempfile.TemporaryDirectory() as dir:
            subprocess.call('rpm2cpio ' + rpm + ' | cpio -i --make-directories -D ' + dir,
                            shell=True)
            self.scan_firmware_dir(dir, proc)

    def scan_firmware(self, arg, proc):
        if os.path.isdir(arg):
            self.scan_firmware_dir(arg, proc)
        else:
            self.scan_firmware_rpm(arg, proc)
