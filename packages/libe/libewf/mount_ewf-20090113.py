#!/usr/bin/env python

##    Copyright (c) 2006-2008, David Loveall
##
##    All rights reserved.
##
##    Redistribution and use in source and binary forms, with or without
##    modification, are permitted provided that the following conditions are met:
##
##    Redistributions of source code must retain the above copyright notice, this
##    list of conditions and the following disclaimer.
##    Redistributions in binary form must reproduce the above copyright notice,
##    this list of conditions and the following disclaimer in the documentation
##    and/or other materials provided with the distribution.
##    Neither the name of the creator nor the names of its contributors may be used
##    to endorse or promote products derived from this software without specific
##    prior written permission.
##    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
##    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
##    CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
##    EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
##    PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
##    PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
##    LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
##    NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
##    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import with_statement

mount_ewf_version = "20090113"
libewf_version = "20080501"

import sys, string

# The only part that depends on 2.5 is two instances of the with statement. However, 2.5
# was also the first version to have ctypes bundled. If you've got all the dependencies
# and fix the call to the lock, you're good. It may be easier to just install a current
# release of Python. If you're reading this, it's your call.

version = string.split(string.split(sys.version)[0], ".")

# Some versions of Python have non numerical version number
# E.g. Ubuntu 11.04 Python 2.7.1+
# Therefore limited the version check to only look at the first 2 values
if map(int, version[:2]) < [2,5]:
	sys.stderr.write("This version of Python is too old. Python 2.5.x or 2.6.x is required.\n")
	sys.stderr.write("Try running:\npython2.5 " + string.join(sys.argv) + "\nor:\npython2.6 " + string.join(sys.argv) + "\n")
	sys.exit(8)

if map(int, version[:2]) >= [3,0]:
	sys.stderr.write("This version of Python is too new. Python 2.5.x or 2.6.x is required.\n")
	sys.stderr.write("Try running:\npython2.5 " + string.join(sys.argv) + "\nor:\npython2.6 " + string.join(sys.argv) + "\n")
	sys.exit(8)

try:
	import fuse
except:
	sys.stderr.write("Python FUSE bindings aren't installed.\n")
	sys.exit(16)

if not hasattr(fuse, '__version__'):
	sys.stderr.write("fuse-py doesn't know of fuse.__version__, probably it's too old.\n")
	sys.exit(16)
fuse.fuse_python_api = (0, 2)

import os, tempfile, ctypes, ctypes.util, stat, errno, time, re, threading, subprocess, binascii

libewf_path = ctypes.util.find_library('ewf')
if libewf_path:
	libewf=ctypes.CDLL(libewf_path)
else:
	sys.stderr.write("Couldn't find libewf.\n")
	sys.exit(2)

def c_off_t(i):
	return ctypes.c_int64(i)

def c_array(ctype, l):
	return (ctype * len(l))(*l)

def c_max(ctype):
	size = ctypes.sizeof(ctype)
	signed = ctype(2 ** (8 * size - 1) - 1)
	unsigned = ctype(2 ** (8 * size) - 1)
	return max(signed.value, unsigned.value)

def find_partitions(disktype):
	partitions = {}
	pattern = re.compile('\n *Partition (?P<number>\w+):[^\n]*\((?P<size>\d+)[^\n]* (?P<start>\d+\+?\d*)(?:, bootable)?\)\n(?: *Type (?P<type>0x[0-9A-F]{2}))?', re.DOTALL)
	result = pattern.finditer(disktype)
	for match in result:
		if match.group('type') not in ["0x05", "0x0F", "0xEE"]:
			partitions[match.group('number')] = {'offset': eval(match.group('start'))*512, 'size': eval(match.group('size'))}
	return partitions

class MyStat(fuse.Stat):
	def __init__(self):
		self.st_mode = 0
		self.st_ino = 0
		self.st_dev = 0
		self.st_nlink = 0
		self.st_uid = 0
		self.st_gid = 0
		self.st_size = 0
		self.st_atime = 0
		self.st_mtime = 0
		self.st_ctime = 0

