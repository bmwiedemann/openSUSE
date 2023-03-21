#
# spec file for package ksmbd-tools
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
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           ksmbd-tools
Version:        3.4.7
Release:        0
Summary:        ksmbd kernel server userspace utilities
License:        GPL-2.0-or-later
Group:          System/Filesystems
Url:            https://github.com/cifsd-team/ksmbd-tools
Source:         https://github.com/cifsd-team/ksmbd-tools/archive/refs/tags/%{version}.tar.gz

# ksmbd kernel module was only added in kernel 5.15
BuildRequires:  kernel-default >= 5.15
BuildRequires:  glib2-devel
BuildRequires:  libnl3-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:	libtool

Requires(pre):	kernel-default >= 5.15

%description
Set of utilities for creating and managing SMB3 shares for the ksmbd kernel
module.

%prep
%setup -q

%build
./autogen.sh
%configure
%make_build

%install
%make_install
# example conf file is packaged as documentation
rm -f %{buildroot}/%{_sysconfdir}/ksmbd/ksmbd.conf.example

%pre
%service_add_pre ksmbd.service

%post
%service_add_post ksmbd.service

%preun
%service_del_preun ksmbd.service

%postun
%service_del_postun ksmbd.service

%files
%{_sbindir}/*
%{_libexecdir}/ksmbd.tools
%{_unitdir}/ksmbd.service
%dir %{_sysconfdir}/ksmbd
%doc ksmbd.conf.example
%{_mandir}/man8/*
%{_mandir}/man5/*

%changelog
