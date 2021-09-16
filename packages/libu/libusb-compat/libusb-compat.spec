#
# spec file for package libusb-compat
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libusb-compat
URL:            http://libusb.info/
Summary:        libusb-1.0 Compatibility Layer for libusb-0.1
License:        BSD-3-Clause AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Version:        0.1.7
Release:        0
Source:         https://github.com/libusb/libusb-compat-0.1/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Source2:        %{name}.rpmlintrc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libusb-1.0)
%define debug_package_requires libusb-0_1-5 = %{version}-%{release}

%description
A compatibility layer allowing applications written for libusb-0.1 to
work with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell
and walk like libusb-0.1.

%package -n libusb-0_1-4
# A better version than 0.1.12 provided by libusb-0_1:
Version:        0.1.13
Release:        0
Summary:        libusb-1.0 Compatibility Library for libusb-0.1
Group:          System/Libraries
# Special symbol for packages, that use libusb-0.1 API, but use libusb-1.0 features:
Provides:       libusb-1_0-features-in-0_1-api
# Update of libusb from openSUSE < 11.1 SLE < 11:
# This symbol is also required by several third party packages!
Provides:       libusb = 0.1.13
Obsoletes:      libusb < 0.1.13
# libusb-compat-hide-libusb-1_0.patch hides this requirement
Requires:       %(rpm -q --provides libusb-1_0-0 | grep libusb-1.0.so.0)

%description -n libusb-0_1-4
A compatibility layer allowing applications written for libusb-0.1 to
work with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell
and walk like libusb-0.1.

%package devel
Summary:        libusb-1.0 Compatibility Layer for libusb-0.1
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libusb-0_1-4 = 0.1.13
Requires:       libusb-1_0-devel
Requires:       libusb-1_0-features-in-0_1-api
# Update of libusb from openSUSE < 11.1 SLE < 11:
Provides:       libusb-devel = 0.1.13
Obsoletes:      libusb-devel < 0.1.13
Conflicts:      libusb-devel < 0.1.13

%description devel
A compatibility layer allowing applications written for libusb-0.1 to
work with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell
and walk like libusb-0.1.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%post -n libusb-0_1-4 -p /sbin/ldconfig

%postun -n libusb-0_1-4 -p /sbin/ldconfig

%files -n libusb-0_1-4
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog LICENSE NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/*-config
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
