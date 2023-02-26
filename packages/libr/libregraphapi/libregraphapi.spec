#
# spec file for package libregraphapi
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


%define sover 1
Name:           libregraphapi
Version:        1.0.1
Release:        0
Summary:        A client library for the LibreGraphAPI library
License:        Apache-2.0
URL:            https://github.com/owncloud/libre-graph-api-cpp-qt-client
Source:         https://github.com/owncloud/libre-graph-api-cpp-qt-client/archive/v%{version}.tar.gz#/libre-graph-api-cpp-qt-client-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-cmake_fixes.patch
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)

%description
Libregraphapi is a MS Graph API influenced API for cloud collaboration.

%package -n libLibreGraphAPI%{sover}
Summary:        A client library for the LibreGraphAPI library

%description -n libLibreGraphAPI%{sover}
Libregraphapi is a MS Graph API influenced API for cloud collaboration.

%package devel
Summary:        Development files for the libregraphAPI library
Requires:       libLibreGraphAPI%{sover} = %{version}

%description devel
Libregraphapi is a MS Graph API influenced API for cloud collaboration.

This package contains development files for libregraphapi.

%prep
%autosetup -p1 -n libre-graph-api-cpp-qt-client-%{version}

%build
cd client
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
cd client
%cmake_install

%ldconfig_scriptlets -n libLibreGraphAPI%{sover}

%files -n libLibreGraphAPI%{sover}
%license LICENSE
%doc README.md
%{_libdir}/libLibreGraphAPI.so.%{sover}
%{_libdir}/libLibreGraphAPI.so.%{version}

%files devel
%{_includedir}/OpenAPI
%{_libdir}/cmake/LibreGraphAPI
%{_libdir}/libLibreGraphAPI.so

%changelog
