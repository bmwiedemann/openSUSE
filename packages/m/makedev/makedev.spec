#
# spec file for package makedev
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           makedev
Version:        2.6
Release:        0
Summary:        Script for Creating Device Files in /dev
License:        GPL-2.0+
Group:          System/Fhs
Url:            http://www.lanana.org/docs/device-list/
Source:         MAKEDEV-%{version}.tar.bz2
Patch0:         %{name}-%{version}.diff
Patch1:         %{name}-%{version}-chown.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the MAKEDEV script, which makes it easy to create
and maintain the files in the /dev directory.

You do not need this script on SUSE Linux, but it is needed for FHS
2.1.

%prep
%setup -q -n MAKEDEV-%{version}
%patch0
%patch1

%build

%install
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}%{_mandir}/man8
make MANDIR=%{buildroot}%{_mandir} ROOT=%{buildroot} install

%files
%defattr(-,root,root)
/sbin/MAKEDEV
%{_mandir}/man8/MAKEDEV.8.gz

%changelog
