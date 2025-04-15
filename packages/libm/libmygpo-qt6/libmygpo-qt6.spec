#
# spec file for package libmygpo-qt6
#
# Copyright (c) 2025 SUSE LLC
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


Name:           libmygpo-qt6
Version:        1.2.0git.20250222T125957~4dfa3ba
Release:        0
Summary:        C++/Qt Client Library for gpodder.net
License:        LGPL-2.1-or-later
URL:            https://github.com/Mazhoon/libmygpo-qt
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)

%description
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

%package -n libmygpo-qt6-1
Summary:        C++/Qt Client Library for gpodder.net

%description -n libmygpo-qt6-1
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

%package devel
Summary:        Development files for libmygpo-qt6
Requires:       libmygpo-qt6-1 = %{version}

%description devel
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.
This package provides development files to use gpodder.net services in Qt 6
applications.

%prep
%autosetup -p1

%build
%cmake_qt6 -DBUILD_WITH_QT6:BOOL=TRUE \
%if "%{_lib}" == "lib64"
  -DLIB_SUFFIX:STRING=64
%endif
%{nil}

%qt6_build

%install
%qt6_install

%check
# Needs network access

%ldconfig_scriptlets -n libmygpo-qt6-1

%files -n libmygpo-qt6-1
%license LICENSE
%doc README
%{_qt6_libdir}/libmygpo-qt6.so.*

%files devel
%{_includedir}/mygpo-qt6/
%{_qt6_cmakedir}/mygpo-qt6/
%{_qt6_libdir}/libmygpo-qt6.so
%{_qt6_pkgconfigdir}/libmygpo-qt6.pc

%changelog

