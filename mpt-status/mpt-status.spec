#
# spec file for package mpt-status
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mpt-status
Version:        1.2.0
Release:        0
Summary:        Program Showing the Status of LSI 1030 RAID Controller
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://freecode.com/projects/mptstatus
Source:         http://ftp.de.debian.org/debian/pool/main/m/mpt-status/%{name}_%{version}.orig.tar.gz
Patch0:         mpt-status.linux-compiler.patch
BuildRequires:  kernel-source
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program shows the status of the physical and logical drives
attached to a LSI 1030 RAID (mptlinux, fusion, mpt, ioc) controller.

%prep
%setup -q
%patch0 -p1

%build
gcc %{optflags} -I/usr/src/linux/drivers/message/fusion -Iincl mpt-status.c -o mpt-status

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man8
install -m 755 mpt-status %{buildroot}%{_bindir}
install -m 644 man/mpt-status.8 %{buildroot}%{_mandir}/man8

%files
%defattr(-,root,root)
%doc doc/{AUTHORS,Changelog,COPYING,DeveloperNotes,FAQ,README,ReleaseNotes,TODO}
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
