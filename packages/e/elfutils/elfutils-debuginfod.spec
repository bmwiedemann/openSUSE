#
# spec file for package elfutils-debuginfod
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


Name:           elfutils-debuginfod
Version:        0.188
Release:        0
Summary:        Debuginfod server provided by elfutils
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://sourceware.org/elfutils/
#Git-Clone:	git://sourceware.org/git/elfutils
Source:         https://fedorahosted.org/releases/e/l/elfutils/%{version}/elfutils-%{version}.tar.bz2
Source1:        https://fedorahosted.org/releases/e/l/elfutils/%{version}/elfutils-%{version}.tar.bz2.sig
Source3:        elfutils.keyring
Source4:        %{name}.sysusers
Patch1:         harden_debuginfod.service.patch
Patch2:         0005-backends-Add-RISC-V-object-attribute-printing.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bsdtar
BuildRequires:  procps
BuildRequires:  sysuser-tools
# For the run-debuginfod-find.sh test case in %%check for /usr/sbin/ss
BuildRequires:  curl
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  iproute
BuildRequires:  libbz2-devel
BuildRequires:  libzstd-devel
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
Requires(post): %fillup_prereq
%{?systemd_ordering}
%sysusers_requires

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
License:        GPL-2.0-or-later OR LGPL-3.0-or-later
Recommends:     debuginfod-profile

%description -n libdebuginfod1
The libdebuginfod1 package contains shared libraries
dynamically loaded from -ldw, which use a debuginfod service
to look up debuginfo and associated data. Also includes a
command-line frontend.

%package -n libdebuginfod-devel
Summary:        Libraries and headers to build debuginfod client applications
Group:          Development/Libraries/C and C++
Conflicts:      libdebuginfod-dummy-devel = %{version}
License:        GPL-2.0-or-later OR LGPL-3.0-or-later
Requires:       libdebuginfod1 = %{version}

%description -n libdebuginfod-devel
The libdebuginfod-devel package contains the libraries
to create applications to use the debuginfod service.

%package -n debuginfod-client
Summary:        Command line client for build-id HTTP ELF/DWARF server
Group:          Development/Tools/Building
Conflicts:      debuginfod-dummy-client = %{version}

%description -n debuginfod-client
The elfutils-debuginfod-client package contains a command-line frontend.

%package -n debuginfod-profile
Summary:        Profile files for build-id HTTP ELF/DWARF server
Group:          Development/Tools/Building

%description -n debuginfod-profile
The debuginfod-profile package contains a profile files that set default
URL for a distribution.

%lang_package

%prep
%autosetup -n elfutils-%version -p1

%build
%sysusers_generate_pre %{SOURCE4} %{name} %{name}.conf
export CFLAGS="%optflags -Werror=date-time"
CFLAGS+=" -g" # tests need debug info enabled (boo#1031556)
%ifarch %sparc
# Small PIC model not sufficient
CFLAGS+=" -fPIC"
%endif
autoreconf -fi
# some patches create new test scripts, which are created 644 by default
chmod a+x tests/run*.sh
%configure \
%if %{suse_version} > 1500
  --enable-debuginfod-urls=https://debuginfod.opensuse.org/ \
%endif
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

install -Dm0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf

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
%{_sysusersdir}/%{name}.conf
%{_mandir}/man8/debuginfod.service.8.*

%dir %attr(0700,debuginfod,debuginfod) %{_localstatedir}/cache/debuginfod
%ghost %attr(0600,debuginfod,debuginfod) %{_localstatedir}/cache/debuginfod/debuginfod.sqlite

%files -n libdebuginfod1
%{_libdir}/libdebuginfod.so.*
%{_libdir}/libdebuginfod-%{version}.so

%files -n libdebuginfod-devel
%{_libdir}/pkgconfig/libdebuginfod.pc
%{_mandir}/man3/debuginfod_*.3*
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/debuginfod.h
%{_libdir}/libdebuginfod.so

%files -n debuginfod-client
%{_bindir}/debuginfod-find
%{_mandir}/man1/debuginfod-find.1*
%{_mandir}/man7/debuginfod-client-config.7*

%files -n debuginfod-profile
%config %{_sysconfdir}/profile.d/debuginfod.sh
%config %{_sysconfdir}/profile.d/debuginfod.csh
%dir %{_sysconfdir}/debuginfod
%config %{_sysconfdir}/debuginfod/elfutils.urls

%pre -f %{name}.pre
%service_add_pre debuginfod.service

%post
%service_add_post debuginfod.service
%{fillup_only -n debuginfod}

%preun
%service_del_preun debuginfod.service

%postun
%service_del_postun debuginfod.service

%changelog
