#
# spec file for package ivykis
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


%define lname   libivykis0
Name:           ivykis
Version:        0.42.4
Release:        0
Summary:        An event dispatching library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://sourceforge.net/projects/libivykis/
Source:         https://downloads.sf.net/libivykis/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
libivykis is a thin wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and is
mainly intended for writing portable high-performance network
servers.

%package -n %{lname}
Summary:        An event dispatching library
Group:          System/Libraries

%description -n %{lname}
libivykis is a thin wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and is
mainly intended for writing portable high-performance network
servers.

%package devel
Summary:        Development files for libivykis, an event dispatching library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libivykis is a thin wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and is
mainly intended for writing portable high-performance network
servers.

This package contains the header files and development symlinks.

%prep
%setup -q

%build
%configure --disable-static --includedir=%{_includedir}/%{name}-%{version}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libivykis.so.0*

%files devel
%{_includedir}/%{name}-%{version}
%{_libdir}/libivykis.so
%{_libdir}/pkgconfig/ivykis.pc
%{_mandir}/man3/iv*.3%{?ext_man}
%{_mandir}/man3/IV*.3%{?ext_man}

%changelog
