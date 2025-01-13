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
%define qt6_version 6.4
%else
ExclusiveArch: do_not_build
%endif
%define soversion 0_9
%define sonum 0.9
%define rname libQuotient
Name:           libQuotient%{?pkg_suffix}
Version:        0.9.2
Release:        0
Summary:        Library for Qt Matrix Clients
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/quotient-im/libQuotient
Source0:        https://github.com/quotient-im/%{rname}/archive/%{version}/%{rname}-%{version}.tar.gz
BuildRequires:  cmake >= 3.26
BuildRequires:  pkgconfig
%if 0%{?qt6}
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-sql-sqlite >= %{qt6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
%endif
BuildRequires:  cmake(Olm) >= 3.2.5
BuildRequires:  pkgconfig(openssl)
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}
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
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}
Requires:       cmake(Qt6Sql) >= %{qt6_version}
Requires:       cmake(Qt6Keychain)
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
%if 0%{?qt6}
%cmake_qt6 \
    -DBUILD_SHARED_LIBS=ON \
%endif
    -DQuotient_INSTALL_TESTS=OFF

%if 0%{?qt6}
%qt6_build
%endif

%install
%if 0%{?qt6}
%qt6_install
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
