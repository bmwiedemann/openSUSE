#
# spec file for package loadlin
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


Name:           loadlin
Version:        1.6f
Release:        0
Summary:        Linux Loader with Command Line from DOS
License:        GPL-2.0-or-later
Group:          System/Boot
URL:            http://youpibouh.thefreecat.org/loadlin
Source:         http://youpibouh.thefreecat.org/loadlin/loadlin-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86

%description
This is a boot loader for Linux that runs under MS-DOS. It can boot
Linux from a DOS prompt or CONFIG.SYS and fully supports the command
line feature of the Linux kernel. This new version also supports
bzImage+initrd--it can load directly 'high' and can load the RAM disk.
bzImage+initrd (since 1.3.73 in the official kernel) was jointly
developed by Werner Almesberger (LILO) and Hans Lermen (LOADLIN).

%prep

%build

%install
mkdir -p %{buildroot}%{_libexecdir}
tar zxfC $RPM_SOURCE_DIR/%{name}-%{version}.tgz %{buildroot}%{_libexecdir}

%files
%defattr(-,root,root)
%{_libexecdir}/%{name}-%{version}

%changelog
