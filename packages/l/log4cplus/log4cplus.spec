#
# spec file for package log4cplus
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           log4cplus
Version:        1.1.0
Release:        0
%define soname  1_1-5
Summary:        C++ logging library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            http://log4cplus.sourceforge.net/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration. It is modeled after the Java log4j API.

%package -n lib%{name}-%{soname}
Summary:        C++ logging library
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}

%description -n lib%{name}-%{soname}
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration. It is modeled after the Java log4j API.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-%{soname} = %{version}

%description devel
This package provides development libraries and headers needed to
build software making use of %{name}

%prep
%setup -q

%build
%configure  --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm %{buildroot}%{_libdir}/*.la

%post   -n lib%{name}-%{soname} -p /sbin/ldconfig
%postun -n lib%{name}-%{soname} -p /sbin/ldconfig

%files -n lib%{name}-%{soname} 
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/log4cplus/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/log4cplus.pc

%changelog
