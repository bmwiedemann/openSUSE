#
# spec file for package mcstrans
#
# Copyright (c) 2020 SUSE LLC
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


Name:           mcstrans
Version:        3.1
Release:        0
Summary:        SELinux Translation Daemon
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/SELinuxProject/selinux/wiki
Source:         https://github.com/SELinuxProject/selinux/releases/download/20200710/%{name}-%{version}.tar.gz
Patch0:         %{name}-writepid.patch
Patch1:         add_includes.patch
BuildRequires:  aaa_base
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel >= 1.30.3
BuildRequires:  libsepol-devel-static
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig(systemd)
Requires:       aaa_base
Provides:       setransd
%{?systemd_requires}

%description
Security-enhanced Linux is a feature of the Linux kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement, Role-based Access
Control, and Multi-level Security.

mcstrans provides a translation daemon to translate SELinux categories
from internal representations to user defined representation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
make LIBDIR="%{_libdir}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_unitdir}
%make_install LIBDIR="%{buildroot}%{_libdir}" SHLIBDIR="%{buildroot}/%{_lib}"
rm -f %{buildroot}%{_sbindir}/*
rm -f %{buildroot}%{_libdir}/*.a
rm %{buildroot}%{_sysconfdir}/rc.d/init.d/mcstrans*
rm -rf %{buildroot}%{_sysconfdir}/rc.d
mkdir -p %{buildroot}%{_datadir}/doc/packages/%{name}
cp -r share/examples %{buildroot}%{_datadir}/doc/packages/%{name}
mkdir -p %{buildroot}%{_sbindir}
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%post
%service_add_post mcstrans.service

%preun
%service_del_preun mcstrans.service

%postun
%service_del_postun mcstrans.service

%pre
%service_add_pre mcstrans.service

%files
%{_unitdir}/mcstrans*.service
/sbin/mcstransd
%{_sbindir}/rcmcstrans
%{_mandir}/man5/*.5%{?ext_man}
%{_mandir}/ru/man5/*.5%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}
%{_mandir}/ru/man8/*.8%{?ext_man}
%dir %{_datadir}/doc/packages/%{name}
%{_datadir}/doc/packages/%{name}/*

%changelog
