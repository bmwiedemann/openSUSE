#
# spec file for package python36-core
#
# Copyright (c) 2021 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%define psuffix -documentation
%bcond_without doc
%bcond_with base
%bcond_with general
%endif
%if "%{flavor}" == "base"
%define psuffix -core
%bcond_with doc
%bcond_without base
%bcond_with general
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with doc
%bcond_with base
%bcond_without general
%endif
%define _version %(c=%{version}; echo ${c/[a-z]*/})
%define tar_suffix %(c=%{_version}; echo ${c#%{_version}})
%define python_version %(c=%{_version}; echo ${c:0:3})
# based on the current source tarball
%define python_version_abitag %(c=%{python_version}; echo ${c//./})
# FIXME %%define python_version_soname %%(c=%%{python_version}; echo ${c//./_})
%define         python_version_soname   3_6
%if 0%(test -n "%{tar_suffix}" && echo 1)
%define _version %(echo "%{_version}~%{tar_suffix}")
%define tarversion %{version}
%else
%define tarversion %{version}
%endif
%define         python_pkg_name python36
# Will provide the python3-* provides
# Will do the /usr/bin/python3 and all the core links
%define         primary_interpreter 0
%define         folderversion %{tarversion}
%define         tarname    Python-%{tarversion}
%define         sitedir         %{_libdir}/python%{python_version}
# three possible ABI kinds: m - pymalloc, d - debug build; see PEP 3149
%define         abi_kind   m
# python ABI version - used in some file names
%define         python_abi %{python_version}%{abi_kind}
# soname ABI tag defined in PEP 3149
%define         abi_tag    %{python_version_abitag}%{abi_kind}
# version part of "libpython" package
%define         so_major 1
%define         so_minor 0
%define         so_version %{python_version_soname}%{abi_kind}%{so_major}_%{so_minor}
# rpm and python have different ideas about what is an arch-dependent name, so:
%if "%{__isa_name}" == "ppc"
%define archname %(echo %{_arch} | sed s/ppc/powerpc/)
%else
%define archname %{_arch}
%endif
# our arm has Hardware-Floatingpoint
%if "%{_arch}" == "arm"
%define armsuffix hf
%endif
# pyexpat.cpython-35m-x86_64-linux-gnu
# pyexpat.cpython-35m-powerpc64le-linux-gnu
# pyexpat.cpython-35m-armv7-linux-gnueabihf
# _md5.cpython-36m-x86_64-linux-gnu.so
%define dynlib() %{sitedir}/lib-dynload/%{1}.cpython-%{abi_tag}-%{archname}-%{_os}%{?_gnu}%{?armsuffix}.so
# deadlocks on test_faulthandler and blocks the build
%if 0%{?qemu_user_space_build}
%bcond_with profileopt
%else
%bcond_with profileopt
%endif
Name:           %{python_pkg_name}%{psuffix}
Version:        3.6.13
Release:        0
Summary:        Python 3 Interpreter
License:        Python-2.0
URL:            https://www.python.org/
Source0:        http://www.python.org/ftp/python/%{folderversion}/%{tarname}.tar.xz
Source1:        http://www.python.org/ftp/python/%{folderversion}/%{tarname}.tar.xz.asc
Source2:        baselibs.conf
Source3:        README.SUSE
Source7:        macros.python3
Source8:        import_failed.py
Source9:        import_failed.map
Source11:       skipped_tests.py
Source12:       idle3.desktop
Source13:       idle3.appdata.xml
# Fixed bundled wheels
Source20:       setuptools-44.1.1-py2.py3-none-any.whl
Source21:       pip-20.2.3-py2.py3-none-any.whl
# The following files are not used in the build.
# They are listed here to work around missing functionality in rpmbuild,
# which would otherwise exclude them from distributed src.rpm files.
Source99:       https://www.python.org/static/files/pubkeys.txt#/python.keyring
Source100:      PACKAGING-NOTES
# implement "--record-rpm" option for distutils installations
Patch01:        Python-3.0b1-record-rpm.patch
# support lib-vs-lib64 distinction
Patch02:        python-3.6.0-multilib-new.patch
# support finding packages in /usr/local, install to /usr/local by default
Patch04:        python-3.3.0b1-localpath.patch
# PATCH-FEATURE-UPSTREAM pep538_coerce_legacy_c_locale.patch bpo#28180 mcepl@suse.com
# This patches coerces locale to be C.UTF-8 irrespective to the system locale
Patch05:        pep538_coerce_legacy_c_locale.patch
# replace DATE, TIME and COMPILER by fixed definitions to aid reproducible builds
Patch06:        python-3.3.0b1-fix_date_time_compiler.patch
# fix wrong include path in curses-panel module
Patch07:        python-3.3.0b1-curses-panel.patch
# POSIX_FADV_WILLNEED throws EINVAL. Use a different constant in test
Patch09:        python-3.3.0b1-test-posix_fadvise.patch
# Disable global and distutils sysconfig comparison test, we deviate from the default depending on optflags
Patch12:        python-3.3.3-skip-distutils-test_sysconfig_module.patch
# Raise timeout value for test_subprocess
Patch15:        subprocess-raise-timeout.patch
# PATCH-FIX-UPSTREAM python-3.6-CVE-2017-18207.patch psimons@suse.com -- Add check for channels of wav file in Lib/wave.py
# Suggested in https://github.com/python/cpython/pull/4437.
Patch20:        python-3.6-CVE-2017-18207.patch
# PATCH-FIX-UPSTREAM bmwiedemann@suse.de -- https://github.com/python/cpython/pull/296
Patch21:        0001-allow-for-reproducible-builds-of-python-packages.patch
# PATCH-FEATURE-OPENSUSE order files for compilation until the underlying cause of bsc#1049186 is resolved
Patch22:        distutils-reproducible-compile.patch
# skip some tests only for PowerPC
Patch23:        skip_random_failing_tests.patch
# PATCH-FIX-UPSTREAM sorted tar https://github.com/python/cpython/pull/2263
Patch24:        python3-sorted_tar.patch
# PATCH-FIX-UPSTREAM bpo23395-PyErr_SetInterrupt-signal.patch boo#1094814 mcepl@suse.com
# handle situation when the SIGINT signal is ignored or not handled
Patch29:        bpo23395-PyErr_SetInterrupt-signal.patch
# PATCH-FIX-OPENSUSE aarch64-prolong-timeout.patch bsc#1149121 mcepl@suse.com
# Our buildbots are apparently too busy on aarch64 to make time right
Patch30:        aarch64-prolong-timeout.patch
# PATCH-FIX-UPSTREAM bpo-36576-skip_tests_for_OpenSSL-111.patch bsc#1149792 mcepl@suse.com
# Skip tests failing with OpenSSL 1.1.1
Patch32:        bpo-36576-skip_tests_for_OpenSSL-111.patch
# PATCH-FIX-OPENSUSE bpo36263-Fix_hashlib_scrypt.patch boo#1151490 mcepl@suse.com
# There is a regression in OpenSSL, which causes bpo#36263, and until it
# is fixed in OpenSSL, we need to protect against it.
Patch33:        bpo36263-Fix_hashlib_scrypt.patch
# PATCH-FIX-UPSTREAM CVE-2019-9674-zip-bomb.patch bsc#1162825 mcepl@suse.com
# Improve documentation warning against the possible zip bombs
Patch35:        CVE-2019-9674-zip-bomb.patch
# PATCH-FIX-UPSTREAM riscv64-support.patch bpo-33377: add triplets for mips-r6 and riscv (#6655)
Patch36:        riscv64-support.patch
# PATCH-FIX-UPSTREAM riscv64-ctypes.patch bpo-35847: RISC-V needs CTYPES_PASS_BY_REF_HACK (GH-11694)
Patch37:        riscv64-ctypes.patch
# PATCH-FIX-UPSTREAM faulthandler._stack_overflow_on_GCC10.patch bpo#38965 mcepl@suse.com
# Fix faulthandler._stack_overflow() on GCC 10
Patch38:        faulthandler_stack_overflow_on_GCC10.patch
# PATCH-FIX-UPSTREAM ignore_pip_deprec_warn.patch mcepl@suse.com
# Ignore deprecation warning for old version of pip
Patch39:        ignore_pip_deprec_warn.patch
# PATCH-FIX-UPSTREAM stop calling removed Sphinx function gh#python/cpython#13236
Patch40:        sphinx-update-removed-function.patch
# PATCH-FIX-UPSTREAM CVE-2021-3426-inf-disclosure-pydoc-getfile.patch bsc#1183374 mcepl@suse.com
# Remove the pydoc getfile feature
Patch41:        CVE-2021-3426-inf-disclosure-pydoc-getfile.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  lzma-devel
BuildRequires:  netcfg
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
#!BuildIgnore:  gdk-pixbuf-loader-rsvg
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libnsl)
BuildRequires:  pkgconfig(libtirpc)
%endif
%if %{with doc}
# Here we just run sphinx and we can use generic one, we don't need
# the flavor variant
BuildRequires:  python3-Sphinx
%endif
%if %{with general}
# required for idle3 (.desktop and .appdata.xml files)
BuildRequires:  appstream-glib
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  gettext
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  timezone
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(x11)
Requires:       %{python_pkg_name}-base = %{version}
Recommends:     %{python_pkg_name}-curses
Recommends:     %{python_pkg_name}-dbm
Recommends:     %{python_pkg_name}-pip
Provides:       python = %{python_version}
%if %{primary_interpreter}
Provides:       python3 = %{python_version}
Obsoletes:      python3 <= %{python_version}
%endif
%endif

%description
Python 3 is modern interpreted, object-oriented programming language,
often compared to Tcl, Perl, Scheme, or Java.  You can find an overview
of Python in the documentation and tutorials included in the python3-doc
package.

This package supplies rich command line features provided by readline,
and sqlite3 support for the interpreter core, thus forming a so called
"extended" runtime.
Installing "python3" is sufficient for the vast majority of usecases.
In addition, recommended packages provide UI toolkit support (python3-curses,
python3-tk), legacy UNIX database bindings (python3-dbm), and the IDLE
development environment (python3-idle).

%package -n %{python_pkg_name}-tk
Summary:        TkInter, a Python Tk Interface
Requires:       %{python_pkg_name} = %{version}
%if %{primary_interpreter}
Provides:       python3-tk = %{version}
Obsoletes:      python3-tk < %{version}
%endif

%description -n %{python_pkg_name}-tk
Python interface to Tk. Tk is the GUI toolkit that comes with Tcl.

%package -n %{python_pkg_name}-curses
Summary:        Python Interface to the (N)Curses Library
Requires:       %{python_pkg_name} = %{version}
%if %{primary_interpreter}
Provides:       python3-curses = %{version}
Obsoletes:      python3-curses < %{version}
%endif

%description -n %{python_pkg_name}-curses
An easy to use interface to the (n)curses CUI library. CUI stands for
Console User Interface.

%package -n %{python_pkg_name}-dbm
Summary:        Python Interface to the GDBM Library
Requires:       %{python_pkg_name} = %{version}
%if %{primary_interpreter}
Provides:       python3-dbm = %{version}
Obsoletes:      python3-dbm < %{version}
%endif

%description -n %{python_pkg_name}-dbm
An easy to use interface for Unix DBM databases, and more specifically,
the GNU implementation GDBM.

%package -n %{python_pkg_name}-idle
Summary:        An Integrated Development Environment for Python
Requires:       %{python_pkg_name} = %{version}
Requires:       %{python_pkg_name}-tk
%if %{primary_interpreter}
Provides:       python3-idle = %{version}
Obsoletes:      python3-idle < %{version}
%endif

%description -n %{python_pkg_name}-idle
IDLE is a Tkinter based integrated development environment for Python.
It features a multi-window text editor with multiple undo, Python
colorizing, and many other things, as well as a Python shell window and
a debugger.

%package -n %{python_pkg_name}-doc
Summary:        Package Documentation for Python 3
Enhances:       %{python_pkg_name} = %{python_version}
%if %{primary_interpreter}
Provides:       python3-doc = %{version}
Obsoletes:      python3-doc < %{version}
%endif

%description -n %{python_pkg_name}-doc
Tutorial, Global Module Index, Language Reference, Library Reference,
Extending and Embedding Reference, Python/C API Reference, Documenting
Python, and Macintosh Module Reference in HTML format.

%package -n %{python_pkg_name}-doc-devhelp
Summary:        Additional Package Documentation for Python 3 in devhelp format
%if %{primary_interpreter}
Provides:       python3-doc-devhelp = %{version}
Obsoletes:      python3-doc-devhelp < %{version}
%endif

%description -n %{python_pkg_name}-doc-devhelp
Tutorial, Global Module Index, Language Reference, Library Reference,
Extending and Embedding Reference, Python/C API Reference, Documenting
Python, and Macintosh Module Reference in format for devhelp.

%package -n %{python_pkg_name}-base
Summary:        Python 3 Interpreter and Stdlib Core
Requires:       libpython%{so_version} = %{version}
Recommends:     %{python_pkg_name} = %{version}
#Recommends:     python3-ensurepip
# python 3.1 didn't have a separate python-base, so it is wrongly
# not a conflict to have python3-3.1 and python3-base > 3.1
Obsoletes:      python3 < 3.2
# no Provides, because python3 is obviously provided by package python3
# python 3.4 provides asyncio
Provides:       %{python_pkg_name}-asyncio = %{version}
# python 3.6 provides typing
Provides:       %{python_pkg_name}-typing = %{version}
# python3-xml was merged into python3, now moved into -base
Provides:       %{python_pkg_name}-xml = %{version}
%if %{primary_interpreter}
Provides:       python3-asyncio = %{version}
Provides:       python3-base = %{version}
Obsoletes:      python3-asyncio < %{version}
Obsoletes:      python3-base < %{version}
Provides:       python3-typing = %{version}
Obsoletes:      python3-typing < %{version}
Provides:       python3-xml = %{version}
Obsoletes:      python3-xml < %{version}
%endif

%description -n %{python_pkg_name}-base
Python is an interpreted, object-oriented programming language, and is
often compared to Tcl, Perl, Scheme, or Java.  You can find an overview
of Python in the documentation and tutorials included in the python-doc
package.

This package contains the interpreter core and most commonly used modules
from the standard library. This is sufficient for many usecases, but it
excludes components that depend on external libraries, most notably XML,
database and UI toolkits support.

%package -n %{python_pkg_name}-tools
Summary:        Python Utility and Demonstration Scripts
Requires:       %{python_pkg_name}-base = %{version}
Provides:       %{python_pkg_name}-2to3 = %{version}
Provides:       %{python_pkg_name}-demo = %{version}
%if %{primary_interpreter}
Provides:       python3-2to3 = %{version}
Provides:       python3-demo = %{version}
Provides:       python3-tools = %{version}
Obsoletes:      python3-2to3 < %{version}
Obsoletes:      python3-demo < %{version}
Obsoletes:      python3-tools < %{version}
%endif

%description -n %{python_pkg_name}-tools
A number of scripts that are useful for building, testing or extending Python,
and a set of demonstration programs.

%package -n %{python_pkg_name}-devel
Summary:        Include Files and Libraries Mandatory for Building Python Modules
Requires:       %{python_pkg_name}-base = %{version}
%if %{primary_interpreter}
Provides:       python3-devel = %{version}
Obsoletes:      python3-devel < %{version}
%endif

%description -n %{python_pkg_name}-devel
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.

This package contains header files, a static library, and development
tools for building Python modules, extending the Python interpreter or
embedding Python in applications.

This also includes the Python distutils, which were in the Python
package up to version 2.2.2.

%package -n %{python_pkg_name}-testsuite
Summary:        Unit tests for Python and its standard library
Requires:       %{python_pkg_name} = %{version}
Requires:       %{python_pkg_name}-tk = %{version}
%if %{primary_interpreter}
Provides:       python3-testsuite = %{version}
Obsoletes:      python3-testsuite < %{version}
%endif

%description -n %{python_pkg_name}-testsuite
Unit tests that are useful for verifying integrity and functionality
of the installed Python interpreter and standard library.
They are a documented part of stdlib, as a module 'test'.

%package -n libpython%{so_version}
Summary:        Python Interpreter shared library
Requires:       %{python_pkg_name}-base >= %{version}

%description -n libpython%{so_version}
Python is an interpreted, object-oriented programming language, and is
often compared to Tcl, Perl, Scheme, or Java.  You can find an overview
of Python in the documentation and tutorials included in the python-doc
(HTML) or python-doc-pdf (PDF) packages.

This package contains libpython3.2 shared library for embedding in
other applications.

%prep
%setup -q -n %{tarname}
%patch01 -p1
%patch02 -p1
%patch04
%patch05 -p1
%patch06 -p1
%patch07
%patch09 -p1
%patch12 -p1
%patch15 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%ifarch ppc ppc64 ppc64le
%patch23 -p1
%endif
%patch24 -p1
%patch29 -p1
%patch30 -p1
%patch32 -p1
%patch33 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1

# drop Autoconf version requirement
sed -i 's/^AC_PREREQ/dnl AC_PREREQ/' configure.ac

# fix shebangs - convert /usr/local/bin/python and /usr/bin/env/python to /usr/bin/python3
for dir in Lib Tools; do
    # find *.py, filter to files that contain bad shebangs
    # break up "/""usr" like this to prevent replacing with %%{_prefix}
    find $dir -name '*.py' -type f -print0 \
        | xargs -0 grep -lE '^#! *(/''usr/.*bin/(env +)?)?python' \
        | xargs sed -r -i -e '1s@^#![[:space:]]*(/''usr/(local/)?bin/(env +)?)?python([0-9]+(\.[0-9]+)?)?@#!%{_bindir}/python3@'
done

# drop in-tree libffi and expat
rm -r Modules/_ctypes/libffi* Modules/_ctypes/darwin
rm -r Modules/expat

# drop duplicate README from site-packages
rm Lib/site-packages/README.txt

# Replace bundled wheels with the updates ones
rm -v Lib/ensurepip/_bundled/*.whl
cp -v %{SOURCE20} %{SOURCE21} Lib/ensurepip/_bundled/
STVER=$(basename %{SOURCE20}|cut -d- -f2)
PIPVER=$(basename %{SOURCE21}|cut -d- -f2)
sed -E -i -e "s/^(\s*_SETUPTOOLS_VERSION\s+=\s+)\"[0-9.]+\"/\1\"${STVER}\"/" \
          -e "s/^(\s*_PIP_VERSION\s+=\s+)\"[0-9.]+\"/\1\"${PIPVER}\"/" \
    Lib/ensurepip/__init__.py

%build
%if %{with doc}
TODAY_DATE=`date -r %{SOURCE0} "+%%B %%d, %%Y"`
# TODO use not date of tarball but date of latest patch

cd Doc
sed -i "s/^today = .*/today = '$TODAY_DATE'/" conf.py
%make_build -j1 html

# Build also devhelp files
sphinx-build -a -b devhelp . build/devhelp
rm -rfv build/devhelp/.doctrees
%else
%define _lto_cflags %{nil}
# use rpm_opt_flags
%if 0%{?suse_version} < 1500
export OPT="%{optflags} -DOPENSSL_LOAD_CONF -fwrapv $(pkg-config --cflags-only-I libffi)"
%else
export OPT="%{optflags} -DOPENSSL_LOAD_CONF -fwrapv $(pkg-config --cflags-only-I libffi) -fno-semantic-interposition"
%endif

touch -r %{SOURCE0} Makefile.pre.in

autoreconf -fvi

%if 0%{?sles_version}
sed -e 's/-fprofile-correction//' -i Makefile.pre.in
%endif

%configure \
    --docdir=%{_docdir}/python \
    --enable-ipv6 \
    --enable-shared \
    --with-fpectl \
    --with-ensurepip=no \
    --with-system-ffi \
    --with-system-expat \
    --without-lto \
%if %{with profileopt}
    --enable-optimizations \
%endif
    --enable-loadable-sqlite-extensions

# prevent make from trying to rebuild PYTHON_FOR_GEN stuff
%make_build -t Python/Python-ast.c \
        Include/Python-ast.h \
        Objects/typeslots.inc \
        Python/opcode_targets.h \
        Include/opcode.h

%if %{with general}
%make_build
%endif
%if %{with base}
%if %{with profileopt}
    target=profile-opt
%else
    target=all
%endif
LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH \
    %make_build $target
%endif
%endif

%check
%if %{with general}
# exclude test_gdb -- it doesn't run in buildservice anyway, and fails on missing debuginfos
# when you install gdb into your test env
EXCLUDE="test_gdb"
# we patch out the message to recommend zypper in and thus this would fail
EXCLUDE="$EXCLUDE test_pydoc"

%ifarch %{arm} s390x
# test_multiprocessing_forkserver is racy
EXCLUDE="$EXCLUDE test_multiprocessing_forkserver"
%endif
%ifarch ppc ppc64 ppc64le
# exclue test_faulthandler due to bnc#831629
EXCLUDE="$EXCLUDE test_faulthandler"
%endif
# some tests break in QEMU
%if 0%{?qemu_user_space_build}
EXCLUDE="$EXCLUDE test_multiprocessing_forkserver test_multiprocessing_spawn test_posix test_os test_socket"
# qemu bug (siginterrupt handling)
EXCLUDE="$EXCLUDE test_signal"
%endif

# This test (part of test_uuid) requires real network interfaces
# so that ifconfig output has "HWaddr <something>".  Some kvm instances
# done have any such interface breaking the uuid module.
EXCLUDE="$EXCLUDE test_uuid"

# TEMPORARILY EXCLUDE test_capi bpo#37169
EXCLUDE="$EXCLUDE test_capi"

# Limit virtual memory to avoid spurious failures
if test $(ulimit -v) = unlimited || test $(ulimit -v) -gt 10000000; then
  ulimit -v 10000000 || :
fi

export PYTHONPATH="$(pwd -P)/Lib"
# Use timeout, like make target buildbottest
# We cannot run tests parallel, because osc build environment doesn’t
# have /dev/shm
%make_build -j1 test TESTOPTS="-u curses -v -x $EXCLUDE --timeout=3000"
# use network, be verbose:
#make test TESTOPTS="-l -u network -v"
%endif

%install
%if %{with doc}
export PDOCS=%{buildroot}%{_docdir}/python%{python_version}
mkdir -p $PDOCS
# generated docs
rm Doc/build/*/.buildinfo
cp -r Doc/build/html $PDOCS
# misc
install -d -m 755 $PDOCS/Misc
rm Misc/README.AIX
for i in Misc/* ; do
  [ -f $i ] && install -c -m 644 $i $PDOCS/Misc/
done
# devhelp
mkdir -p %{buildroot}%{_datadir}/gtk-doc/html
cp -r Doc/build/devhelp %{buildroot}%{_datadir}/gtk-doc/html/Python%{python_version}
rm -rf %{buildroot}%{_datadir}/gtk-doc/html/Python%{python_version}/.doctrees
%endif
%if %{with general}
%make_install

# clean out stuff that is in python-base and subpackages

find %{buildroot}%{_bindir} -mindepth 1 -not -name "*idle3*" -print -delete
rm %{buildroot}%{_libdir}/lib*
rm -r %{buildroot}%{_libdir}/pkgconfig
rm -r %{buildroot}%{_mandir}/*
rm -r %{buildroot}%{_includedir}/*

rm -r %{buildroot}%{sitedir}/config*
find %{buildroot}%{sitedir} -name "*.egg-info" -delete
rm -r %{buildroot}%{sitedir}/__pycache__
rm -r %{buildroot}%{sitedir}/site-packages
rm %{buildroot}%{sitedir}/*.*

for module in \
    asyncio ctypes collections concurrent distutils email encodings \
    ensurepip html http \
    importlib json logging multiprocessing pydoc_data unittest \
    urllib venv wsgiref lib2to3 test turtledemo \
    xml xmlrpc
do
    rm -r %{buildroot}%{sitedir}/$module
done

for library in \
    array _asyncio audioop binascii _bisect _bz2 cmath _codecs_* \
    _crypt _csv _ctypes _datetime _decimal fcntl grp \
    _hashlib _heapq _json _lsprof _lzma math mmap _multibytecodec \
    _multiprocessing _opcode ossaudiodev parser _pickle \
    _posixsubprocess _random resource select _ssl _socket spwd \
    _struct syslog termios _testbuffer _testimportmultiple \
    _testmultiphase unicodedata zlib _ctypes_test _testcapi xxlimited \
    _elementtree pyexpat _md5 _sha1 \
    _sha256 _sha512 _blake2 _sha3
do
    eval rm "%{buildroot}%{sitedir}/lib-dynload/$library.*"
done

# Idle is not packaged in base due to the appstream-glib dependency
# move idle config into /etc
install -d -m 755 %{buildroot}%{_sysconfdir}/idle%{python_version}
(
    cd %{buildroot}/%{sitedir}/idlelib/
    for file in *.def ; do
        mv $file %{buildroot}%{_sysconfdir}/idle%{python_version}/
        ln -sf %{_sysconfdir}/idle%{python_version}/$file  %{buildroot}/%{sitedir}/idlelib/
    done
)

# keep just idle3.X
rm %{buildroot}%{_bindir}/idle3

# install idle icons
for size in 16 32 48 ; do
    install -m 644 -D Lib/idlelib/Icons/idle_${size}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/idle%{python_version}.png
done

# install idle desktop file
cp %{SOURCE12} idle%{python_version}.desktop
sed -i -e 's:idle3:idle%{python_version}:g' idle%{python_version}.desktop
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 -D -t %{buildroot}%{_datadir}/applications idle%{python_version}.desktop
%suse_update_desktop_file idle%{python_version}

cp %{SOURCE13} idle%{python_version}.appdata.xml
sed -i -e 's:idle3.desktop:idle%{python_version}.desktop:g' idle%{python_version}.appdata.xml
mkdir -p %{buildroot}%{_datadir}/metainfo
install -m 644 -D -t %{buildroot}%{_datadir}/metainfo idle%{python_version}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/idle%{python_version}.appdata.xml

%fdupes %{buildroot}/%{_libdir}/python%{python_version}
%endif
%if %{with base}
%make_install

# remove .a
find %{buildroot} -name "*.a" -delete

# install "site-packages" and __pycache__ for third parties
install -d -m 755 %{buildroot}%{sitedir}/site-packages
install -d -m 755 %{buildroot}%{sitedir}/site-packages/__pycache__
# and their 32bit counterparts explicitly
mkdir -p %{buildroot}%{_prefix}/lib/python%{python_version}/site-packages/__pycache__

# cleanup parts that don't belong
for dir in curses dbm sqlite3 tkinter idlelib; do
    find "%{buildroot}/%{sitedir}/$dir"/* -maxdepth 0 -name "test" -o -exec rm -rf {} +
done
rm -fv %{buildroot}%{dynlib nis}

# overwrite the copied binary with a link
ln -sf python%{python_version} %{buildroot}%{_bindir}/python3

# decide to ship python3 or just python3.X
%if !%{primary_interpreter}
# base
rm %{buildroot}%{_bindir}/python3
rm %{buildroot}%{_bindir}/pydoc3
rm %{buildroot}%{_bindir}/pyvenv
rm %{buildroot}%{_mandir}/man1/python3.1
# devel
rm %{buildroot}%{_bindir}/python3-config
rm %{buildroot}%{_libdir}/libpython3.so
rm %{buildroot}%{_libdir}/pkgconfig/python3.pc
%endif

# link shared library instead of static library that tools expect
ln -s ../../libpython%{python_abi}.so %{buildroot}%{_libdir}/python%{python_version}/config-%{python_abi}-%{archname}-%{_os}%{?_gnu}%{?armsuffix}/libpython%{python_abi}.so

# delete idle3, which has to many packaging dependencies for base
rm %{buildroot}%{_bindir}/idle3*

# delete the generic 2to3 binary if we are not primary
%if !%{primary_interpreter}
rm %{buildroot}%{_bindir}/2to3
%endif

# replace duplicate .pyo/.pyc with hardlinks
%fdupes %{buildroot}/%{sitedir}

# documentation
export PDOCS=%{buildroot}%{_docdir}/%{name}
install -d -m 755 $PDOCS
install -c -m 644 %{SOURCE3} $PDOCS/
install -c -m 644 README.rst $PDOCS/

# tools
for x in `find Tools/ \( -not -name Makefile \) -print | sort` ; do
  test -d $x && ( install -c -m 755 -d $PDOCS/$x ) \
             || ( install -c -m 644 $x $PDOCS/$x )
done
# gdb script is shipped with devel subpackage
rm -r $PDOCS/Tools/gdb
# clean up the bat files
find "$PDOCS" -name "*.bat" -delete

# put gdb helper script into place
install -m 755 -D Tools/gdb/libpython.py %{buildroot}%{_datadir}/gdb/auto-load/%{_libdir}/libpython%{python_abi}.so.%{so_major}.%{so_minor}-gdb.py

# install devel files to /config
#cp Makefile Makefile.pre.in Makefile.pre $RPM_BUILD_ROOT%{sitedir}/config-%{python_abi}/

# RPM macros
%if %{primary_interpreter}
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -m 644 %{SOURCE7} %{buildroot}%{_rpmconfigdir}/macros.d/ # macros.python3
%endif

# import_failed hooks
FAILDIR=%{buildroot}/%{sitedir}/_import_failed
mkdir $FAILDIR
install -m 644 %{SOURCE8} %{SOURCE9} $FAILDIR # import_failed.*
LD_LIBRARY_PATH=. ./python -c "from py_compile import compile; compile('$FAILDIR/import_failed.py', dfile='%{sitedir}/_import_failed/import_failed.py')"
LD_LIBRARY_PATH=. ./python -O -c "from py_compile import compile; compile('$FAILDIR/import_failed.py', dfile='%{sitedir}/_import_failed/import_failed.py')"
(
    cd $FAILDIR
    while read package modules; do
        for module in $modules; do
            ln import_failed.py $module.py
            pushd __pycache__
            for i in import_failed*; do
                ln $i "$module${i#import_failed}"
            done
            popd
        done
    done < %{SOURCE9}
)
echo %{sitedir}/_import_failed > %{buildroot}/%{sitedir}/site-packages/zzzz-import-failed-hooks.pth
%endif

%if %{with general}
%files -n %{python_pkg_name}-tk
%defattr(644, root, root, 755)
%{sitedir}/tkinter
%exclude %{sitedir}/tkinter/test
%{dynlib _tkinter}

%files -n %{python_pkg_name}-curses
%defattr(644, root, root, 755)
%{sitedir}/curses
%{dynlib _curses}
%{dynlib _curses_panel}

%files -n %{python_pkg_name}-dbm
%defattr(644, root, root, 755)
%{sitedir}/dbm
%{dynlib _dbm}
%{dynlib _gdbm}

%files -n %{python_pkg_name}
%defattr(644, root, root, 755)
%dir %{sitedir}
%dir %{sitedir}/lib-dynload
%{sitedir}/sqlite3
%exclude %{sitedir}/sqlite3/test
%{dynlib readline}
%{dynlib _sqlite3}
%{dynlib nis}

%files -n %{python_pkg_name}-idle
%defattr(644, root, root, 755)
%{sitedir}/idlelib
%dir %{_sysconfdir}/idle%{python_version}
%config %{_sysconfdir}/idle%{python_version}/*
%doc Lib/idlelib/NEWS.txt
%doc Lib/idlelib/README.txt
%doc Lib/idlelib/TODO.txt
%doc Lib/idlelib/extend.txt
%doc Lib/idlelib/ChangeLog
%{_bindir}/idle%{python_version}
%{_datadir}/applications/idle%{python_version}.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/idle%{python_version}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/idle%{python_version}.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/*/apps
%attr(755, root, root) %{_bindir}/idle%{python_version}
# endif for if general
%endif

%if %{with doc}
%files -n %{python_pkg_name}-doc
%dir %{_docdir}/python%{python_version}
%doc %{_docdir}/python%{python_version}/Misc
%doc %{_docdir}/python%{python_version}/html

%files -n %{python_pkg_name}-doc-devhelp
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/Python%{python_version}
%endif

%if %{with base}
%post -n libpython%{so_version} -p /sbin/ldconfig
%postun -n libpython%{so_version} -p /sbin/ldconfig

%files -n libpython%{so_version}
%defattr(644, root,root)
%{_libdir}/libpython%{python_abi}.so.%{so_major}.%{so_minor}

%files -n %{python_pkg_name}-tools
%defattr(644, root, root, 755)
%{sitedir}/turtledemo
%if %{primary_interpreter}
%{_bindir}/2to3
%endif
%attr(755, root, root)%{_bindir}/2to3-%{python_version}
%doc %{_docdir}/%{name}/Tools

%files -n %{python_pkg_name}-devel
%defattr(644, root, root, 755)
%{_libdir}/libpython%{python_abi}.so
%if %{primary_interpreter}
%{_libdir}/libpython3.so
%endif
%{_libdir}/pkgconfig/*
%{_includedir}/python%{python_abi}
%{sitedir}/config-%{python_abi}-*
%defattr(755, root, root)
%{_bindir}/python%{python_abi}-config
%{_bindir}/python%{python_version}-config
%if %{primary_interpreter}
%{_bindir}/python3-config
%endif
# Own these directories to not depend on gdb
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load%{_libdir}
%{_datadir}/gdb/auto-load/%{_libdir}/libpython%{python_abi}.so.%{so_major}.%{so_minor}-gdb.py

%files -n %{python_pkg_name}-testsuite
%defattr(644, root, root, 755)
%{sitedir}/test
%{sitedir}/*/test
%{sitedir}/*/tests
%{dynlib _ctypes_test}
%{dynlib _testbuffer}
%{dynlib _testcapi}
%{dynlib _testimportmultiple}
%{dynlib _testmultiphase}
%{dynlib xxlimited}
# workaround for missing packages
%dir %{sitedir}/sqlite3
%dir %{sitedir}/tkinter

%files -n %{python_pkg_name}-base
%defattr(644, root, root, 755)
# docs
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.rst
%license LICENSE
%doc %{_docdir}/%{name}/README.SUSE
%if %{primary_interpreter}
%{_mandir}/man1/python3.1%{?ext_man}
%endif
%{_mandir}/man1/python%{python_version}.1%{?ext_man}
# license text, not a doc because the code can use it at run-time
%{sitedir}/LICENSE.txt
# RPM macros
%if %{primary_interpreter}
%{_rpmconfigdir}/macros.d/macros.python3
%endif
# binary parts
%dir %{sitedir}/lib-dynload
%{dynlib array}
%{dynlib _asyncio}
%{dynlib audioop}
%{dynlib binascii}
%{dynlib _bisect}
%{dynlib _bz2}
%{dynlib cmath}
%{dynlib _codecs_cn}
%{dynlib _codecs_hk}
%{dynlib _codecs_iso2022}
%{dynlib _codecs_jp}
%{dynlib _codecs_kr}
%{dynlib _codecs_tw}
%{dynlib _crypt}
%{dynlib _csv}
%{dynlib _ctypes}
%{dynlib _datetime}
%{dynlib _decimal}
%{dynlib _elementtree}
%{dynlib fcntl}
%{dynlib grp}
%{dynlib _hashlib}
%{dynlib _heapq}
%{dynlib _json}
%{dynlib _lsprof}
%{dynlib _lzma}
%{dynlib math}
%{dynlib mmap}
%{dynlib _multibytecodec}
%{dynlib _multiprocessing}
%{dynlib _opcode}
%{dynlib ossaudiodev}
%{dynlib parser}
%{dynlib _pickle}
%{dynlib _posixsubprocess}
%{dynlib pyexpat}
%{dynlib _random}
%{dynlib resource}
%{dynlib select}
%{dynlib _socket}
%{dynlib spwd}
%{dynlib _ssl}
%{dynlib _struct}
%{dynlib syslog}
%{dynlib termios}
%{dynlib unicodedata}
%{dynlib zlib}
# hashlib fallback modules
%{dynlib _blake2}
%{dynlib _md5}
%{dynlib _sha1}
%{dynlib _sha256}
%{dynlib _sha512}
%{dynlib _sha3}
# python parts
%dir %{_prefix}/lib/python%{python_version}
%dir %{_prefix}/lib/python%{python_version}/site-packages
%dir %{_prefix}/lib/python%{python_version}/site-packages/__pycache__
%dir %{sitedir}
%dir %{sitedir}/site-packages
%dir %{sitedir}/site-packages/__pycache__
%exclude %{sitedir}/*/test
%exclude %{sitedir}/*/tests
%{sitedir}/*.py
%{sitedir}/asyncio
%{sitedir}/ctypes
%{sitedir}/collections
%{sitedir}/concurrent
%{sitedir}/distutils
%{sitedir}/email
%{sitedir}/encodings
%{sitedir}/ensurepip
%{sitedir}/html
%{sitedir}/http
%{sitedir}/importlib
%{sitedir}/json
%{sitedir}/lib2to3
%{sitedir}/logging
%{sitedir}/multiprocessing
%{sitedir}/pydoc_data
%{sitedir}/unittest
%{sitedir}/urllib
%{sitedir}/venv
%{sitedir}/wsgiref
%{sitedir}/xml
%{sitedir}/xmlrpc
%{sitedir}/__pycache__
# import-failed hooks
%{sitedir}/_import_failed
%{sitedir}/site-packages/zzzz-import-failed-hooks.pth
# symlinks
%if %{primary_interpreter}
%{_bindir}/python3
%{_bindir}/pydoc3
%{_bindir}/pyvenv
%endif
# executables
%attr(755, root, root) %{_bindir}/pydoc%{python_version}
%attr(755, root, root) %{_bindir}/python%{python_abi}
%attr(755, root, root) %{_bindir}/python%{python_version}
%attr(755, root, root) %{_bindir}/pyvenv-%{python_version}
# endif for if base
%endif

%changelog
