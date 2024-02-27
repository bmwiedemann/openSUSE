#
# spec file for package freesrp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 0
%define libname lib%{name}%{sover}
Name:           freesrp
Version:        0.3.0
Release:        0
Summary:        Library and tools for the FreeSRP SDR transceiver
License:        GPL-3.0
Group:          Productivity/Hamradio/Other
Url:            http://freesrp.org/
#Git-Clone:     https://github.com/FreeSRP/libfreesrp.git
Source:         https://github.com/FreeSRP/libfreesrp/archive/%{version}.tar.gz#/libfreesrp-%{version}.tar.xz
Patch0:         freesrp-cmake-libsuffix.diff
Patch1:         freesrp-fix-pthread-linking-issue.diff
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
A C++ library that uses libusb to program and configure the
FreeSRP hardware and both receive and transmit RF signals.

%package devel
Summary:        Development files for libfreesrp
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libraries and header files for developing applications that want to
make use of libfreesrp.

%package -n %{libname}
Summary:        Library for FreeSRP
Group:          System/Libraries
Requires:       %{name}-udev

%description -n %{libname}
libfreesrp is a C++ library that uses libusb to program and
configure the FreeSRP hardware and both receive and transmit RF signals.

%package udev
Summary:        Udev rules for FreeSRP
Group:          Hardware/Other

%description udev
Udev rules for FreeSRP SDR hardware

%prep
%autosetup -p1 -n libfreesrp-%{version}

%build
export CXXFLAGS='%{optflags} -Wno-return-type'
%cmake
%make_jobs

%install
%cmake_install
install -Dpm0644 87-electronics-kitchen.rules %{buildroot}%{_udevrulesdir}/87-electronics-kitchen.rules

%post -n %{libname} -p /sbin/ldconfig
%postun  -n %{libname} -p /sbin/ldconfig
%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING README.md
%{_bindir}/freesrp-ctl
%{_bindir}/freesrp-io
%{_libdir}/libfreesrp.so.*

%files udev
%defattr(-,root,root)
%{_udevrulesdir}/87-electronics-kitchen.rules

%files devel
%defattr(-,root,root)
%{_libdir}/libfreesrp.so
%{_includedir}/freesrp.hpp

%changelog
