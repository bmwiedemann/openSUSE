#
# spec file for package python310
#
# Copyright (c) 2025 SUSE LLC
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

%if 0%{?do_profiling} && !0%{?want_reproducible_builds}
%bcond_without profileopt
%else
%bcond_with profileopt
%endif

%define         python_pkg_name python310
%if "%{python_pkg_name}" == "%{primary_python}"
%define primary_interpreter 1
%else
%define primary_interpreter 0
%endif

%if 0%{?sle_version} && 0%{?suse_version} < 1550
# Obsoleting previous "latest" Python versions
# Next versions will get more lines like for older versions
%define obsolete_python_versioned() \
Obsoletes:      python39%{?1:-%{1}}
%else
%define obsolete_python_versioned() %{nil}
%endif

# Setting up variables
%define _version %(c=%{version}; echo ${c/[a-z]*/})
%define tar_suffix %(c=%{_version}; echo ${c#%{_version}})
%define python_version %(echo %{_version}|cut -d. -f1-2)
# based on the current source tarball
%define python_version_abitag %(c=%{python_version}; echo ${c//./})
# FIXME %%define python_version_soname %%(c=%%{python_version}; echo ${c//./_})
%define         python_version_soname   3_10
%if 0%(test -n "%{tar_suffix}" && echo 1)
%define _version %(echo "%{_version}~%{tar_suffix}")
%define tarversion %{version}
%else
%define tarversion %{version}
%endif
# We don't process beta signs well
%define         folderversion %{tarversion}
%define         tarname    Python-%{tarversion}
%define         sitedir         %{_libdir}/python%{python_version}
# three possible ABI kinds: m - pymalloc, d - debug build; see PEP 3149
%define         abi_kind   %{nil}
# python ABI version - used in some file names
%define         python_abi %{python_version}%{abi_kind}
# soname ABI tag defined in PEP 3149
%define         abi_tag    %{python_version_abitag}%{abi_kind}
# version part of "libpython" package
%define         so_major 1
%define         so_minor 0
%define         so_version %{python_version_soname}%{abi_kind}-%{so_major}_%{so_minor}
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
# Decide whether we want to use mpdecimal
%if 0%{?suse_version} >= 1550
%bcond_without mpdecimal
%else
%bcond_with mpdecimal
%endif
# pyexpat.cpython-35m-x86_64-linux-gnu
# pyexpat.cpython-35m-powerpc64le-linux-gnu
# pyexpat.cpython-35m-armv7-linux-gnueabihf
# _md5.cpython-38m-x86_64-linux-gnu.so
%define dynlib() %{sitedir}/lib-dynload/%{1}.cpython-%{abi_tag}-%{archname}-%{_os}%{?_gnu}%{?armsuffix}.so
Name:           %{python_pkg_name}%{psuffix}
Version:        3.10.18
Release:        0
Summary:        Python 3 Interpreter
License:        Python-2.0
URL:            https://www.python.org/
Source0:        https://www.python.org/ftp/python/%{folderversion}/%{tarname}.tar.xz
Source1:        https://www.python.org/ftp/python/%{folderversion}/%{tarname}.tar.xz.sigstore
Source2:        baselibs.conf
Source3:        README.SUSE
Source7:        macros.python3
Source8:        import_failed.py
Source9:        import_failed.map
Source10:       pre_checkin.sh
Source11:       skipped_tests.py
Source19:       idle3.desktop
Source20:       idle3.appdata.xml
# content of bluez-devel:
# 1. sudo zypper --pkg-cache-dir /tmp install -f -d --no-recommends bluez-devel
# 2. rpm2cpio /tmp/*/*/bluez-devel-*.rpm|cpio -idu
# 3. mkdir Vendor && mv usr/include/* Vendor/
# 4. tar cJf bluez-devel-vendor.tar.xz Vendor/
Source21:       bluez-devel-vendor.tar.xz
Source98:       python310-rpmlintrc
# Tarball is signed by the GPG key of Pablo Galindo Salgado (0x64E628F8D684696D)
# https://keybase.io/pablogsal/pgp_keys.asc?fingerprint=a035c8c19219ba821ecea86b64e628f8d684696d
Source99:       python.keyring
# The following files are not used in the build.
# They are listed here to work around missing functionality in rpmbuild,
# which would otherwise exclude them from distributed src.rpm files.
Source100:      PACKAGING-NOTES
# PATCH-FEATURE-UPSTREAM F00251-change-user-install-location.patch bsc#[0-9]+ mcepl@suse.com
# Fix installation in /usr/local (boo#1071941), originally from Fedora
# https://src.fedoraproject.org/rpms/python3/blob/master/f/00251-change-user-install-location.patch
# Set values of prefix and exec_prefix in distutils install command
# to /usr/local if executable is /usr/bin/python* and RPM build
# is not detected to make pip and distutils install into separate location
Patch01:        F00251-change-user-install-location.patch
# PATCH-FEATURE-UPSTREAM distutils-reproducible-compile.patch gh#python/cpython#8057 mcepl@suse.com
# Improve reproduceability
Patch02:        distutils-reproducible-compile.patch
# support finding packages in /usr/local, install to /usr/local by default
Patch03:        python-3.3.0b1-localpath.patch
# replace DATE, TIME and COMPILER by fixed definitions to aid reproducible builds
Patch04:        python-3.3.0b1-fix_date_time_compiler.patch
# Raise timeout value for test_subprocess
Patch06:        subprocess-raise-timeout.patch
# PATCH-FEATURE-UPSTREAM bpo-31046_ensurepip_honours_prefix.patch bpo#31046 mcepl@suse.com
# ensurepip should honour the value of $(prefix)
Patch07:        bpo-31046_ensurepip_honours_prefix.patch
# PATCH-FIX-SLE no-skipif-doctests.patch jsc#SLE-13738 mcepl@suse.com
# SLE-15 version of Sphinx doesn't know about skipif directive in doctests.
Patch11:        no-skipif-doctests.patch

# PATCH-FIX-SLE skip-test_pyobject_freed_is_freed.patch mcepl@suse.com
# skip a test failing on SLE-15
Patch15:        skip-test_pyobject_freed_is_freed.patch
# PATCH-FIX-SLE fix_configure_rst.patch bpo#43774 mcepl@suse.com
# remove duplicate link targets and make documentation with old Sphinx in SLE
Patch16:        fix_configure_rst.patch
# PATCH-FIX-UPSTREAM bpo-46811 gh#python/cpython#7da97f61816f mcepl@suse.com
# NOTE: SUSE version of expat 2.4.4 is patched in SUSE for CVE-2022-25236
Patch17:        support-expat-CVE-2022-25236-patched.patch
# PATCH-FIX-UPSTREAM bpo-37596-make-set-marshalling.patch bsc#1211765 mcepl@suse.com
# Make `set` and `frozenset` marshalling deterministic
Patch18:        bpo-37596-make-set-marshalling.patch
# PATCH-FIX-UPSTREAM gh-78214-marshal_stabilize_FLAG_REF.patch bsc#1213463 mcepl@suse.com
# marshal: Stabilize FLAG_REF usage
Patch19:        gh-78214-marshal_stabilize_FLAG_REF.patch
# PATCH-FIX-UPSTREAM fix-sphinx-72.patch gh#python/cpython#97950
# This is a patch with a lot of PR combined to make the doc work with
# sphinx 7.2
# This patch has the following github pull requests:
# * gh#python/cpython#104151
# * gh#python/cpython#104154
# * gh#python/cpython#104155
# * gh#python/cpython#104157
# * gh#python/cpython#104159
# * gh#python/cpython#104161
# * gh#python/cpython#104163
# * gh#python/cpython#104221
# * gh#python/cpython#107246
Patch21:        sphinx-72.patch
# PATCH-FIX-UPSTREAM CVE-2023-52425-libexpat-2.6.0-backport.patch gh#python/cpython#117187 mcepl@suse.com
# Make the test suite work with libexpat < 2.6.0
Patch22:        CVE-2023-52425-libexpat-2.6.0-backport.patch
# PATCH-FIX-UPSTREAM bso1227999-reproducible-builds.patch bsc#1227999 mcepl@suse.com
# reproducibility patches
Patch24:        bso1227999-reproducible-builds.patch
# PATCH-FIX-UPSTREAM gh120226-fix-sendfile-test-kernel-610.patch gh#python/cpython#120226 mcepl@suse.com
# Fix test_sendfile_close_peer_in_the_middle_of_receiving on Linux >= 6.10 (GH-120227)
Patch27:        gh120226-fix-sendfile-test-kernel-610.patch
# PATCH-FIX-UPSTREAM sphinx-802.patch mcepl@suse.com
# status_iterator method moved between the Sphinx versions
Patch28:        sphinx-802.patch
# PATCH-FIX-UPSTREAM CVE-2025-6069-quad-complex-HTMLParser.patch bsc#1244705 mcepl@suse.com
# avoid quadratic complexity when processing malformed inputs with HTMLParser
Patch29:        CVE-2025-6069-quad-complex-HTMLParser.patch
BuildRequires:  autoconf-archive
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
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
#!BuildIgnore:  gdk-pixbuf-loader-rsvg
%if 0%{?suse_version} >= 1550
# The provider for python(abi) is in rpm-build-python
BuildRequires:  rpm-build-python
%endif
%if 0%{?suse_version} >= 1500 && 0%{?suse_version} < 1599
BuildRequires:  pkgconfig(libnsl)
BuildRequires:  pkgconfig(libtirpc)
%endif
%if %{with mpdecimal}
BuildRequires:  mpdecimal-devel
%endif
%if %{with doc}
%if 0%{?sle_version} && 0%{?sle_version} <= 150300
BuildRequires:  python3-Sphinx
%else
BuildRequires:  python3-Sphinx >= 3.2.0
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-python-docs-theme >= 2022.1
%endif
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
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(x11)
Requires:       %{python_pkg_name}-base = %{version}
Provides:       %{python_pkg_name}-readline
Provides:       %{python_pkg_name}-sqlite3
Recommends:     %{python_pkg_name}-curses
Recommends:     %{python_pkg_name}-dbm
Recommends:     %{python_pkg_name}-pip
%obsolete_python_versioned
%if %{primary_interpreter}
Provides:       python3 = %{python_version}
Provides:       python3-readline
Provides:       python3-sqlite3
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
%obsolete_python_versioned tk
%if %{primary_interpreter}
Provides:       python3-tk = %{version}
%endif

%description -n %{python_pkg_name}-tk
Python interface to Tk. Tk is the GUI toolkit that comes with Tcl.

%package -n %{python_pkg_name}-curses
Summary:        Python Interface to the (N)Curses Library
Requires:       %{python_pkg_name} = %{version}
%obsolete_python_versioned curses
%if %{primary_interpreter}
Provides:       python3-curses
%endif

%description -n %{python_pkg_name}-curses
An easy to use interface to the (n)curses CUI library. CUI stands for
Console User Interface.

%package -n %{python_pkg_name}-dbm
Summary:        Python Interface to the GDBM Library
Requires:       %{python_pkg_name} = %{version}
%obsolete_python_versioned dbm
%if %{primary_interpreter}
Provides:       python3-dbm
%endif

%description -n %{python_pkg_name}-dbm
An easy to use interface for Unix DBM databases, and more specifically,
the GNU implementation GDBM.

%package -n %{python_pkg_name}-idle
Summary:        An Integrated Development Environment for Python
Requires:       %{python_pkg_name} = %{version}
Requires:       %{python_pkg_name}-tk
%obsolete_python_versioned idle
%if %{primary_interpreter}
Provides:       python3-idle = %{version}
%endif

%description -n %{python_pkg_name}-idle
IDLE is a Tkinter based integrated development environment for Python.
It features a multi-window text editor with multiple undo, Python
colorizing, and many other things, as well as a Python shell window and
a debugger.

%package -n %{python_pkg_name}-doc
Summary:        Package Documentation for Python 3
Enhances:       %{python_pkg_name} = %{python_version}
%obsolete_python_versioned doc
%if %{primary_interpreter}
Provides:       python3-doc = %{version}
%endif

%description -n %{python_pkg_name}-doc
Tutorial, Global Module Index, Language Reference, Library Reference,
Extending and Embedding Reference, Python/C API Reference, Documenting
Python, and Macintosh Module Reference in HTML format.

%package -n %{python_pkg_name}-doc-devhelp
Summary:        Additional Package Documentation for Python 3 in devhelp format
%obsolete_python_versioned doc-devhelp
%if %{primary_interpreter}
Provides:       python3-doc-devhelp = %{version}
%endif

%description -n %{python_pkg_name}-doc-devhelp
Tutorial, Global Module Index, Language Reference, Library Reference,
Extending and Embedding Reference, Python/C API Reference, Documenting
Python, and Macintosh Module Reference in format for devhelp.

%package -n %{python_pkg_name}-base
Summary:        Python 3 Interpreter and Stdlib Core
Requires:       libpython%{so_version} = %{version}
Recommends:     %{python_pkg_name} = %{version}
%obsolete_python_versioned base
#Recommends:     python3-ensurepip
# python 3.1 didn't have a separate python-base, so it is wrongly
# not a conflict to have python3-3.1 and python3-base > 3.1
Obsoletes:      python3 < 3.2
# no Provides, because python3 is obviously provided by package python3
# python 3.4 provides asyncio
Provides:       %{python_pkg_name}-asyncio = %{version}
%obsolete_python_versioned asyncio
# python 3.6 provides typing
Provides:       %{python_pkg_name}-typing = %{version}
%obsolete_python_versioned typing
# python3-xml was merged into python3, now moved into -base
Provides:       %{python_pkg_name}-xml = %{version}
%if %{primary_interpreter}
Provides:       python3-asyncio = %{version}
Obsoletes:      python3-asyncio < %{version}
Provides:       python3-base = %{version}
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
%obsolete_python_versioned tools
%if %{primary_interpreter}
Provides:       python3-2to3 = %{version}
Provides:       python3-demo = %{version}
Provides:       python3-tools = %{version}
Obsoletes:      python3-2to3 < %{version}
Obsoletes:      python3-demo < %{version}
%endif

%description -n %{python_pkg_name}-tools
A number of scripts that are useful for building, testing or extending Python,
and a set of demonstration programs.

%package -n %{python_pkg_name}-devel
Summary:        Include Files and Libraries Mandatory for Building Python Modules
Requires:       %{python_pkg_name}-base = %{version}
%obsolete_python_versioned devel
%if %{primary_interpreter}
Provides:       python3-devel = %{version}
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
%obsolete_python_versioned testsuite
%if %{primary_interpreter}
Provides:       python3-testsuite = %{version}
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
%autopatch -p1 -M 07
%if 0%{?sle_version} && 0%{?sle_version} <= 150300
%patch -p1 -P 11
%endif
%autopatch -p1 -m 12 -M 20
%if ! 0%{?sle_version} || 0%{?sle_version} >= 160000
%patch -p1 -P 21
%endif
%autopatch -p1 -m 22

# drop Autoconf version requirement
sed -i 's/^AC_PREREQ/dnl AC_PREREQ/' configure.ac

%if %{primary_interpreter}
# fix shebangs - convert /usr/local/bin/python and /usr/bin/env/python to /usr/bin/python3
for dir in Lib Tools; do
    # find *.py, filter to files that contain bad shebangs
    # break up "/""usr" like this to prevent replacing with %%{_prefix}
    find $dir -name '*.py' -type f -print0 \
        | xargs -0 grep -lE '^#! *(/''usr/.*bin/(env +)?)?python' \
        | xargs sed -r -i -e '1s@^#![[:space:]]*(/''usr/(local/)?bin/(env +)?)?python([0-9]+(\.[0-9]+)?)?@#!%{_bindir}/python3@'
done
%else
# For non-primary Python, just don't bother (bsc#1193179) and remove all
# those shebangs
for dir in Lib Tools; do
    find $dir -name '*.py' -type f -exec sed -i '1{/^#!.*python/ d}' '{}' \;
done
# We shortened the file Lib/pdb.py so we have to move the test breakpoint location
sed -i -e '/Breakpoint 3 at ...pdb.py:94/s/94/93/' Lib/test/test_pdb.py
%endif

# drop in-tree libffi and expat
rm -r Modules/_ctypes/libffi* Modules/_ctypes/darwin
rm -r Modules/expat

# drop duplicate README from site-packages
rm Lib/site-packages/README.txt

# Add vendored bluez-devel files
tar xvf %{SOURCE21}

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
export OPT="%{optflags} -DOPENSSL_LOAD_CONF -fwrapv $(pkg-config --cflags-only-I libffi) -fno-semantic-interposition"

touch -r %{SOURCE0} Makefile.pre.in

autoreconf -fvi

%if 0%{?sles_version}
sed -e 's/-fprofile-correction//' -i Makefile.pre.in
%endif

export CFLAGS="%{optflags} -IVendor/"

%configure \
    --with-platlibdir=%{_lib} \
    --docdir=%{_docdir}/python \
    --enable-ipv6 \
    --enable-shared \
    --with-ensurepip=no \
    --with-system-ffi \
    --with-system-expat \
    --with-lto \
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
    --with-ssl-default-suites=openssl \
%endif
%if %{with profileopt}
    --enable-optimizations \
%endif
%if %{with mpdecimal}
    --with-system-libmpdec \
%endif
    --enable-loadable-sqlite-extensions

# prevent make from trying to rebuild PYTHON_FOR_GEN stuff
# %%make_build -t Python/Python-ast.c \
        # Include/Python-ast.h \
        # Objects/typeslots.inc \
        # Python/opcode_targets.h \
        # Include/opcode.h
%make_build

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
export SUSE_VERSION="0%{?suse_version}"
export SLE_VERSION="0%{?sle_version}"
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
EXCLUDE="$EXCLUDE test_faulthandler test_multiprocessing_forkserver test_multiprocessing_spawn test_os test_posix test_signal test_socket test_subprocess"
%endif

# This test (part of test_uuid) requires real network interfaces
# so that ifconfig output has "HWaddr <something>".  Some kvm instances
# done have any such interface breaking the uuid module.
EXCLUDE="$EXCLUDE test_uuid"

# bsc#1195140 and bpo#37169 - test_capi is failing on openSUSE, and not sure why
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
    xml xmlrpc zoneinfo
do
    rm -r %{buildroot}%{sitedir}/$module
done

for library in \
    array _asyncio audioop binascii _bisect _bz2 cmath _codecs_* \
    _contextvars _crypt _csv _ctypes _datetime _decimal fcntl grp \
    _hashlib _heapq _json _lsprof _lzma math mmap _multibytecodec \
    _multiprocessing _opcode ossaudiodev _pickle _posixshmem \
    _posixsubprocess _queue _random resource select _ssl _socket spwd \
    _statistics _struct syslog termios _testbuffer _testimportmultiple \
    _testmultiphase unicodedata zlib _ctypes_test _testinternalcapi _testcapi \
    _testclinic xxlimited xxlimited_35 \
    _xxtestfuzz _xxsubinterpreters _elementtree pyexpat _md5 _sha1 \
    _sha256 _sha512 _blake2 _sha3 _uuid _zoneinfo
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
cp %{SOURCE19} idle%{python_version}.desktop
sed -i -e 's:idle3:idle%{python_version}:g' idle%{python_version}.desktop
install -m 644 -D -t %{buildroot}%{_datadir}/applications idle%{python_version}.desktop

cp %{SOURCE20} idle%{python_version}.appdata.xml
sed -i -e 's:idle3.desktop:idle%{python_version}.desktop:g' idle%{python_version}.appdata.xml
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
rm %{buildroot}%{_mandir}/man1/python3.1
# devel
rm %{buildroot}%{_bindir}/python3-config
rm %{buildroot}%{_libdir}/libpython3.so
rm %{buildroot}%{_libdir}/pkgconfig/{python3,python3-embed}.pc
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

# Remove -IVendor/ from python-config boo#1231795
sed -i 's/-IVendor\///' %{buildroot}%{_bindir}/python%{python_abi}-config

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

# For the purposes of reproducibility, it is necessary to eliminate any *.pyc files inside documentation dirs
if [ -d %{buildroot}%{_defaultdocdir} ] ; then
find %{buildroot}%{_defaultdocdir} -type f -name \*.pyc -ls -exec rm -vf '{}' \;
fi

%if %{with general}
%files -n %{python_pkg_name}-tk
%{sitedir}/tkinter
%exclude %{sitedir}/tkinter/test
%{dynlib _tkinter}

%files -n %{python_pkg_name}-curses
%{sitedir}/curses
%{dynlib _curses}
%{dynlib _curses_panel}

%files -n %{python_pkg_name}-dbm
%{sitedir}/dbm
%{dynlib _dbm}
%{dynlib _gdbm}

%files -n %{python_pkg_name}
%dir %{sitedir}
%dir %{sitedir}/lib-dynload
%{sitedir}/sqlite3
%exclude %{sitedir}/sqlite3/test
%{dynlib readline}
%{dynlib _sqlite3}
%if 0%{?suse_version} >= 1500 && 0%{?suse_version} < 1599
%{dynlib nis}
%endif

%files -n %{python_pkg_name}-idle
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
%{_datadir}/metainfo/idle%{python_version}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/idle%{python_version}.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/*/apps
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
%{_libdir}/libpython%{python_abi}.so.%{so_major}.%{so_minor}

%files -n %{python_pkg_name}-tools
%{sitedir}/turtledemo
%if %{primary_interpreter}
%{_bindir}/2to3
%endif
%attr(755, root, root)%{_bindir}/2to3-%{python_version}
%doc %{_docdir}/%{name}/Tools

%files -n %{python_pkg_name}-devel
%{_libdir}/libpython%{python_abi}.so
%if %{primary_interpreter}
%{_libdir}/libpython3.so
%endif
%{_libdir}/pkgconfig/*
%{_includedir}/python%{python_abi}
%{sitedir}/config-%{python_abi}-*
%{_bindir}/python%{python_abi}-config
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
%{sitedir}/test
%{sitedir}/*/test
%{sitedir}/*/tests
%{dynlib _ctypes_test}
%{dynlib _testbuffer}
%{dynlib _testcapi}
%{dynlib _testclinic}
%{dynlib _testinternalcapi}
%{dynlib _testimportmultiple}
%{dynlib _testmultiphase}
%{dynlib xxlimited}
# workaround for missing packages
%dir %{sitedir}/sqlite3
%dir %{sitedir}/tkinter

%files -n %{python_pkg_name}-base
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
%{dynlib _contextvars}
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
%{dynlib _pickle}
%{dynlib _posixshmem}
%{dynlib _posixsubprocess}
%{dynlib pyexpat}
%{dynlib _queue}
%{dynlib _random}
%{dynlib resource}
%{dynlib select}
%{dynlib _socket}
%{dynlib spwd}
%{dynlib _ssl}
%{dynlib _statistics}
%{dynlib _struct}
%{dynlib syslog}
%{dynlib termios}
%{dynlib unicodedata}
%{dynlib _uuid}
%{dynlib _xxsubinterpreters}
%{dynlib _xxtestfuzz}
%{dynlib xxlimited_35}
%{dynlib zlib}
%{dynlib _zoneinfo}
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
%{sitedir}/zoneinfo
%{sitedir}/__pycache__
# import-failed hooks
%{sitedir}/_import_failed
%{sitedir}/site-packages/zzzz-import-failed-hooks.pth
# symlinks
%if %{primary_interpreter}
%{_bindir}/python3
%{_bindir}/pydoc3
%endif
# executables
%attr(755, root, root) %{_bindir}/pydoc%{python_version}
# %%attr(755, root, root) %%{_bindir}/python%%{python_abi}
%attr(755, root, root) %{_bindir}/python%{python_version}
# endif for if base
%endif

%changelog
