#
# spec file for package qt6-networkauth
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


%define real_version 6.7.2
%define short_version 6.7
%define short_name qtnetworkauth
%define tar_name qtnetworkauth-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-networkauth%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Set of APIs to obtain limited access to online accounts and HTTP services
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-networkauth-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Network Authorization provides a set of APIs that enable Qt
applications to obtain limited access to online accounts and HTTP
services without exposing users' passwords.

%if !%{qt6_docs_flavor}

%package -n libQt6NetworkAuth6
Summary:        Qt 6 NetworkAuth library

%description -n libQt6NetworkAuth6
The Qt 6 NetworkAuth library.

%package devel
Summary:        Qt 6 NetworkAuth library - Development files
Requires:       libQt6NetworkAuth6 = %{version}
Requires:       cmake(Qt6Network) = %{real_version}

%description devel
Development files for the Qt 6 NetworkAuth library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 NetworkAuth Library
Requires:       cmake(Qt6NetworkAuth) = %{real_version}

%description private-devel
This package provides private headers of libQt6NetworkAuth that do not have any
ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%ldconfig_scriptlets -n libQt6NetworkAuth6

%files -n libQt6NetworkAuth6
%license LICENSES/*
%{_qt6_libdir}/libQt6NetworkAuth.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtNetworkAuthTestsConfig.cmake
%{_qt6_cmakedir}/Qt6NetworkAuth/
%{_qt6_descriptionsdir}/NetworkAuth.json
%{_qt6_includedir}/QtNetworkAuth/
%{_qt6_libdir}/libQt6NetworkAuth.prl
%{_qt6_libdir}/libQt6NetworkAuth.so
%{_qt6_metatypesdir}/qt6networkauth_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_networkauth.pri
%{_qt6_pkgconfigdir}/Qt6NetworkAuth.pc
%exclude %{_qt6_includedir}/QtNetworkAuth/%{real_version}

%files private-devel
%{_qt6_includedir}/QtNetworkAuth/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_networkauth_private.pri

%endif

%changelog
