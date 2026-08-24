#
# spec file for package Regina-REXX
#
# Copyright (c) 2026 SUSE LLC
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


%define somajor 3
%define libname libregina%{somajor}
Name:           Regina-REXX
Version:        3.9.7
Release:        0
Summary:        Mark Hessling's implementation of the REXX Interpreter
License:        GFDL-1.1-only AND LGPL-2.1-or-later
URL:            https://regina-rexx.sourceforge.io/
# The regina-documentation downloads offered next to the release are the very
# same two PDFs the tarball already ships in doc/, so they are not fetched
# separately -- doing so only duplicated 1.5 MB into the -doc package.
Source:         https://sourceforge.net/projects/regina-rexx/files/regina-rexx/%{version}/regina-rexx-%{version}.tar.gz#/Regina-REXX-%{version}.tar.gz
Source1:        rxstack.service
# PATCH-FIX-UPSTREAM Regina-REXX-parallel-make.patch -- compile the alternate-variant objects with -o instead of moving the shared object aside and back, which races under make -j
Patch0:         Regina-REXX-parallel-make.patch
# PATCH-FIX-UPSTREAM Regina-REXX-trip-helpers-c99.patch -- include <stdlib.h> in the trip test helpers, whose implicit exit()/atoi() declarations are an error since GCC 14
Patch1:         Regina-REXX-trip-helpers-c99.patch
BuildRequires:  alts
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(ncurses)
# /usr/bin/{rexx,rxqueue} are symlinks to /usr/bin/alts, which comes from alts.
Requires:       alts
Provides:       rexx
%{?systemd_ordering}

%description
Mark Hessling's implementation of the REXX language interpreter.

%package devel
Summary:        Header files for the REXX interpreter
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Provides:       regina-devel = %{version}-%{release}
Provides:       regina:%{_includedir}/rexxsaa.h

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require Regina-REXX.

%package -n %{libname}
Summary:        The regina shared library

%description -n %{libname}
This package provides the shared library for Mark Hessling's implementation
of the REXX Interpreter.

%package doc
Summary:        Documentation for the Regina REXX interpreter
BuildArch:      noarch

%description doc
Documentation for both the Regina REXX interpreter and the REXX Utility
Functions (regutil).

%prep
%autosetup -p1 -n regina-rexx-%{version}

%build
%configure \
  --enable-posix-threads
%make_build

%install
%make_install
# The supplied init script isn't sufficient for our needs.
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/rxstack.service
# Do not ship statical library
rm -f %{buildroot}%{_libdir}/libregina.a

