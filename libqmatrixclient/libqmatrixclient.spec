#
# spec file for package libqmatrixclient
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
%define soname libQMatrixClient
%define soversion 0_5_1

Name:           libqmatrixclient
Version:        0.5.1.2
Release:        0
Summary:        Library for Qt Matrix Clients
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
Url:            https://github.com/QMatrixClient/libqmatrixclient
Source0:        https://github.com/QMatrixClient/libqmatrixclient/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)

%description
Library for Qt-based Matrix chat clients. It is required by
Quaternion.

%package -n %{soname}%{soversion}
Summary:        Library for Qt Matrix Clients
Group:          System/Libraries

%description -n %{soname}%{soversion}
Library for Qt-based Matrix chat clients. It is required by
Quaternion.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{soversion} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%if 0%{?suse_version} < 1500
export CC="gcc-7"
export CXX="g++-7"
%endif
%cmake

%install
%cmake_install
# need for other clients like quaternion
mkdir -p %{buildroot}%{_datadir}/QMatrixClient

%post  -n %{soname}%{soversion} -p /sbin/ldconfig
%postun -n %{soname}%{soversion} -p /sbin/ldconfig

%files -n %{soname}%{soversion}
%doc README.md
%license COPYING
%dir %{_datadir}/QMatrixClient
%{_libdir}/libQMatrixClient.so.*

%files devel
%doc README.md
%license COPYING
%{_libdir}/pkgconfig/QMatrixClient.pc
%{_libdir}/libQMatrixClient.so
%{_libdir}/cmake/QMatrixClient/
%dir %{_includedir}/csapi
%dir %{_includedir}/csapi/definitions
%dir %{_includedir}/csapi/definitions/wellknown
%dir %{_includedir}/application-service
%dir %{_includedir}/application-service/definitions
%dir %{_includedir}/identity
%dir %{_includedir}/identity/definitions
%dir %{_includedir}/jobs
%dir %{_includedir}/events
%{_includedir}/*.h
%{_includedir}/application-service/definitions/*.h
%{_includedir}/csapi/*.h
%{_includedir}/csapi/definitions/*h
%{_includedir}/csapi/definitions/wellknown/*h
%{_includedir}/events/*.h
%{_includedir}/identity/definitions/*.h
%{_includedir}/jobs/*.h
%{_bindir}/qmc-example

%changelog
