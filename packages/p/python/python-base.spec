#
# spec file for package python-base
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define so_version 2_7-1_0

Name:           python-base
Version:        2.7.18
Release:        0
Summary:        Python Interpreter base package
License:        Python-2.0
Group:          Development/Languages/Python
URL:            http://www.python.org/
%define         tarversion %{version}
%define         tarname Python-%{tarversion}
Source0:        http://www.python.org/ftp/python/%{version}/%{tarname}.tar.xz
Source4:        http://www.python.org/ftp/python/%{version}/%{tarname}.tar.xz.asc
Source6:        python.keyring
Source1:        macros.python2
Source2:        baselibs.conf
Source3:        README.SUSE
Source5:        local.pth
# Fixed bundled wheels
Source10:       setuptools-44.1.1-py2.py3-none-any.whl
Source11:       pip-20.0.2-py2.py3-none-any.whl
# For Patch 66
Source66:       recursion.tar
Source99:       python-base-rpmlintrc
# COMMON-PATCH-BEGIN
Patch1:         python-2.7-dirs.patch
Patch2:         python-distutils-rpm-8.patch
Patch3:         python-2.7.5-multilib.patch
Patch4:         python-2.5.1-sqlite.patch
Patch5:         python-2.7.4-canonicalize2.patch
Patch7:         python-2.6-gettext-plurals.patch
Patch8:         python-2.6b3-curses-panel.patch
Patch10:        sparc_longdouble.patch
Patch13:        python-2.7.2-fix_date_time_compiler.patch
Patch17:        remove-static-libpython.patch
# PATCH-FEATURE-OPENSUSE python-bundle-lang.patch bnc#617751 dimstar@opensuse.org -- gettext: when looking in default_localedir also check in locale-bundle.
Patch20:        python-bundle-lang.patch
# PATCH-FIX-UPSTREAM Fix argument passing in libffi for aarch64
Patch22:        python-2.7-libffi-aarch64.patch
Patch24:        python-bsddb6.patch
# PATCH-FIX-UPSTREAM accept directory-based CA paths as well
Patch33:        python-2.7.9-ssl_ca_path.patch
# PATCH-FEATURE-SLE disable SSL verification-by-default in http clients
Patch34:        python-2.7.9-sles-disable-verification-by-default.patch
# PATCH-FIX-UPSTREAM do not use non-ASCII filename in test_ssl.py
Patch35:        do-not-use-non-ascii-in-test_ssl.patch
# PATCH-FIX-UPSTREAM bmwiedemann@suse.de -- allow python packages to build reproducibly
Patch38:        reproducible.patch
# bypass boo#1078485 random failing tests
Patch40:        python-skip_random_failing_tests.patch
# PATCH-FIX-UPSTREAM sorted tar https://github.com/python/cpython/pull/2263
Patch41:        python-sorted_tar.patch
# https://github.com/python/cpython/pull/9624 (https://bugs.python.org/issue34834)
Patch47:        openssl-111-middlebox-compat.patch
# PATCH-FIX-SUSE python default SSLContext doesn't contain OP_CIPHER_SERVER_PREFERENCE
Patch48:        openssl-111-ssl_options.patch
# PATCH-FIX-UPSTREAM CVE-2019-5010-null-defer-x509-cert-DOS.patch bnc#1122191 mcepl@suse.com
# gh#python/cpython#11569
# Fix segfault in ssl's cert parser
Patch49:        CVE-2019-5010-null-defer-x509-cert-DOS.patch
# PATCH-FIX-UPSTREAM bpo36160-init-sysconfig_vars.patch gh#python/cpython#12131 mcepl@suse.com
# Initialize sysconfig variables in test_site.
Patch50:        bpo36160-init-sysconfig_vars.patch
# PATCH-FIX-UPSTREAM CVE-2017-18207.patch gh#python/cpython#4437 psimons@suse.com
# Add check for channels of wav file in Lib/wave.py
Patch51:        CVE-2017-18207.patch
# PATCH-FIX-UPSTREAM gh#python/cpython#12341
Patch55:        bpo36302-sort-module-sources.patch
# Fix installation in /usr/local (boo#1071941), adapted from Fedora
# https://src.fedoraproject.org/rpms/python3/blob/master/f/00251-change-user-install-location.patch
# Set values of prefix and exec_prefix in distutils install command
# to /usr/local if executable is /usr/bin/python* and RPM build
# is not detected to make pip and distutils install into separate location
Patch56:        adapted-from-F00251-change-user-install-location.patch
# Switch couple of tests failing on acient SLE-12
Patch57:        python-2.7.17-switch-off-failing-SSL-tests.patch
# PATCH-FIX-UPSTREAM CVE-2020-8492-urllib-ReDoS.patch bsc#1162367 mcepl@suse.com
# Fixes Python urrlib allowed an HTTP server to conduct Regular
# Expression Denial of Service (ReDoS)
Patch58:        CVE-2020-8492-urllib-ReDoS.patch
# PATCH-FIX-UPSTREAM CVE-2019-9674-zip-bomb.patch bsc#1162825 mcepl@suse.com
# Improve documentation warning against the possible zip bombs
Patch59:        CVE-2019-9674-zip-bomb.patch
# PATCH-FIX-UPSTREAM configure_PYTHON_FOR_REGEN.patch bsc#1078326 mcepl@suse.com
# PYTHON_FOR_REGEN value is set very weird upstream
Patch60:        configure_PYTHON_FOR_REGEN.patch
# PATCH-FIX-SLE CVE-2021-3177-buf_ovrfl_PyCArg_repr.patch bsc#1181126 mcepl@suse.com
# buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution
Patch61:        CVE-2021-3177-buf_ovrfl_PyCArg_repr.patch
# PATCH-FIX-UPSTREAM CVE-2021-23336-only-amp-as-query-sep.patch bsc#[0-9]+ mcepl@suse.com
# this patch makes things totally awesome
Patch62:        CVE-2021-23336-only-amp-as-query-sep.patch
# PATCH-FIX-UPSTREAM CVE-2021-3737-fix-HTTP-client-infinite-line-reading-after-a-HTTP-100-Continue.patch boo#1189241 gh#python/cpython#25916
Patch63:        CVE-2021-3737-fix-HTTP-client-infinite-line-reading-after-a-HTTP-100-Continue.patch
# PATCH-FIX-UPSTREAM CVE-2021-3733-fix-ReDoS-in-request.patch boo#1189287 gh#python/cpython#24391
Patch64:        CVE-2021-3733-fix-ReDoS-in-request.patch
# PATCH-FIX-UPSTREAM sphinx-update-removed-function.patch bpo#35293 gh#python/cpython#22198 -- fix doc build
Patch65:        sphinx-update-removed-function.patch
# PATCH-FIX-UPSTREAM CVE-2019-20907_tarfile-inf-loop.patch bsc#1174091 mcepl@suse.com
# avoid possible infinite loop in specifically crafted tarball (CVE-2019-20907)
# REQUIRES SOURCE 66
Patch66:        CVE-2019-20907_tarfile-inf-loop.patch
# PATCH-FIX-UPSTREAM CVE-2020-26116-httplib-header-injection.patch bsc#1177211
# Fixes httplib to disallow control characters in method to avoid header
# injection
Patch67:        CVE-2020-26116-httplib-header-injection.patch
# PATCH-FIX-UPSTREAM CVE-2021-4189-ftplib-trust-PASV-resp.patch bsc#1194146 mcepl@suse.com
# Make ftplib not trust the PASV response. (gh#python/cpython#24838)
Patch68:        CVE-2021-4189-ftplib-trust-PASV-resp.patch
# PATCH-FIX-UPSTREAM CVE-2022-0391-urllib_parse-newline-parsing.patch bsc#1195396 mcepl@suse.com
# whole long discussion is on bpo#43882
# fix for santization URLs containing ASCII newline and tabs in urllib.parse
Patch69:        CVE-2022-0391-urllib_parse-newline-parsing.patch
# PATCH-FIX-UPSTREAM CVE-2015-20107-mailcap-unsafe-filenames.patch bsc#1198511 mcepl@suse.com
# avoid the command injection in the mailcap module.
Patch70:        CVE-2015-20107-mailcap-unsafe-filenames.patch
# PATCH-FIX-UPSTREAM CVE-2021-28861 bsc#1202624
# Coerce // to / in Lib/BaseHTTPServer.py
Patch71:        CVE-2021-28861-double-slash-path.patch
Patch72:        bpo34990-2038-problem-compileall.patch
# PATCH-FIX-UPSTREAM CVE-2022-45061-DoS-by-IDNA-decode.patch bsc#1205244 mcepl@suse.com
# Avoid DoS by decoding IDNA for too long domain names
Patch73:        CVE-2022-45061-DoS-by-IDNA-decode.patch
# COMMON-PATCH-END
%define         python_version    %(echo %{tarversion} | head -c 3)
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libbz2-devel
%if %{suse_version} >= 1500
BuildRequires:  libnsl-devel
%endif
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1550
# The provider for python(abi) is in rpm-build-python
BuildRequires:  rpm-build-python
%endif
BuildRequires:  xz
BuildRequires:  zlib-devel
#!BuildIgnore:  python
# for the test suite
BuildRequires:  netcfg
# explicitly, see bnc#697251:
Requires:       libpython%{so_version} = %{version}-%{release}
Provides:       %{name} = %{python_version}
# bug437293
%ifarch ppc64
Obsoletes:      python-64bit
%endif
Provides:       python-ctypes = 1.1.0
Obsoletes:      python-ctypes < 1.1.0
Provides:       python-argparse = 1.4.0.1
Obsoletes:      python-argparse < 1.4.0.1
Provides:       python2-argparse = 1.4.0.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Provides:       python2-base = %{version}

