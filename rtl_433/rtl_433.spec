#
# spec file for package rtl_433
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define version_unconverted 18.05+git.20180806
Name:           rtl_433
Version:        18.05+git.20180806
Release:        0
Summary:        Turns RTL2832 dongle into a 433.92MHz generic data receiver
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/merbanan/rtl_433.git
Source:         %{name}-%{version}.tar.xz
Patch0:         rtl_433-disable-test.diff
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(librtlsdr)

%description
An application using librtlsdr to decode the temperature from
wireless temperature sensors (433.92MHz)

%package devel
Summary:        Turns RTL2832 dongle into a 433.92MHz generic data receiver
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Turns RTL2832 dongle into a 433.92MHz generic data receiver.

This subpackage contains header files for developing applications that want
to make use of rtl_433.

%prep
%setup -q
%patch0 -p1

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS README.md
%{_bindir}/rtl_433

%files devel
%{_includedir}/rtl_433.h
%{_includedir}/rtl_433_devices.h

%changelog
