#
# spec file for package liblastfm-qt6
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


Name:           liblastfm-qt6
Version:        1.2.0git.20250222T104528~81e8f9d
Release:        0
Summary:        Qt 6 port of liblastfm
License:        GPL-3.0-or-later
URL:            https://github.com/Mazhoon/liblastfm
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(samplerate)

%description
liblastfm is a collection of libraries to help you integrate Last.fm services
into your applications.

%package -n liblastfm6-1
Summary:        Qt 6 port of liblastfm

%description -n liblastfm6-1
liblastfm is a collection of libraries to help you integrate Last.fm services
into your applications.

%package devel
Summary:        Development files for liblastfm6
Requires:       liblastfm6-1 = %{version}

%description devel
liblastfm is a collection of libraries to help you integrate Last.fm services
into your applications.
This package provides development files to use Last.fm services in Qt 6
applications.

%prep
%autosetup -p1

%build
%cmake_qt6

%qt6_build

%install
%qt6_install

%check
# Tests need network access

%ldconfig_scriptlets -n liblastfm6-1

%files -n liblastfm6-1
%license COPYING
%doc README.md
%{_qt6_libdir}/liblastfm6.so.*
%{_qt6_libdir}/liblastfm_fingerprint6.so.*

%files devel
%{_includedir}/lastfm6/
%{_qt6_cmakedir}/lastfm6/
%{_qt6_libdir}/liblastfm6.so
%{_qt6_libdir}/liblastfm_fingerprint6.so

%changelog