# The examples carry a "#!/usr/bin/env regina" shebang, which is not allowed in
# packaged scripts, and rexxcps.rexx still has its original CRLF line endings.
sed -i -e '1s|^#!%{_bindir}/env regina|#!%{_bindir}/regina|' -e 's/\r$//' \
    %{buildroot}%{_datadir}/regina-rexx/examples/*.rexx

# Installed executable by the build system, but it is a plain data file.
chmod 0644 %{buildroot}%{_libdir}/pkgconfig/libregina.pc

install -m 755 -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcrxstack

# ooRexx provides the same rexx and rxqueue commands (boo#1083875), so both are
# registered with libalternatives -- update-alternatives is deprecated and must
# not be used in new packages. /usr/bin/{rexx,rxqueue} are plain symlinks to
# /usr/bin/alts, which reads the config files below and exec()s the highest
# priority binary; there is no install-time state, hence no scriptlet.
mv %{buildroot}%{_bindir}/rexx %{buildroot}%{_bindir}/rexx-%{name}
mv %{buildroot}%{_bindir}/rxqueue %{buildroot}%{_bindir}/rxqueue-%{name}

mkdir -p %{buildroot}%{_datadir}/libalternatives/rexx
mkdir -p %{buildroot}%{_datadir}/libalternatives/rxqueue
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/rexx
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/rxqueue

# Priority 15 is the one update-alternatives used, so the relative precedence
# against the other REXX interpreters does not change.
#
# KeepArgv0 keeps argv[0] as the user typed it, which is what the plain
# symlink used to deliver: both rexx.c and rxqueue.c print argv[0] verbatim in
# their usage and -v output, so without it every message would name the
# internal rexx-Regina-REXX. Nothing branches on argv[0] -- on Linux regina
# locates itself via readlink("/proc/self/exe"), which exec() keeps correct.
#
# group= ties rexx and rxqueue together so selecting one switches both. They are
# not independent in practice: rxqueue talks to the queue of its own
# interpreter, so Regina's rexx alongside ooRexx's rxqueue is a combination
# nothing supports, even though update-alternatives allowed it. A group only
# takes effect if every member declares the identical group, so this must match
# ooRexx, which registers the same two names as a group at its own priority; a
# group declared on one side only is silently inert. rexxc and rxsubcom are
# deliberately absent -- they are ooRexx-only, and naming a member no other
# provider can supply is what the libalternatives documentation warns against.
cat > %{buildroot}%{_datadir}/libalternatives/rexx/15.conf <<EOF
binary=%{_bindir}/rexx-%{name}
man=regina.1
group=rexx,rxqueue
options=KeepArgv0
EOF
cat > %{buildroot}%{_datadir}/libalternatives/rxqueue/15.conf <<EOF
binary=%{_bindir}/rxqueue-%{name}
man=rxqueue-%{name}.1
group=rexx,rxqueue
options=KeepArgv0
EOF

# ooRexx also owns man1/rexx.1 and man1/rxqueue.1 outright, so those two paths
# must not be shipped here as well -- the previous revival attempt (request
# 1287670) was declined over exactly that conflict. rexx.1 is a byte-identical
# copy of regina.1, which we do ship, so it is simply dropped; rxqueue.1 is
# Regina-specific and is renamed to sit next to the binary it documents. The
# man= entries above keep "man rexx" and "man rxqueue" resolving, as man(1)
# itself is linked against libalternatives.
rm -f %{buildroot}%{_mandir}/man1/rexx.1%{?ext_man}
mv %{buildroot}%{_mandir}/man1/rxqueue.1%{?ext_man} \
   %{buildroot}%{_mandir}/man1/rxqueue-%{name}.1%{?ext_man}

%check
# trip/ is upstream's ANSI conformance suite. Its own "testing" driver calls
# every case as a REXX *function* and aborts on the first one that returns no
# value, so it never reaches most of them -- run the cases directly instead.
# The cases report a failure by PRINTING "FuncTrip: error" and still exit 0,
# so the output has to be inspected; the exit status alone proves nothing.
pushd trip
# The ADDRESS COMMAND cases refuse to run without these three helpers.
for helper in rc true std; do
  gcc %{optflags} -o $helper $helper.c
done
# Deliberately not run:
#   builtin              pre-existing FORMAT/TRUNC rounding deviations, some of
#                        which the test file itself marks disputed ("this is an
#                        error in TRL") -- they are not caused by this build
#   time                 runs "sleep 3" and asserts the elapsed whole seconds
#                        are exactly 3, which a loaded build host will miss
#   error, lexical2      read from stdin and hang
#   addrtest4*, qocca    exit non-zero unprompted
for t in addrtest1 addrtest2 addrtest3 arith assign create files funcs \
         lexical limits lostdigits signal stack stats trip variable; do
  if ! out=$(LD_LIBRARY_PATH=.. PATH=".:$PATH" ../regina $t.rexx 2>&1); then
    echo "TRIP FAILURE (non-zero exit): $t.rexx"
    echo "$out"
    exit 1
  fi
  if echo "$out" | grep -qE 'FuncTrip: error|^Error [0-9]|Syntax error'; then
    echo "TRIP FAILURE (reported error): $t.rexx"
    echo "$out"
    exit 1
  fi
  echo "trip: $t.rexx OK"
done
popd

%pre
%service_add_pre rxstack.service

%post
%service_add_post rxstack.service

%preun
%service_del_preun rxstack.service

%postun
%service_del_postun rxstack.service

%ldconfig_scriptlets -n %{libname}

%files
%license COPYING-LIB
%doc README.*
%{_mandir}/man1/regina.1%{?ext_man}
%{_mandir}/man1/rxqueue-%{name}.1%{?ext_man}
%{_mandir}/man1/rxstack.1%{?ext_man}
%config(noreplace) %{_sysconfdir}/rxstack.conf
%{_bindir}/regina
%{_bindir}/rexx
%{_bindir}/rexx-%{name}
%{_bindir}/rxqueue
%{_bindir}/rxqueue-%{name}
%{_bindir}/rxstack
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/rexx
%dir %{_datadir}/libalternatives/rxqueue
%{_datadir}/libalternatives/rexx/15.conf
%{_datadir}/libalternatives/rxqueue/15.conf
%{_datadir}/regina-rexx
%{_sbindir}/rcrxstack
%{_unitdir}/rxstack.service

%files doc
%license COPYING-LIB
%doc doc/regina.pdf doc/regutil.pdf

%files devel
%{_bindir}/regina-config
%{_mandir}/man1/regina-config.1%{?ext_man}
%{_includedir}/rexxsaa.h
%{_libdir}/libregina.so
%{_libdir}/pkgconfig/libregina.pc

%files -n %{libname}
%license COPYING-LIB
%{_libdir}/libregina.so.%{somajor}*
%{_libdir}/regina-rexx

%changelog
