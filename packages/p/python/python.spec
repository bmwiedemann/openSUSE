#
# spec file for package python
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


Name:           python
Version:        2.7.18
Release:        0
Summary:        Python Interpreter
License:        Python-2.0
Group:          Development/Languages/Python
URL:            http://www.python.org/
%define         tarversion %{version}
%define         tarname Python-%{tarversion}
Source0:        http://www.python.org/ftp/python/%{version}/%{tarname}.tar.xz
Source1:        README.SUSE
Source8:        sle_tls_checks_policy.py
#Source11:       testfiles.tar.bz2
Source50:       idle.appdata.xml
Source51:       idle.desktop
# issues with copyrighted Unicode testing files
# For Patch 66
Source66:       recursion.tar

# !!!!!!!!!!!!!!
# do not add or edit patches here. please edit python-base.spec
# instead and run pre_checkin.sh
# !!!!!!!!!!!!!!
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
BuildRequires:  automake
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  gdbm-devel
BuildRequires:  gmp-devel
BuildRequires:  libbz2-devel
%if %{suse_version} >= 1500
BuildRequires:  libnsl-devel
BuildRequires:  libopenssl-1_1-devel
%else
BuildRequires:  libopenssl-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  tk-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(x11)
# for %%{_datadir}/application and %%{_datadir}/mime/packages
BuildRequires:  filesystem
BuildRequires:  update-desktop-files
# for %%{_datadir}/icons/hicolor directories
BuildRequires:  hicolor-icon-theme
%define         python_version    %(echo %{tarversion} | head -c 3)
%define         idle_name         idle
Requires:       python-base = %{version}
%if %{suse_version} == 1315 && !0%{?is_opensuse}
Recommends:     python-strict-tls-check
%endif
Provides:       %{name} = %{python_version}
Provides:       python2 = %{version}
# To make older versions of this package to conflict with
# shared-python-startup I need a symbol to conflict with
Provides:       python2_split_startup
Obsoletes:      python-elementtree
Obsoletes:      python-nothreads
Obsoletes:      python-sqlite
Obsoletes:      python21
# bug437293
%ifarch ppc64
Obsoletes:      python-64bit
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Python is an interpreted, object-oriented programming language, and is
often compared to Tcl, Perl, Scheme, or Java.  You can find an overview
of Python in the documentation and tutorials included in the python-doc
(HTML) or python-doc-pdf (PDF) packages.

If you want to install third party modules using distutils, you need to
install python-devel package.

%package idle
Summary:        An Integrated Development Environment for Python
Group:          Development/Languages/Python
Requires:       python-base = %{version}
Requires:       python-tk
Provides:       python2-idle = %{version}

%description idle
IDLE is a Tkinter based integrated development environment for Python.
It features a multi-window text editor with multiple undo, Python
colorizing, and many other things, as well as a Python shell window and
a debugger.

%package demo
Summary:        Python Demonstration Scripts
Group:          Development/Languages/Python
Requires:       python-base = %{version}
Provides:       pyth_dmo
Obsoletes:      pyth_dmo
Provides:       python2-demo = %{version}

%description demo
Various demonstrations of what you can do with Python and a number of
programs that are useful for building or extending Python.

%package tk
Summary:        TkInter - Python Tk Interface
Group:          Development/Libraries/Python
Requires:       python-base = %{version}
Provides:       pyth_tk
Provides:       pyth_tkl
Provides:       python-tkinter
Provides:       python_tkinter_lib
#%ifarch %ix86
#Provides:       _tkinter.so
#%endif
Obsoletes:      pyth_tk
Obsoletes:      pyth_tkl
Obsoletes:      python-tkinter
Provides:       python2-tk = %{version}

%description tk
Python interface to Tk. Tk is the GUI toolkit that comes with Tcl.

%package curses
Summary:        Python Interface to the (N)Curses Library
Group:          Development/Libraries/Python
Requires:       python-base = %{version}
Obsoletes:      pyth_cur
Provides:       pyth_cur
Provides:       python2-curses = %{version}

