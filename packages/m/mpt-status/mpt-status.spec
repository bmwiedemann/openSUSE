#
# spec file for package mpt-status
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


Name:           mpt-status
Version:        1.2.0
Release:        0
Summary:        Program Showing the Status of LSI 1030 RAID Controller
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://freecode.com/projects/mptstatus
Source:         http://ftp.de.debian.org/debian/pool/main/m/mpt-status/%{name}_%{version}.orig.tar.gz
Patch0:         mpt-status.linux-compiler.patch
BuildRequires:  kernel-source

%description
This program shows the status of the physical and logical drives attached
to a LSI 1030 RAID (mptlinux, fusion, mpt, ioc) controller.

%prep
%autosetup -p1

%build
cc %{optflags} -I/usr/src/linux/drivers/message/fusion -Iincl mpt-status.c -o mpt-status

%install
install -Dpm 0755 mpt-status \
  %{buildroot}%{_bindir}/mpt-status
install -Dpm 0644 man/mpt-status.8 \
  %{buildroot}%{_mandir}/man8/mpt-status.8

%files
%license doc/{COPYING,AUTHORS}
%doc doc/{Changelog,DeveloperNotes,FAQ,README,ReleaseNotes,TODO}
%{_bindir}/mpt-status
%{_mandir}/man8/*

%changelog
