#
# spec file for package log4cplus
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


%define soname  1_2-5
Name:           log4cplus
Version:        2.0.5
Release:        0
Summary:        C++ logging library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            http://log4cplus.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/log4cplus/log4cplus-stable/%{version}/%{name}-%{version}.tar.xz
Source2:        https://downloads.sourceforge.net/project/log4cplus/log4cplus-stable/%{version}/%{name}-%{version}.tar.xz.sig
Source3:        %{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz

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
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n lib%{name}-%{soname} -p /sbin/ldconfig
%postun -n lib%{name}-%{soname} -p /sbin/ldconfig

%files -n lib%{name}-%{soname}
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%license COPYING
%{_includedir}/log4cplus/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/log4cplus.pc

%changelog