%description curses
An easy to use interface to the (n)curses CUI library. CUI stands for
Console User Interface.

%package gdbm
Summary:        Python Interface to the GDBM Library
Group:          Development/Libraries/Python
Requires:       python-base = %{version}
Obsoletes:      pygdmod
Provides:       pygdmod
Provides:       python2-gdbm = %{version}
# Compat to allow BR on python_module dbm and have it properly
# pull in gdbm on py2 and dbm on py3
Provides:       python-dbm = %{version}
Provides:       python2-dbm = %{version}

%description gdbm
An easy to use interface for GDBM databases. GDBM is the GNU
implementation of the standard Unix DBM databases.

%if %{suse_version} == 1315 && !0%{?is_opensuse}
%package strict-tls-check
Summary:        Enable secure verification of TLS certificates
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Supplements:    %{name}

%description strict-tls-check
When this package is present, Python performs strict verification of
TLS certificates, including hostname check, by default. This is
the preferred secure setting.

It is distributed as a separate package, because this behavior
can cause verification errors in improperly written legacy scripts
that rely on earlier non-verification behavior.
%endif

%prep
%setup -q -n %{tarname}
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

%if %{suse_version} == 1315 && !0%{?is_opensuse}
cp %{SOURCE8} Lib/
%endif

%build
%define _lto_cflags %{nil}
export OPT="%{optflags} -DOPENSSL_LOAD_CONF -fwrapv"

autoreconf -f -i . # Modules/_ctypes/libffi
# prevent make from trying to rebuild asdl stuff, which requires existing
# python installation
touch Parser/asdl* Python/Python-ast.c Include/Python-ast.h

%configure \
    --docdir=%{_docdir}/python \
    --enable-ipv6 \
    --with-fpectl \
    --enable-shared \
    --enable-unicode=ucs4

LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH \
    make %{?_smp_mflags}

%check
# on hppa, the threading of glibc is quite broken. The tests just stop
# at some point, and the machine does not build anything more until a
# timeout several hours later.
%ifnarch hppa
# Limit virtual memory to avoid spurious failures
if test $(ulimit -v) = unlimited || test $(ulimit -v) -gt 10000000; then
  ulimit -v 10000000 || :
fi
LIST="test_urllib test_ssl test_hashlib test_hmac test_unicodedata test_tarfile test_sqlite test_tcl test_dbm test_anydbm test_dumbdbm test_gdbm test_whichdb test_tk test_ttk_textonly test_bsddb test_bsddb3 test_readline"
make test TESTOPTS="-w $LIST" TESTPYTHONOPTS="-R"
%endif

%install
# replace rest of /usr/local/bin/python or /usr/bin/python2.x with /usr/bin/python
find . -name '*.py' -type f | grep -vE "^./Parser/|^./Python/" \
  | xargs grep -lE '^#! *(/usr/.*bin/(env +)?)?python' \
  | xargs sed -r -i -e '1s@^#![[:space:]]*(/usr/(local/)?bin/(env +)?)?python([0-9]+\.[0-9]+)?@#!/usr/bin/python@'
# the grep inbetween makes it much faster
########################################
# install it
########################################
%make_install OPT="%{optflags} -fPIC"
########################################
# some cleanups
########################################
# remove hard links and replace them with symlinks
for dir in bin include %{_lib} ; do
    rm -f %{buildroot}/%{_prefix}/$dir/python
    ln -s python%{python_version} %{buildroot}/%{_prefix}/$dir/python
