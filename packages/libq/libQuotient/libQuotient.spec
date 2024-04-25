#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define lib_suffix Qt6
%endif
%define soversion 0_8
%define sonum 0.8
%define rname libQuotient
%bcond_without e2ee
Name:           libQuotient%{?pkg_suffix}
Version:        0.8.2
Release:        0
Summary:        Library for Qt Matrix Clients
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/quotient-im/libQuotient
Source0:        https://github.com/quotient-im/%{rname}/archive/%{version}/%{rname}-%{version}.tar.gz
BuildRequires:  cmake
# c++-20 required
%if 0%{?suse_version} < 1550
BuildRequires:  gcc12-PIE
BuildRequires:  gcc12-c++
%endif
BuildRequires:  pkgconfig
%if 0%{?qt6}
BuildRequires:  qt6-sql-sqlite
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
%else
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.5
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
%endif
%if %{with e2ee}
BuildRequires:  cmake(Olm) >= 3.2.5
BuildRequires:  pkgconfig(openssl)
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Sql)
Requires:       qt6-sql-sqlite
%else
BuildRequires:  cmake(Qt5Sql)
Requires:       libQt5Sql5-sqlite
%endif
%endif

%description
Library for Qt-based Matrix chat clients. It is required by
Quaternion.

%package -n libQuotient%{?qt6:%{lib_suffix}-}%{soversion}
Summary:        Library for Qt Matrix Clients
Group:          System/Libraries

%description -n libQuotient%{?qt6:%{lib_suffix}-}%{soversion}
Library for Qt-based Matrix chat clients. It is required by
Quaternion.

%package -n libQuotient%{?pkg_suffix}-devel
Summary:        Development files for libQuotient
Group:          Development/Libraries/C and C++
Requires:       libQuotient%{?qt6:%{lib_suffix}-}%{soversion} = %{version}
%if 0%{?qt6}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Network)
%if %{with e2ee}
Requires:       cmake(Qt6Sql)
%endif
Requires:       cmake(Qt6Keychain)
%else
Requires:       cmake(Qt5Gui)
Requires:       cmake(Qt5Multimedia)
Requires:       cmake(Qt5Network)
%if %{with e2ee}
Requires:       cmake(Qt5Sql)
%endif
Requires:       cmake(Qt5Keychain)
%endif
Requires:       cmake(Olm)
Requires:       pkgconfig(openssl)
# The devel packages are not coinstallable in the 0.8 release
%if 0%{?qt6}
Conflicts:      libQuotient-devel
%endif

%description -n libQuotient%{?pkg_suffix}-devel
The libQuotient devel package contains libraries and header files for
developing applications that use libQuotient.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?suse_version} < 1550
    export CXX=g++-12
%endif

%if 0%{?qt6}
%cmake_qt6 \
    -DBUILD_WITH_QT6=ON \
    -DBUILD_SHARED_LIBS=ON \
%if 0%{?suse_version} < 1550
    -DCMAKE_C_COMPILER:STRING=gcc-12 \
    -DCMAKE_CXX_COMPILER:STRING=g++-12 \
%endif
%else
%cmake \
%endif
    -DQuotient_INSTALL_TESTS=OFF \
%if %{with e2ee}
    -DQuotient_ENABLE_E2EE=ON
%else
    -DQuotient_ENABLE_E2EE=OFF
%endif

%if 0%{?qt6}
%qt6_build
%else
%cmake_build
%endif

%install
%if 0%{?qt6}
%qt6_install
%else
%cmake_install
%endif

# Not useful
rm -r %{buildroot}%{_datadir}/ndk-modules/

%check
# testolmaccount needs a local server
%ctest --exclude-regex 'testolmaccount'

%ldconfig_scriptlets -n libQuotient%{?qt6:%{lib_suffix}-}%{soversion}

%files -n libQuotient%{?qt6:%{lib_suffix}-}%{soversion}
%doc README.md
%license COPYING
%{_libdir}/libQuotient%{?qt6:%{lib_suffix}}.so.%{version}
%{_libdir}/libQuotient%{?qt6:%{lib_suffix}}.so.%{sonum}

%files -n libQuotient%{?pkg_suffix}-devel
%doc README.md
%license COPYING
%{_libdir}/pkgconfig/Quotient%{?qt6:%{lib_suffix}}.pc
%{_libdir}/libQuotient%{?qt6:%{lib_suffix}}.so
%{_libdir}/cmake/Quotient%{?qt6:%{lib_suffix}}/
%{_includedir}/Quotient/

%changelog
