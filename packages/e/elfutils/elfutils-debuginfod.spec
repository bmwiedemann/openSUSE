#
# spec file for package elfutils-debuginfod
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


Name:           elfutils-debuginfod
Version:        0.183
Release:        0
Summary:        Debuginfod server provided by elfutils
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://sourceware.org/elfutils/
#Git-Clone:	git://sourceware.org/git/elfutils
Source:         https://fedorahosted.org/releases/e/l/elfutils/%{version}/elfutils-%{version}.tar.bz2
Source1:        https://fedorahosted.org/releases/e/l/elfutils/%{version}/elfutils-%{version}.tar.bz2.sig
Source2:        elfutils.changes
Source3:        elfutils.keyring
Patch0:         disable-run-readelf-self-test.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
# For the run-debuginfod-find.sh test case in %%check for /usr/sbin/ss
BuildRequires:  curl
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  iproute
BuildRequires:  libbz2-devel
BuildRequires:  pkgconfig
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# For debuginfod
BuildRequires:  pkgconfig(libarchive) >= 3.1.2
BuildRequires:  pkgconfig(libcurl) >= 7.29.0
BuildRequires:  pkgconfig(libmicrohttpd) >= 0.9.33
BuildRequires:  pkgconfig(sqlite3) >= 3.7.17
BuildRequires:  pkgconfig(systemd)
Requires:       debuginfod-client = %{version}
Requires:       elfutils = %{version}
Requires:       sysconfig
Requires(post): %fillup_prereq
%{?systemd_requires}

%description
The elfutils-debuginfod package contains the debuginfod binary
and control files for a service that can provide ELF/DWARF
files to remote clients, based on build-id identification.
The ELF/DWARF file searching functions in libdwfl can query
such servers to download those files on demand.

%package -n libdebuginfod1
Summary:        Library for build-id HTTP ELF/DWARF server
Group:          System/Libraries
Conflicts:      libdebuginfod1-dummy = %{version}

%description -n libdebuginfod1
The libdebuginfod1 package contains shared libraries
dynamically loaded from -ldw, which use a debuginfod service
to look up debuginfo and associated data. Also includes a
command-line frontend.

%package -n libdebuginfod-devel
Summary:        Libraries and headers to build debuginfod client applications
Group:          Development/Libraries/C and C++
Conflicts:      libdebuginfod-dummy-devel = %{version}

%description -n libdebuginfod-devel
The libdebuginfod-devel package contains the libraries
to create applications to use the debuginfod service.

%package -n debuginfod-client
Summary:        Command line client for build-id HTTP ELF/DWARF server
Group:          Development/Tools/Building
Conflicts:      debuginfod-dummy-client = %{version}

%description -n debuginfod-client
The elfutils-debuginfod-client package contains a command-line frontend.

%lang_package

%prep
%autosetup -n elfutils-%version -p1

%build
%global _lto_cflags %{_lto_cflags} -flto-partition=none -Wno-error=stack-usage=
# Change DATE/TIME macros to use last change time of elfutils.changes
# See http://lists.opensuse.org/opensuse-factory/2011-05/msg00304.html
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
# Set modversion used to verify dynamically loaded ebl backend matches to
# similarly predictable value [upstream default is hostname + date]
MODVERSION="suse-build `eval echo ${DATE} ${TIME}`"
sed --in-place "s/^MODVERSION=.*\$/MODVERSION=\"${MODVERSION}\"/" configure.ac
export CFLAGS="%optflags"
CFLAGS+=" -g" # make tests pass when user does not want debuginfo (boo#1031556)
%ifarch %sparc
# Small PIC model not sufficient
CFLAGS+=" -fPIC"
%endif
autoreconf -fi
# some patches create new test scripts, which are created 644 by default
chmod a+x tests/run*.sh
%configure --enable-debuginfod-urls=https://debuginfod.opensuse.org/ \
  --program-prefix=eu-
%make_build

