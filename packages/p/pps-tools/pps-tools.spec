#
# spec file for package pps-tools
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


%define version_unconverted 0.0.0+git.20181203
Name:           pps-tools
Version:        0.0.0+git.20181203
Release:        0
Summary:        Userspace tools for the Linux Pulse Per Second subsystem
License:        GPL-2.0-or-later
URL:            http://linuxpps.org
Source:         %{name}-%{version}.tar.xz

%description
Userland tools to test Linux kernel PPS API. See Documentations/pps/pps.txt
for reference.

%package devel
Summary:        Development files for the LinuxPPS API

%description devel
This subpackage contains a header-only C API providing a number of
inline C functions that call out to the kernel's Pulse Per Second
API. It is, for example, used by ntpd to interact with timing
devices.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
%make_build

%install
# for some reason rebuild occurs during installation
# we need to be sure that optflags are still honored
export CFLAGS="%{optflags}"
%make_install

%files
%license COPYING
%{_bindir}/ppsctl
%{_bindir}/ppsfind
%{_bindir}/ppsldisc
%{_bindir}/ppstest
%{_bindir}/ppswatch

%files devel
%license COPYING
%{_includedir}/sys/timepps.h

%changelog
