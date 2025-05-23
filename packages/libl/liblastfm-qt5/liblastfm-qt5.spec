#
# spec file for package liblastfm-qt5
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


Name:           liblastfm-qt5
Version:        1.1.0
Release:        0
Summary:        A Qt C++ Library for the Last.fm Webservices
License:        GPL-3.0-or-later
URL:            https://github.com/lastfm/liblastfm/
Source:         https://github.com/lastfm/liblastfm/archive/%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM
Patch0:         0001-Make-Qt5-build-default-and-simplify-logic-add-missin.patch
# PATCH-FIX-UPSTREAM
Patch1:         0004-Fix-build-with-Qt-5.11_beta3-drop-qt5_use_modules.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Stick-to-c-14-for-liblastfm.patch
# PATCH-FIX-UPSTREAM
Patch3:         liblastfm-cmake4.patch
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)

%description
liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package -n liblastfm5-1
Summary:        A Qt C++ Library for the Last.fm Webservices

%description -n liblastfm5-1
liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package -n liblastfm_fingerprint5-1
Summary:        A Qt C++ Library for the Last.fm Webservices

%description -n liblastfm_fingerprint5-1
liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package devel
Summary:        Development Files for the Last.fm Webservices
Requires:       liblastfm5-1 = %{version}
Requires:       liblastfm_fingerprint5-1 = %{version}
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5DBus)
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5Xml)

%description devel
liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

This package contains development files for liblastfm.

%prep
%autosetup -p1 -n liblastfm-%{version}

%build
%cmake \
  -DBUILD_WITH_QT4=OFF \
  -DBUILD_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n liblastfm5-1
%ldconfig_scriptlets -n liblastfm_fingerprint5-1

%files -n liblastfm5-1
%license COPYING
%doc README.md
%{_libdir}/liblastfm5.so.*

%files -n liblastfm_fingerprint5-1
%license COPYING
%{_libdir}/liblastfm_fingerprint5.so.*

%files devel
%license COPYING
%{_libdir}/liblastfm5.so
%{_libdir}/liblastfm_fingerprint5.so
%{_includedir}/lastfm5/

%changelog