%description
Python is an interpreted, object-oriented programming language, and is
often compared to Tcl, Perl, Scheme, or Java.  You can find an overview
of Python in the documentation and tutorials included in the python-doc
(HTML) or python-doc-pdf (PDF) packages.

This package contains all of stand-alone Python files, minus binary
modules that would pull in extra dependencies.

%package -n python-devel
Summary:        Include Files and Libraries Mandatory for Building Python Modules
Group:          Development/Languages/Python
Requires:       glibc-devel
Requires:       python = %{version}
Requires:       python-base = %{version}-%{release}
Provides:       python2-devel = %{version}
# provide testsuite namespace that was split in python3 to ease dependencies
Provides:       python-testsuite = %{version}
Provides:       python2-testsuite = %{version}

%description -n python-devel
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.

This package contains header files, a static library, and development
tools for building Python modules, extending the Python interpreter or
embedding Python in applications.

%package -n python-xml
Summary:        A Python XML Interface
Group:          Development/Libraries/Python
Requires:       python-base = %{version}-%{release}
# pyxml used to live out of tree
Provides:       pyxml = 0.8.5
Obsoletes:      pyxml < 0.8.5
Provides:       python2-xml = %{version}

%description -n python-xml
The expat module is a Python interface to the expat XML parser. Since
Python2.x, it is part of the core Python distribution.