done
# kill imageop.so, it's insecure
rm -f %{buildroot}/%{_libdir}/python%{python_version}/lib-dynload/imageop.so
#cleanup for -base
rm %{buildroot}%{_bindir}/python%{python_version}
rm %{buildroot}%{_bindir}/python2
rm %{buildroot}%{_bindir}/python
rm %{buildroot}%{_bindir}/smtpd.py
rm %{buildroot}%{_bindir}/pydoc
rm %{buildroot}%{_bindir}/2to3
rm %{buildroot}%{_mandir}/man1/python*
rm %{buildroot}%{_libdir}/libpython*.so.*
rm %{buildroot}%{_libdir}/python
find %{buildroot}%{_libdir}/python%{python_version} -maxdepth 1 \
    ! \( -name "ssl.py*" -o -name "sle_tls_checks_policy.py*" \) \
    -exec rm {} ";"
rm %{buildroot}%{_bindir}/python%{python_version}-config
rm %{buildroot}%{_bindir}/python2-config
rm %{buildroot}%{_bindir}/python-config
rm %{buildroot}%{_libdir}/pkgconfig/*
rm -r %{buildroot}%{_includedir}/python
rm -r %{buildroot}%{_includedir}/python%{python_version}
rm -r %{buildroot}%{_libdir}/python%{python_version}/compiler
rm -r %{buildroot}%{_libdir}/python%{python_version}/config
rm -r %{buildroot}%{_libdir}/python%{python_version}/ctypes
rm -r %{buildroot}%{_libdir}/python%{python_version}/distutils
rm -r %{buildroot}%{_libdir}/python%{python_version}/email
rm -r %{buildroot}%{_libdir}/python%{python_version}/encodings
rm -r %{buildroot}%{_libdir}/python%{python_version}/ensurepip
rm -r %{buildroot}%{_libdir}/python%{python_version}/hotshot
rm -r %{buildroot}%{_libdir}/python%{python_version}/importlib
rm -r %{buildroot}%{_libdir}/python%{python_version}/json
rm -r %{buildroot}%{_libdir}/python%{python_version}/lib2to3
rm -r %{buildroot}%{_libdir}/python%{python_version}/logging
rm -r %{buildroot}%{_libdir}/python%{python_version}/multiprocessing
rm -r %{buildroot}%{_libdir}/python%{python_version}/plat-*
rm -r %{buildroot}%{_libdir}/python%{python_version}/pydoc_data
rm -r %{buildroot}%{_libdir}/python%{python_version}/test
rm -r %{buildroot}%{_libdir}/python%{python_version}/unittest
rm -r %{buildroot}%{_libdir}/python%{python_version}/wsgiref
rm -r %{buildroot}%{_libdir}/python%{python_version}/xml
rm %{buildroot}%{_libdir}/libpython%{python_version}.so
rm %{buildroot}%{_libdir}/python%{python_version}/site-packages/README
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_bisect.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_csv.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_collections.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_ctypes.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_ctypes_test.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_elementtree.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_functools.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_heapq.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_hotshot.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_io.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_json.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_locale.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_lsprof.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_multiprocessing.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_random.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_socket.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_struct.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_testcapi.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/array.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/binascii.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/bz2.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/cPickle.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/cStringIO.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/cmath.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/crypt.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/datetime.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/fcntl.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/future_builtins.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/grp.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/itertools.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/linuxaudiodev.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/math.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/mmap.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/nis.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/operator.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/ossaudiodev.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/parser.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/pyexpat.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/resource.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/select.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/spwd.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/strop.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/syslog.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/termios.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/time.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/unicodedata.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/zlib.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_codecs*.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/_multibytecodec.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/audioop.so
rm -f %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/dl.so
rm %{buildroot}%{_libdir}/python%{python_version}/lib-dynload/Python-%{tarversion}-py%{python_version}.egg-info
# replace duplicate .pyo/.pyc with hardlinks
%fdupes %{buildroot}/%{_libdir}/python%{python_version}
########################################
# documentation
########################################
export PDOCS=%{buildroot}%{_docdir}/%{name}
install -d -m 755 $PDOCS
install -c -m 644 %{SOURCE1}                        $PDOCS/
install -c -m 644 LICENSE                           $PDOCS/
install -c -m 644 README                            $PDOCS/
########################################
# tools and demos
########################################
find Tools/ Demo/ -type d \( -regex ".*/.cvsignore" \) -exec rm -f \{\} \;
for x in `find Tools/ Demo/ \( -not -name Makefile \) -print | sort` ; do
  test -d $x && ( install -c -m 755 -d $PDOCS/$x ) \
             || ( install -c -m 644 $x $PDOCS/$x )