%install
%make_install
# remove unneeded files
rm -f %{buildroot}/%{_libdir}/*.la
ls -lR %{buildroot}/%{_libdir}/libelf*

rm -f %{buildroot}/%{_bindir}/eu*
rm -f %{buildroot}/%{_libdir}/libasm*
rm -f %{buildroot}/%{_includedir}/elfutils/lib*.h
rm -f %{buildroot}/%{_includedir}/elfutils/elf-knowledge.h
rm -f %{buildroot}/%{_includedir}/elfutils/known-dwarf.h
rm -f %{buildroot}/%{_includedir}/elfutils/version.h
rm -f %{buildroot}/%{_libdir}/libelf*
rm -f %{buildroot}/%{_includedir}/libelf.h
rm -f %{buildroot}/%{_includedir}/gelf.h
rm -f %{buildroot}/%{_includedir}/nlist.h
rm -f %{buildroot}/%{_includedir}/dwarf.h
rm -f %{buildroot}/%{_libdir}/libdw*
rm -f %{buildroot}/%{_mandir}/man3/elf_*.3*
rm -f %{buildroot}/%{_mandir}/man1/eu-*.1*
rm -rf %{buildroot}%{_datadir}/locale/
rm -f %{buildroot}/%{_libdir}/pkgconfig/libdw.pc
rm -f %{buildroot}/%{_libdir}/pkgconfig/libelf.pc

install -Dm0644 config/debuginfod.service %{buildroot}%{_unitdir}/debuginfod.service
install -d -m 755 %{buildroot}%{_fillupdir}
cp config/debuginfod.sysconfig %{buildroot}%{_fillupdir}/sysconfig.debuginfod

mkdir -p %{buildroot}%{_localstatedir}/cache/debuginfod
touch %{buildroot}%{_localstatedir}/cache/debuginfod/debuginfod.sqlite

%post -n libdebuginfod1 -p /sbin/ldconfig
%postun -n libdebuginfod1 -p /sbin/ldconfig

%check
%if 0%{?qemu_user_space_build}
# qemu-linux-user does not support ptrace and a few other process details
export XFAIL_TESTS="dwfl-proc-attach run-backtrace-dwarf.sh run-backtrace-native.sh run-deleted.sh"
%endif
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS NOTES README THANKS TODO
%{_bindir}/debuginfod
%{_unitdir}/debuginfod.service
%{_mandir}/man8/debuginfod.8*
%{_fillupdir}/sysconfig.debuginfod

%dir %attr(0700,debuginfod,debuginfod) %{_localstatedir}/cache/debuginfod
%verify(not md5 size mtime) %attr(0600,debuginfod,debuginfod) %{_localstatedir}/cache/debuginfod/debuginfod.sqlite

%files -n libdebuginfod1
%{_libdir}/libdebuginfod.so.*
%{_libdir}/libdebuginfod-%{version}.so
%config %{_sysconfdir}/profile.d/debuginfod.sh
%config %{_sysconfdir}/profile.d/debuginfod.csh

%files -n libdebuginfod-devel
%{_libdir}/pkgconfig/libdebuginfod.pc
%{_mandir}/man3/debuginfod_*.3*
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/debuginfod.h
%{_libdir}/libdebuginfod.so

%files -n debuginfod-client
%{_bindir}/debuginfod-find
%{_mandir}/man1/debuginfod-find.1*

%pre
getent group debuginfod >/dev/null || %{_sbindir}/groupadd -r debuginfod
getent passwd debuginfod >/dev/null || %{_sbindir}/useradd -r -g debuginfod -d %{_localstatedir}/cache/debuginfod -s /bin/false -c "elfutils debuginfo server" debuginfod
%service_add_pre debuginfod.service

%post
%service_add_post debuginfod.service
%{fillup_only -n debuginfod}

%preun
%service_del_preun debuginfod.service

%postun
%service_del_postun debuginfod.service

%changelog