%package -n libpython%{so_version}
Summary:        Python Interpreter shared library
Group:          Development/Languages/Python

%description -n libpython2_7-1_0
Python is an interpreted, object-oriented programming language, and is
often compared to Tcl, Perl, Scheme, or Java.  You can find an overview
of Python in the documentation and tutorials included in the python-doc
(HTML) or python-doc-pdf (PDF) packages.

This package contains libpython2.7 shared library for embedding in
other applications.

%prep
%setup -q -n %{tarname}
# patching
# COMMON-PREP-BEGIN
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1
%patch13 -p1
%patch17 -p1
%patch20 -p1
%patch22 -p1
%patch24 -p1
%patch33 -p1
%if %{suse_version} < 1500 && !0%{?is_opensuse}
%patch34 -p1
%endif
%patch35 -p1
%patch38 -p1
%ifarch ppc ppc64 ppc64le
%patch40 -p1
%endif
%patch41 -p1
%if %{suse_version} >= 1500
%patch47 -p1
%patch48 -p1
%else
%patch57 -p1
%endif
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch55 -p1
%patch56 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1

# For patch 66
cp -v %{SOURCE66} Lib/test/recursion.tar

# drop Autoconf version requirement
sed -i 's/^version_required/dnl version_required/' configure.ac
# COMMON-PREP-END