class ewfFS(fuse.Fuse):
	def __init__(self, *args, **kw):
		fuse.Fuse.__init__(self, *args, **kw)
		self.multithreaded = True
		self.partitions = {}
		self.files = {}
		self.disktype = False
		self.rw = False
		self.delta = False
		self.ewf_debug = False
		self.mountpoint = ""
		self.read_lock = threading.Lock()

	def getattr(self, path):
		if self.ewf_debug:
			print "GETATTR:", path
		st = MyStat()
		if path == '/':
			st.st_mode = stat.S_IFDIR | 0555
			st.st_nlink = 2
			return st
		for name in self.files:
			if path == name:
				st.st_mode = stat.S_IFREG | 0444
				st.st_nlink = 1
				st.st_size = len(self.files[name])
				return st
		for name in self.partitions:
			if path == name:
				if self.rw:
					st.st_mode = stat.S_IFREG | 0666
				else:
					st.st_mode = stat.S_IFREG | 0444
				st.st_nlink = 1
				st.st_size = self.partitions[name]['size']
				return st
		return -errno.ENOENT

	def readdir(self, path, offset):
		if self.ewf_debug:
			print "READDIR:", path, "OFFSET:", offset
		for r in  '.', '..':
			yield fuse.Direntry(r)
		for name in self.files:
			yield fuse.Direntry(name[1:])
		for name in self.partitions:
			yield fuse.Direntry(name[1:])

	def open(self, path, flags):
		if self.ewf_debug:
			print "OPEN:", path, "FLAGS:", flags
		for name in self.files:
			if path == name:
				accmode = os.O_RDONLY | os.O_WRONLY | os.O_RDWR
				if (flags & accmode) != os.O_RDONLY:
					if self.ewf_debug:
						print "Returning access error"
					return -errno.EACCES
				return 0
		for name in self.partitions:
			if path == name:
				accmode = os.O_RDONLY | os.O_WRONLY | os.O_RDWR
				if (not self.rw) and (flags & accmode) != os.O_RDONLY:
					if self.ewf_debug:
						print "Returning access error"
					return -errno.EACCES
				return 0
		return -errno.ENOENT

	def read(self, path, size, offset):
		if self.ewf_debug:
			print "READ FROM:", path, "OFFSET:", offset, "SIZE:", size
		for name in self.files:
			if path == name:
				return self.files[name][offset:offset+size]
		for name in self.partitions:
			if path == name:
				if offset > self.partitions[name]['size']:
					size = 0
				if offset+size > self.partitions[name]['size']:
					size = self.partitions[name]['size'] - offset
				buf = ctypes.create_string_buffer(size)
				with self.read_lock:
					libewf.libewf_read_random(self.partitions[name]['handle'], buf, ctypes.c_size_t(size), c_off_t(offset+self.partitions[name]['offset']))
				if self.ewf_debug:
					print "RETURNING LENGTH", len(buf.raw)
				return buf.raw
		return -errno.ENOENT

	def write(self, path, buf, offset):
		if self.ewf_debug:
			print "WRITE TO:", path, "OFFSET:", offset, "SIZE:", len(buf)
		if self.rw:
			size = len(buf)
			for name in self.partitions:
				if path == name:
					if offset > self.partitions[name]['size']:
						size = 0
					if offset+size > self.partitions[name]['size']:
						size = self.partitions[name]['size'] - offset
					if size <= 0:
						if self.ewf_debug:
							print "writing past end of file, returning too big"
						return -errno.EFBIG
					# fuse is expecting an int, not the long which is returned because a c_size_t is unsigned
					#libewf.libewf_write_random.restype = ctypes.c_size_t
					libewf.libewf_write_random.restype = ctypes.c_int
					with self.read_lock:
						result = libewf.libewf_write_random(self.partitions[name]['handle'], ctypes.create_string_buffer(buf[:size]), ctypes.c_size_t(size), c_off_t(offset+self.partitions[name]['offset']))
					#if result == ctypes.c_size_t(-1).value:
					if result == -1:
						if self.ewf_debug:
							print "ERROR on write, returning IO error"
						return -errno.EIO
					if self.ewf_debug:
						#print "RETURNING", int(result)
						print "RETURNING",  result
					#return int(result)
					return result
		return -errno.ENOENT

	def fsdestroy(self):
		if self.ewf_debug:
			print "FSDESTROY"
		for name in self.partitions:
			libewf.close(self.partitions[name]['handle'])

	def truncate(self, path, size):
		if self.ewf_debug:
			print "TRUNCATE", path, size
		return -errno.ENOSYS

	def unlink(self, path):
		if self.ewf_debug:
			print "UNLINK", path
		return -errno.ENOSYS

