#
# spec file for package libQuotient
#
# Copyright (c) 2022 SUSE LLC
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


%define soversion 0_7
%define sonum 0.7
%bcond_with e2ee
Name:           libQuotient
Version:        0.7.0
Release:        0
Summary:        Library for Qt Matrix Clients
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/quotient-im/libQuotient
Source0:        https://github.com/quotient-im/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.9
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
%if %{with e2ee}
BuildRequires:  cmake(Olm)
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
%autosetup -p1

%build
%cmake \
    -DQuotient_INSTALL_TESTS=OFF \
%if %{with e2ee}
    -DQuotient_ENABLE_E2EE=ON
%else
    -DQuotient_ENABLE_E2EE=OFF
%endif

%cmake_build

%install
%cmake_install
# Not useful
rm -r %{buildroot}%{_datadir}/ndk-modules/

%post  -n %{name}%{soversion} -p /sbin/ldconfig
%postun -n %{name}%{soversion} -p /sbin/ldconfig

%files -n %{name}%{soversion}
%doc README.md
%license COPYING
%{_libdir}/libQuotient.so.%{version}
%{_libdir}/libQuotient.so.%{sonum}

%files devel
%doc README.md
%license COPYING
%{_libdir}/pkgconfig/Quotient.pc
%{_libdir}/libQuotient.so
%{_libdir}/cmake/Quotient/
%{_includedir}/Quotient/

%changelog