# Replace bundled wheels with the updates ones
rm -v Lib/ensurepip/_bundled/*.whl
cp -v %{SOURCE10} %{SOURCE11} Lib/ensurepip/_bundled/
STVER=$(basename %{SOURCE10}|cut -d- -f2)
PIPVER=$(basename %{SOURCE11}|cut -d- -f2)
sed -i -e "s/^\(\s*_SETUPTOOLS_VERSION\s\+=\s\+\)\"[0-9.]\+\"/\1\"${STVER}\"/" \
       -e "s/^\(\s*_PIP_VERSION\s\+=\s\+\)\"[0-9.]\+\"/\1\"${PIPVER}\"/" \
    Lib/ensurepip/__init__.py

cp -p %{SOURCE1} macros.python2
%if %{suse_version} < 1500
# on SLE12 and SLE11 the python2 modules will still be called python-xxxx
# as this SPEC file is used on SLE12, keep it in here for the time being
sed -i -e 's/python2_package_prefix python2/python2_package_prefix python/' macros.python2
%endif

%build
%define _lto_cflags %{nil}
export OPT="%{optflags} -DOPENSSL_LOAD_CONF -fwrapv"

autoreconf -f -i . # Modules/_ctypes/libffi

# provide a stable timestamp
touch -r %{SOURCE0} Makefile.pre.in

# prevent make from trying to rebuild asdl stuff, which requires existing
# python installation
touch Parser/asdl* Python/Python-ast.c Include/Python-ast.h

%configure \
    --docdir=%{_docdir}/python \
    --with-fpectl \
    --enable-ipv6 \
    --enable-shared \
    --enable-unicode=ucs4

%if 0%{?do_profiling}
target=profile-opt
%else
target=all
%endif
LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH \
    make %{?_smp_mflags} $target

%check
# on hppa, the threading of glibc is quite broken. The tests just stop
# at some point, and the machine does not build anything more until a
# timeout several hours later.
%ifnarch hppa
# test_file(2k) fails in autobuild env - "stdin.seek(-1)" wrongly succeeds. probably an issue with autobuild's stdin
# test_urllib2 relies on being able to resolve local address, which is notoriously impossible in autobuild
# test_urllib2_localnet randomly fails out
EXCLUDE="test_urllib2 test_urllib2_localnet test_file test_file2k"
# test_nis and test_threading are AWFULLY slow.
EXCLUDE="$EXCLUDE test_nis test_threading"
# test_gdb fails if gdb with (different) python support is part of the buildsystem
EXCLUDE="$EXCLUDE test_gdb"
%ifarch ia64
# test_smtplib's testSend is known to be broken and on ia64 it actually fails most of the time, preventing the build.
EXCLUDE="$EXCLUDE test_smtplib"
%endif
# test_unicode fails in Factory
EXCLUDE="$EXCLUDE test_unicode"
%if 0%{?qemu_user_space_build}
# test_asyncore fails because of unimplemented sockopt
EXCLUDE="$EXCLUDE test_asyncore test_mmap"
# emulation is unreliable
EXCLUDE="$EXCLUDE test_multiprocessing test_thread"
# qemu bug (siginterrupt handling)
EXCLUDE="$EXCLUDE test_signal"
%endif
%ifarch s390 s390x
# test_regrtest tries to segfault the interpreter by dereferencing a NULL pointer, but that doesn't
# actually produce a segfault on S390
EXCLUDE="$EXCLUDE test_regrtest"
%endif

# This test (part of test_uuid) requires real network interfaces
# so that ifconfig output has "HWaddr <something>".  Some kvm instances
# don't have any such interface breaking the uuid module test.
EXCLUDE="$EXCLUDE test_uuid"

# bypass boo#1078485
# many flaky tests if osc build in loop on ppc64le
%ifarch ppc ppc64 ppc64le
EXCLUDE="$EXCLUDE test_asynchat test_asyncore test_dircache test_multiprocessing test_nntplib test_queue test_signal test_socket test_subprocess test_telnetlib test_xmlrpc "
%endif

# Limit virtual memory to avoid spurious failures
if test $(ulimit -v) = unlimited || test $(ulimit -v) -gt 10000000; then
  ulimit -v 10000000 || :
fi
make test TESTOPTS="-l -w -x $EXCLUDE" TESTPYTHONOPTS="-R"
# use network, be verbose:
#make test TESTOPTS="-l -u network -v"
%endif

%install
# replace rest of /usr/local/bin/python or /usr/bin/python2.5 with /usr/bin/python
find . -name '*.py' -type f | grep -vE "^./Parser/|^./Python/" \
  | xargs grep -lE '^#! *(/usr/.*bin/(env +)?)?python' \
  | xargs sed -r -i -e '1s@^#![[:space:]]*(/usr/(local/)?bin/(env +)?)?python([0-9]+\.[0-9]+)?@#!/usr/bin/python@'
# the grep inbetween makes it much faster
########################################
# install it
########################################
%make_install OPT="%{optflags} -fPIC"
install -m 644 %{SOURCE5} %{buildroot}%{_libdir}/python%{python_version}/site-packages/_local.pth
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d/
install -m 644 macros.python2 %{buildroot}%{_rpmconfigdir}/macros.d/

# make sure /usr/lib/python/site-packages exists even on lib64 machines
mkdir -p %{buildroot}%{_prefix}/lib/python%{python_version}/site-packages
########################################
# some cleanups
########################################
# remove hard links and replace them with symlinks
for dir in bin include %{_lib} ; do
    rm -f %{buildroot}/%{_prefix}/$dir/python
    ln -s python%{python_version} %{buildroot}/%{_prefix}/$dir/python
done
CLEANUP_DIR="%{buildroot}%{_libdir}/python%{python_version}"
# don't distribute precompiled windows installers (duh)
rm -f $CLEANUP_DIR/distutils/command/*.exe
# kill imageop.so - it used to be insecure and it is deprecated anyway
rm -f $CLEANUP_DIR/lib-dynload/imageop.so
# link shared library instead of static library that tools expect
ln -s ../../libpython%{python_version}.so %{buildroot}%{_libdir}/python%{python_version}/config/libpython%{python_version}.so
# remove various things that don't need to be in python-base
rm %{buildroot}%{_bindir}/idle
rm -rf $CLEANUP_DIR/{curses,bsddb,idlelib,lib-tk,sqlite3}
rm $CLEANUP_DIR/ssl.py*
#        does not work without _ssl.so anyway
# replace duplicate .pyo/.pyc with hardlinks
%fdupes %{buildroot}/%{_libdir}/python%{python_version}
########################################
# documentation
########################################
export PDOCS=%{buildroot}%{_docdir}/%{name}
install -d -m 755 $PDOCS
install -c -m 644 %{SOURCE3}                        $PDOCS/
install -c -m 644 LICENSE                           $PDOCS/
install -c -m 644 README                            $PDOCS/
ln -s python%{python_version}.1.gz %{buildroot}%{_mandir}/man1/python.1.gz
########################################
# devel
########################################
# install Makefile.pre.in and Makefile.pre
cp Makefile Makefile.pre.in Makefile.pre %{buildroot}%{_libdir}/python%{python_version}/config/

%post -n libpython2_7-1_0 -p %{run_ldconfig}
%postun -n libpython2_7-1_0 -p %{run_ldconfig}

%files -n python-devel
%defattr(-, root, root)
%{_libdir}/python%{python_version}/config/*
%exclude %{_libdir}/python%{python_version}/config/Setup
%exclude %{_libdir}/python%{python_version}/config/Makefile
%defattr(644, root, root, 755)
%{_libdir}/libpython*.so
%{_libdir}/pkgconfig/python-%{python_version}.pc
%{_libdir}/pkgconfig/python.pc
%{_libdir}/pkgconfig/python2.pc
%{_includedir}/python*
%exclude %{_includedir}/python%{python_version}/pyconfig.h
%{_libdir}/python%{python_version}/test
%defattr(755, root, root)
%{_bindir}/python-config
%{_bindir}/python2-config
%{_bindir}/python%{python_version}-config

%files -n python-xml
%defattr(644, root, root, 755)
%{_libdir}/python%{python_version}/xml
%{_libdir}/python%{python_version}/lib-dynload/pyexpat.so

%files -n libpython2_7-1_0
%defattr(644, root, root)
%{_libdir}/libpython*.so.*

%files
%defattr(644, root, root, 755)
%{_rpmconfigdir}/macros.d/macros.python2
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.SUSE
%doc %{_mandir}/man1/python.1*
%doc %{_mandir}/man1/python2.1*
%doc %{_mandir}/man1/python%{python_version}.1*
%dir %{_includedir}/python%{python_version}
%{_includedir}/python%{python_version}/pyconfig.h
%{_libdir}/python
%dir %{_prefix}/lib/python%{python_version}
%dir %{_prefix}/lib/python%{python_version}/site-packages
%dir %{_libdir}/python%{python_version}
%dir %{_libdir}/python%{python_version}/config
%{_libdir}/python%{python_version}/config/Setup
%{_libdir}/python%{python_version}/config/Makefile
%{_libdir}/python%{python_version}/*.*
%{_libdir}/python%{python_version}/compiler
%{_libdir}/python%{python_version}/ctypes
%{_libdir}/python%{python_version}/distutils
%{_libdir}/python%{python_version}/email
%{_libdir}/python%{python_version}/encodings
%{_libdir}/python%{python_version}/ensurepip
%{_libdir}/python%{python_version}/hotshot
%{_libdir}/python%{python_version}/importlib
%{_libdir}/python%{python_version}/json
%{_libdir}/python%{python_version}/lib2to3
%{_libdir}/python%{python_version}/logging
%{_libdir}/python%{python_version}/multiprocessing
%{_libdir}/python%{python_version}/plat-*
%{_libdir}/python%{python_version}/pydoc_data
%{_libdir}/python%{python_version}/unittest
%{_libdir}/python%{python_version}/wsgiref
%dir %{_libdir}/python%{python_version}/site-packages
%{_libdir}/python%{python_version}/site-packages/README
%{_libdir}/python%{python_version}/site-packages/_local.pth
%dir %{_libdir}/python%{python_version}/lib-dynload
%{_libdir}/python%{python_version}/lib-dynload/_bisect.so
#%%{_libdir}/python%%{python_version}/lib-dynload/_bytesio.so
%{_libdir}/python%{python_version}/lib-dynload/_csv.so
%{_libdir}/python%{python_version}/lib-dynload/_collections.so
%{_libdir}/python%{python_version}/lib-dynload/_ctypes.so
%{_libdir}/python%{python_version}/lib-dynload/_ctypes_test.so
%{_libdir}/python%{python_version}/lib-dynload/_elementtree.so
#%%{_libdir}/python%%{python_version}/lib-dynload/_fileio.so
%{_libdir}/python%{python_version}/lib-dynload/_functools.so
%{_libdir}/python%{python_version}/lib-dynload/_heapq.so
%{_libdir}/python%{python_version}/lib-dynload/_hotshot.so
%{_libdir}/python%{python_version}/lib-dynload/_io.so
%{_libdir}/python%{python_version}/lib-dynload/_json.so
%{_libdir}/python%{python_version}/lib-dynload/_locale.so
%{_libdir}/python%{python_version}/lib-dynload/_lsprof.so
%{_libdir}/python%{python_version}/lib-dynload/_md5.so
%{_libdir}/python%{python_version}/lib-dynload/_multiprocessing.so
%{_libdir}/python%{python_version}/lib-dynload/_random.so
%{_libdir}/python%{python_version}/lib-dynload/_sha.so
%{_libdir}/python%{python_version}/lib-dynload/_sha256.so
%{_libdir}/python%{python_version}/lib-dynload/_sha512.so
%{_libdir}/python%{python_version}/lib-dynload/_socket.so
%{_libdir}/python%{python_version}/lib-dynload/_struct.so
%{_libdir}/python%{python_version}/lib-dynload/_testcapi.so
%{_libdir}/python%{python_version}/lib-dynload/array.so
%{_libdir}/python%{python_version}/lib-dynload/audioop.so
%{_libdir}/python%{python_version}/lib-dynload/binascii.so
%{_libdir}/python%{python_version}/lib-dynload/bz2.so
%{_libdir}/python%{python_version}/lib-dynload/cPickle.so
%{_libdir}/python%{python_version}/lib-dynload/cStringIO.so
%{_libdir}/python%{python_version}/lib-dynload/cmath.so
%{_libdir}/python%{python_version}/lib-dynload/crypt.so
%{_libdir}/python%{python_version}/lib-dynload/datetime.so
%{_libdir}/python%{python_version}/lib-dynload/fcntl.so
%{_libdir}/python%{python_version}/lib-dynload/future_builtins.so
%{_libdir}/python%{python_version}/lib-dynload/grp.so
%{_libdir}/python%{python_version}/lib-dynload/itertools.so
%{_libdir}/python%{python_version}/lib-dynload/linuxaudiodev.so
%{_libdir}/python%{python_version}/lib-dynload/math.so
%{_libdir}/python%{python_version}/lib-dynload/mmap.so
%{_libdir}/python%{python_version}/lib-dynload/nis.so
%{_libdir}/python%{python_version}/lib-dynload/operator.so
%{_libdir}/python%{python_version}/lib-dynload/ossaudiodev.so
%{_libdir}/python%{python_version}/lib-dynload/parser.so
%{_libdir}/python%{python_version}/lib-dynload/resource.so
%{_libdir}/python%{python_version}/lib-dynload/select.so
%{_libdir}/python%{python_version}/lib-dynload/spwd.so
%{_libdir}/python%{python_version}/lib-dynload/strop.so
%{_libdir}/python%{python_version}/lib-dynload/syslog.so
%{_libdir}/python%{python_version}/lib-dynload/termios.so
%{_libdir}/python%{python_version}/lib-dynload/time.so
%{_libdir}/python%{python_version}/lib-dynload/unicodedata.so
%{_libdir}/python%{python_version}/lib-dynload/zlib.so
%{_libdir}/python%{python_version}/lib-dynload/_codecs*.so
%{_libdir}/python%{python_version}/lib-dynload/_multibytecodec.so
%{_libdir}/python%{python_version}/lib-dynload/Python-%{tarversion}-py%{python_version}.egg-info
# these modules don't support 64-bit arches (disabled by setup.py)
%ifnarch alpha ia64 x86_64 s390x ppc64 ppc64le sparc64 aarch64
# requires sizeof(int) == sizeof(long) == sizeof(char*)
%{_libdir}/python%{python_version}/lib-dynload/dl.so
%endif
%attr(755, root, root) %{_bindir}/pydoc
%attr(755, root, root) %{_bindir}/python
%attr(755, root, root) %{_bindir}/python%{python_version}
%attr(755, root, root) %{_bindir}/smtpd.py
%{_bindir}/python2
%exclude %{_bindir}/2to3

%changelog