def find_image_segments(filename, delta = False):
	basename = os.path.basename(filename)
	rootname, extname = os.path.splitext(basename)
	dirname = os.path.dirname(filename)

	contents = os.listdir(dirname)
	filenames = []
	deltanames = []
	for item in contents:
		itemroot, itemext = os.path.splitext(item)
		if itemroot == rootname and libewf.libewf_check_file_signature(os.path.join(dirname, item)) == 1:
			if itemext[:2] == extname[:2]:
				filenames.append(os.path.join(dirname, item))
			if delta and itemext.startswith(".d"):
				deltanames.append(os.path.join(dirname, item))
	filenames.sort()
	deltanames.sort()
	if delta == True:
		filenames += deltanames
	elif delta:
		filenames.append(delta)
	return filenames

def get_header(handle, files, filename, type, name):
	size = min(c_max(ctypes.c_size_t), 2**16) # Don't create a buffer larger than 64k
	buf = ctypes.create_string_buffer(size)
	if libewf.libewf_get_header_value(handle, type, buf, ctypes.c_size_t(size)) and buf.value:
		files[filename] = files[filename] + "# " + name + ": " + buf.value + "\n"

def main():
	libewf.libewf_get_version.restype = ctypes.c_char_p
	if not libewf.libewf_get_version() == libewf_version:
		sys.stderr.write("Using libewf-" + libewf.libewf_get_version() + ". Tested with libewf-" + libewf_version + ".\n")

	usage = """
   %prog [options] <filename(s)> <mountpoint>
  
Note: This utility allows EWF files to be mounted as a filesystem containing a flat disk image. <filename> can be any segment of the EWF file. To be identified, all files need to be in the same directory, have the same root file name, and have the same first character of file extension. Alternatively, multiple filenames can be specified in different locations in the order to be reassembled.
"""
	server = ewfFS(version="%prog " + mount_ewf_version + " FUSE " + fuse.__version__, usage=usage, dash_s_do='undef')
	server.parser.add_option(mountopt="disktype", dest="disktype", metavar="DISKTYPE_BINARY", help="disktype program")
	server.parser.add_option(mountopt="rw", dest="rw", metavar=" ", help="read-write support")
	server.parser.add_option(mountopt="delta", dest="delta", metavar=" ", help="use previously generated delta file")
	server.parser.add_option(mountopt="ewf_debug", dest="ewf_debug", metavar=" ", help="print ewf debug messages")
	server.parse(values=server, errex=1)
	if server.disktype == None:
		server.disktype = "disktype"
	if server.rw == None:
		server.rw = True
		libewf.libewf_get_flags_read_write.restype = ctypes.c_uint8
		flag = libewf.libewf_get_flags_read_write()
	else:
		server.rw = False
		libewf.libewf_get_flags_read.restype = ctypes.c_uint8
		flag = libewf.libewf_get_flags_read()
	if server.delta == None:
		server.delta = True
	elif type(server.delta) == 'str':
		if not (os.path.isfile(server.delta) and libewf.libewf_check_file_signature(server.delta) == 1):
			server.delta = False
	if server.ewf_debug == None:
		server.ewf_debug = True
		libewf.libewf_set_notify_values(ctypes.pythonapi.PyFile_AsFile(ctypes.py_object(sys.stdout)), ctypes.c_uint8(1))
	elif server.ewf_debug == "mount":
		server.ewf_debug = True
		libewf.libewf_set_notify_values(ctypes.pythonapi.PyFile_AsFile(ctypes.py_object(sys.stdout)), ctypes.c_uint8(0))
	elif server.ewf_debug == "lib":
		server.ewf_debug = False
		libewf.libewf_set_notify_values(ctypes.pythonapi.PyFile_AsFile(ctypes.py_object(sys.stdout)), ctypes.c_uint8(1))
	else:
		server.ewf_debug = False
		libewf.libewf_set_notify_values(ctypes.pythonapi.PyFile_AsFile(ctypes.py_object(sys.stdout)), ctypes.c_uint8(0))
	server.mountpoint = os.path.abspath(sys.argv[-1])

	filenames = []
	for arg in sys.argv[1:-1]:
		if os.path.isfile(arg):
			if libewf.libewf_check_file_signature(arg) == 1:
				filenames.append(arg)
	if len(filenames) == 1:
		filenames = find_image_segments(os.path.abspath(filenames[0]), server.delta)
	if len(filenames) == 0:
		server.parser.print_usage()
		sys.stderr.write("ewf segment filename(s) required.\n")
		sys.exit(1)

	if server.ewf_debug:
		print "Filenames:", filenames

	handle = libewf.libewf_open(c_array(ctypes.c_char_p, filenames), ctypes.c_ulong(len(filenames)), ctypes.c_uint8(flag))
	if handle == 0:
		server.parser.print_usage()
		sys.stderr.write("Couldn't open EWF file.\n")
		sys.exit(1)
	libewf.libewf_parse_header_values(handle, 3)

	size = min(c_max(ctypes.c_size_t), 2**16) # Don't create a buffer larger than 64k
	buf = ctypes.create_string_buffer(size)
	prefix = "/" + os.path.splitext(os.path.basename(filenames[0]))[0]
	if os.uname()[0] == "Darwin":
		partition_suffix = ".img"
		drive_suffix = ".dmg"
	else:
		partition_suffix = ""
		drive_suffix = ""

	info_name = prefix + ".txt"
	server.files[info_name] = ""
	get_header(handle, server.files, info_name, "description", "Description")
	get_header(handle, server.files, info_name, "case_number", "Case number")
	get_header(handle, server.files, info_name, "examiner_name", "Examiner name")
	get_header(handle, server.files, info_name, "evidence_number", "Evidence number")
	get_header(handle, server.files, info_name, "notes", "Notes")
	get_header(handle, server.files, info_name, "acquiry_date", "Acquiry date")
	get_header(handle, server.files, info_name, "system_date", "System date")
	get_header(handle, server.files, info_name, "acquiry_operating_system", "Operating system used")
	get_header(handle, server.files, info_name, "acquiry_software_version", "Software version used")
	get_header(handle, server.files, info_name, "password", "Password")
	get_header(handle, server.files, info_name, "compression_type", "Compression type")
	get_header(handle, server.files, info_name, "model", "Model")
	get_header(handle, server.files, info_name, "serial_number", "Serial number")

	media_size = ctypes.c_uint64()
	if libewf.libewf_get_media_size(handle, ctypes.byref(media_size)) != 1:
		sys.stderr.write("Unable to get media size.\n")
		sys.exit(4)
	if media_size.value == 0:
		sys.stderr.write("Invalid media size.\n")
		sys.exit(4)

	server.partitions[prefix + drive_suffix] = {'handle': handle, 'offset': 0, 'size': media_size.value}
	if server.disktype:
		p = subprocess.Popen([server.disktype] + filenames, stdout=subprocess.PIPE)
		server.files[prefix + ".disktype.txt"] = p.stdout.read()
		p.wait()
		partitions = find_partitions(server.files[prefix + ".disktype.txt"])
		for partition in partitions:
			server.partitions[prefix + "p" + partition + partition_suffix] = partitions[partition]
			server.partitions[prefix + "p" + partition + partition_suffix]['handle'] = handle

	size = 16
	md5 = (ctypes.c_uint8 * size)()
	libewf.libewf_get_md5_hash(handle, ctypes.byref(md5), ctypes.c_size_t(size))
	md5_printable = binascii.hexlify(md5)

	full_path = os.path.join(server.mountpoint, prefix[1:] + drive_suffix)
	if os.uname()[0] == "Linux":
		server.files[info_name] = server.files[info_name] + md5_printable + " *" + full_path + "\n"
	else:
		server.files[info_name] = server.files[info_name] + "MD5 (" + full_path + ") = " + md5_printable + "\n"

	server.main()

if __name__ == '__main__':
	main()