done
########################################
# idle
########################################
# move idle config into /etc
install -d -m755 %{buildroot}%{_sysconfdir}/%{idle_name}
(
    cd %{buildroot}/%{_libdir}/python%{python_version}/idlelib/
    for file in *.def ; do
        mv $file %{buildroot}%{_sysconfdir}/%{idle_name}/
        ln -sf /etc/%{idle_name}/$file  %{buildroot}/%{_libdir}/python%{python_version}/idlelib/
    done
)

# Install .desktop, mime and appdata files from upstream tarball
%if 0%{?suse_version} >= 1500
install -Dm0644 %{SOURCE50} %{buildroot}/%{_datadir}/mime/packages/idle.appdata.xml
%endif
install -D -m 0644 Lib/idlelib/Icons/idle_16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/idle.png
install -D -m 0644 Lib/idlelib/Icons/idle_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/idle.png
install -D -m 0644 Lib/idlelib/Icons/idle_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/idle.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE51}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files idle
%defattr(644, root, root, 755)
%dir %{_sysconfdir}/%{idle_name}
%config %{_sysconfdir}/%{idle_name}/*
%doc Lib/idlelib/NEWS.txt
%doc Lib/idlelib/README.txt
%doc Lib/idlelib/TODO.txt
%doc Lib/idlelib/extend.txt
%doc Lib/idlelib/ChangeLog
%{_libdir}/python%{python_version}/idlelib
%attr(755, root, root) %{_bindir}/%{idle_name}
%if 0%{?suse_version} >= 1500
%{_datadir}/mime/packages/idle.appdata.xml
%endif
%{_datadir}/applications/idle.desktop
%{_datadir}/icons/hicolor/*/apps/idle.png

%files demo
%defattr(644, root, root, 755)
%doc %{_docdir}/%{name}/Demo
%doc %{_docdir}/%{name}/Tools

%files tk
%defattr(644, root, root, 755)
%{_libdir}/python%{python_version}/lib-tk/
%{_libdir}/python%{python_version}/lib-dynload/_tkinter.so

%files curses
%defattr(644, root, root, 755)
%{_libdir}/python%{python_version}/curses
%{_libdir}/python%{python_version}/lib-dynload/_curses.so
%{_libdir}/python%{python_version}/lib-dynload/_curses_panel.so

%files gdbm
%defattr(644, root, root, 755)
%{_libdir}/python%{python_version}/lib-dynload/gdbm.so
%{_libdir}/python%{python_version}/lib-dynload/dbm.so

%if %{suse_version} == 1315 && !0%{?is_opensuse}
%files strict-tls-check
%defattr(644, root, root, 755)
%{_libdir}/python%{python_version}/sle_tls_checks_policy.py*
%endif

%files
%defattr(644, root, root, 755)
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.SUSE
%dir %{_libdir}/python%{python_version}
%{_libdir}/python%{python_version}/ssl.py*
%{_libdir}/python%{python_version}/bsddb
%{_libdir}/python%{python_version}/sqlite3
%dir %{_libdir}/python%{python_version}/lib-dynload
%{_libdir}/python%{python_version}/lib-dynload/_bsddb.so
%{_libdir}/python%{python_version}/lib-dynload/_hashlib.so
%{_libdir}/python%{python_version}/lib-dynload/_sqlite3.so
%{_libdir}/python%{python_version}/lib-dynload/_ssl.so
%{_libdir}/python%{python_version}/lib-dynload/readline.so

%changelog
