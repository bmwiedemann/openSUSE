#
# spec file for package libieee1284
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 3
%define soname %{sover}
%define libname libieee1284%{soname}
Name:           libieee1284
Version:        0.2.11
Release:        0
Summary:        A Library for Interfacing IEEE 1284-Compatible Devices
License:        GPL-2.0-or-later AND MIT
Group:          System/Libraries
URL:            https://cyberelk.net/tim/software/libieee1284/
#Git-Clone:     https://github.com/twaugh/libieee1284.git
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://cyberelk.net/tim/libieee1284/interface.pdf
Source2:        baselibs.conf
Patch1:         libieee1284-strict-aliasing.patch
BuildRequires:  fdupes

%description
This library is intended to be used by applications that need to
communicate with (or at least identify) devices that are attached via a
parallel port.

For Linux, there are some wrinkles in communicating with devices on
parallel ports (see %{_docdir}/libieee1284/README). The
aim of this library is to take all the worry about these wrinkles from
the application.  It figures out which method is appropriate for the
currently running kernel.  For instance, if the application wants to
know the device ID of a device on a particular port, it asks the
library for the the device ID. The library then figures out if it is
available via /proc (in any of the possible locations) and, if not,
tries asking the device itself. If /dev/parport0 is not available for
use, it tries ioperm; if that fails, it tries /dev/port. The
application does not have to care.

%package -n %{libname}
Summary:        A Library for Interfacing IEEE 1284-Compatible Devices
Group:          System/Libraries

%description -n %{libname}
This library is intended to be used by applications that need to
communicate with (or at least identify) devices that are attached via a
parallel port.

%package devel
Summary:        Development files for libieee1284
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for libieee1284, a Library for Interfacing IEEE
1284-Compatible Devices.

%prep
%setup -q
%patch1 -p1
cp %{SOURCE1} .

%build
%configure \
  --disable-static \
  --without-python
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# create symbolic links to the actual library
ln -sf %{buildroot}/%{_libdir}/libieee1284.so.3.2.1 libieee1284.so.3
ln -sf %{buildroot}/%{_libdir}/libieee1284.so.3.2.1 libieee1284.so
%fdupes -s %{buildroot}

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/libieee1284.so.%{sover}*

%files devel
%doc interface.pdf
%{_bindir}/libieee1284_test
%{_includedir}/ieee1284.h
%{_libdir}/libieee1284.so
%{_mandir}/man3/libieee1284.3%{?ext_man}
%{_mandir}/man3/ieee1284_*.3%{?ext_man}
%{_mandir}/man3/parport*.3%{?ext_man}

%changelog
