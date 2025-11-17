#
# spec file for package libqxmpp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define sover 7
Name:           libqxmpp
Version:        1.12.0
Release:        0
Summary:        Qt XMPP Library
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/qxmpp
Source0:        https://download.kde.org/unstable/qxmpp/qxmpp-%{version}.tar.xz
Source1:        https://download.kde.org/unstable/qxmpp/qxmpp-%{version}.tar.xz.sig
Source2:        qxmpp.keyring
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libomemo-c)

%description
QXmpp is a cross-platform C++ XMPP client library based on Qt and C++.

%package -n libQXmppQt6-%{sover}
Summary:        Qt XMPP Library

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

# No need to build it twice

%package -n libqxmpp-doc
Summary:        Qxmpp library documentation
BuildArch:      noarch

%description -n libqxmpp-doc
This packages provides documentation of Qxmpp library API.

%prep
%autosetup -p1 -n qxmpp-%{version}

%build
# Due to the cmake maintainers bad idea, CMAKE_INSTALL_DOCDIR has to be redefined
%cmake_qt6 \
  -DWITH_GSTREAMER=ON \
  -DCMAKE_INSTALL_DOCDIR=%{_datadir}/doc/qxmpp \
  -DBUILD_DOCUMENTATION=ON \
  -DBUILD_TESTS=ON \
  -DBUILD_OMEMO=ON

%qt6_build

%install
%qt6_install

%fdupes %{buildroot}%{_datadir}/doc/qxmpp/

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

# Exclude tests needing a network connection
%{ctest --exclude-regex "tst_(qxmppcallmanager|qxmppiceconnection|qxmppserver|qxmpptransfermanager|qxmppuploadrequestmanager)"}

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

%files -n libqxmpp-doc
%{_datadir}/doc/qxmpp/

%changelog
