#
# spec file for package libestr
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libestr
Version:        0.1.11
Release:        0
Summary:        String handling essentials library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libestr.adiscon.com/
Source0:        http://libestr.adiscon.com/files/download/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
This package compiles the string handling essentials library
used by the rsyslog daemon.

%package -n libestr0
Summary:        String handling essentials library
Group:          Development/Libraries/C and C++

%description -n libestr0
This package provides the string handling essentials shared library
used by the rsyslog daemon.

%package devel
Summary:        String handling essentials development files
Group:          Development/Libraries/C and C++
Requires:       libestr0 = %{version}

%description devel
This package provides files required for development with libestr,
the string handling essentials library used by the rsyslog daemon.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libestr0 -p /sbin/ldconfig
%postun -n libestr0 -p /sbin/ldconfig

%files -n libestr0
%license COPYING
%{_libdir}/libestr.so.0*

%files devel
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{_libdir}/libestr.so
%{_libdir}/pkgconfig/libestr.pc
%{_includedir}/libestr.h

%changelog
