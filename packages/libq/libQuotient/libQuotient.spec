#
# spec file for package libQuotient
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


%define soversion 0_6
%bcond_without e2ee
Name:           libQuotient
Version:        0.6.3
Release:        0
Summary:        Library for Qt Matrix Clients
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/quotient-im/libQuotient
Source0:        https://github.com/quotient-im/%{name}/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
%if %{with e2ee}
BuildRequires:  cmake(Olm)
BuildRequires:  pkgconfig(QtOlm)
%endif

%description
Library for Qt-based Matrix chat clients. It is required by
Quaternion.

%package -n %{name}%{soversion}
Summary:        Library for Qt Matrix Clients
Group:          System/Libraries

%description -n %{name}%{soversion}
Library for Qt-based Matrix chat clients. It is required by
Quaternion.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soversion} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%if %{with e2ee}
%cmake -DQuotient_ENABLE_E2EE=ON
%else
%cmake -DQuotient_ENABLE_E2EE=OFF
%endif

%cmake_build

%install
%cmake_install

%post  -n %{name}%{soversion} -p /sbin/ldconfig
%postun -n %{name}%{soversion} -p /sbin/ldconfig

%files -n %{name}%{soversion}
%doc README.md
%license COPYING
%{_libdir}/libQuotient.so.*

%files devel
%doc README.md
%license COPYING
%{_libdir}/pkgconfig/Quotient.pc
%{_libdir}/libQuotient.so
%{_libdir}/cmake/Quotient/
%dir %{_includedir}/Quotient
%dir %{_includedir}/Quotient/csapi
%dir %{_includedir}/Quotient/csapi/definitions
%dir %{_includedir}/Quotient/csapi/definitions/wellknown
%dir %{_includedir}/Quotient/application-service
%dir %{_includedir}/Quotient/application-service/definitions
%dir %{_includedir}/Quotient/identity
%dir %{_includedir}/Quotient/identity/definitions
%dir %{_includedir}/Quotient/jobs
%dir %{_includedir}/Quotient/events
%dir %{_datadir}/ndk-modules
%{_includedir}/Quotient/*.h
%{_includedir}/Quotient/application-service/definitions/*.h
%{_includedir}/Quotient/csapi/*.h
%{_includedir}/Quotient/csapi/definitions/*h
%{_includedir}/Quotient/csapi/definitions/wellknown/*h
%{_includedir}/Quotient/events/*.h
%{_includedir}/Quotient/identity/definitions/*.h
%{_includedir}/Quotient/jobs/*.h
%{_bindir}/quotest
%{_datadir}/ndk-modules/Android.mk

%changelog
