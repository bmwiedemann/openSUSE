#
# spec file for package libqxmpp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define qt6_version 6.4.0

%define sover 10
Name:           libqxmpp
Version:        1.16.1
Release:        0
Summary:        Qt XMPP Library
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/qxmpp
Source0:        https://download.kde.org/unstable/qxmpp/qxmpp-%{version}.tar.xz
Source1:        https://download.kde.org/unstable/qxmpp/qxmpp-%{version}.tar.xz.sig
Source2:        qxmpp.keyring
BuildRequires:  fdupes
# The default GCC version is too old in Leap 16
%if 0%{?suse_version} >= 1600 && 0%{?suse_version} < 1699
BuildRequires:  gcc15-PIE
BuildRequires:  gcc15-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.20
BuildRequires:  pkgconfig(libomemo-c)
BuildRequires:  pkgconfig(openssl) >= 3.0

%description
QXmpp is a cross-platform C++ XMPP client library based on Qt and C++.

%package -n libQXmppQt6-%{sover}
Summary:        Qt XMPP Library
Obsoletes:      libqxmpp-doc < 1.16.1

%description -n libQXmppQt6-%{sover}
QXmpp is a cross-platform C++ XMPP client library based on Qt and C++.

%package -n libQXmppQt6-devel
Summary:        Qxmpp Development Files
Requires:       libQXmppQt6-%{sover} = %{version}
Requires:       pkgconfig(gstreamer-1.0)
# Old package for backward compatibility
Obsoletes:      libqxmpp-devel < %{version}

%description -n libQXmppQt6-devel
Development package for qxmpp.

%prep
%autosetup -p1 -n qxmpp-%{version}

%build
%cmake_qt6 \
  -DBUILD_DOCUMENTATION:BOOL=FALSE \
  -DBUILD_TESTING:BOOL=TRUE \
  -DBUILD_EXAMPLES:BOOL=FALSE \
%if 0%{?suse_version} >= 1600 && 0%{?suse_version} < 1699
  -DCMAKE_C_COMPILER:STRING=gcc-15 \
  -DCMAKE_CXX_COMPILER:STRING=g++-15
%endif
%{nil}

%qt6_build

%install
%qt6_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

# Exclude tests needing a network connection
%{ctest --exclude-regex "tst_(QXmppIceConnection|QXmppTransferManager)"}

%ldconfig_scriptlets -n libQXmppQt6-%{sover}

%files -n libQXmppQt6-%{sover}
%license LICENSES/*
%doc AUTHORS CHANGELOG.md README.md
%{_libdir}/libQXmppQt6.so.*
%{_libdir}/libQXmppOmemoQt6.so.*

%files -n libQXmppQt6-devel
%{_includedir}/QXmppQt6/
%{_libdir}/cmake/QXmppQt6/
%{_libdir}/cmake/QXmppOmemoQt6/
%{_libdir}/libQXmppQt6.so
%{_libdir}/libQXmppOmemoQt6.so
%{_libdir}/pkgconfig/QXmppQt6.pc

%changelog
