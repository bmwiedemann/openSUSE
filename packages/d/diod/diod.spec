#
# spec file for package diod
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           diod
Version:        1.1.0+0.ga32f5a4
Release:        0
Summary:        Distributed I/O Daemon - a 9P file server
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/chaos/diod
Source0:        %{name}-%{version}.tar.xz
Patch0:         harden_diod.service.patch
Patch1:         libnpclient-noinline-npc_gets.patch
BuildRequires:  autogen
BuildRequires:  automake
BuildRequires:  c_compiler
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(lua5.3)
BuildRequires:  pkgconfig(munge)
BuildRequires:  pkgconfig(ncurses)
Recommends:     munge

%description
This package contains diod, a multi-threaded, user space file server
that speaks 9P2000.L protocol.

%prep
%autosetup -p1

%build
autoreconf -fiv
export CPPFLAGS=-I%{_includedir}/lua5.3
%configure --with-systemdsystemunitdir=%{_unitdir}
make %{?_smp_mflags}

%install
%make_install
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcdiod
%if 0%{?suse_version} < 1550
mkdir %{buildroot}/sbin
ln -s %{_sbindir}/mount.diod %{buildroot}/sbin/mount.diod
%endif

%pre
%service_add_pre diod.service

%preun
%service_del_preun diod.service

%post
%service_add_post diod.service

%postun
%service_del_postun diod.service

%files
%license COPYING
%doc README.md NEWS.md

%if 0%{?suse_version} < 1550
/sbin/*
%endif
%{_sbindir}/*
%{_unitdir}/diod.service

%ghost %{_sysconfdir}/diod.conf
%ghost %{_sysconfdir}/auto.diod

%{_mandir}/man8/*
%{_mandir}/man5/*

%changelog
