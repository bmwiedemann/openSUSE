#
# spec file for package libqxmpp
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


# Currently not available on 15.4 / 15.5
%if 0%{?suse_version} > 1500
%bcond_without omemo
%endif
%define sover 4
Name:           libqxmpp
Version:        1.5.3
Release:        0
Summary:        Qt XMPP Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/qxmpp-project/qxmpp/
Source0:        https://github.com/qxmpp-project/qxmpp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.7
BuildRequires:  doxygen
BuildRequires:  fdupes
# c++-17 is required
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(gstreamer-1.0)
%if %{with omemo}
BuildRequires:  pkgconfig(libomemo-c)
%endif

%description
QXmpp is a cross-platform C++ XMPP client library based on Qt and C++.

%package -n %{name}%{sover}
Summary:        Qt XMPP Library
Group:          System/Libraries
Provides:       libqxmpp-qt5-0 = %{version}
Obsoletes:      libqxmpp-qt5-0 < %{version}

%description -n %{name}%{sover}
QXmpp is a cross-platform C++ XMPP client library based on Qt and C++.

%package -n %{name}-devel
Summary:        Qxmpp Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       pkgconfig(gstreamer-1.0)
Provides:       libqxmpp-qt5-devel = %{version}
Obsoletes:      libqxmpp-qt5-devel < %{version}

%description -n %{name}-devel
Development package for qxmpp.

%package doc
Summary:        Qxmpp library documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This packages provides documentation of Qxmpp library API.

%prep
%setup -q -n qxmpp-%{version}

%build
%if 0%{?suse_version} <= 1500
  export CXX=g++-10
%endif

%cmake \
  -DWITH_GSTREAMER=ON \
  -DBUILD_DOCUMENTATION=ON \
  -DBUILD_EXAMPLES=ON \
  -DBUILD_TESTS=ON \
%if %{with omemo}
  -DBUILD_OMEMO=ON \
%endif

%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}/doc/qxmpp/

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

# Exclude tests needing a network connection
%{ctest --exclude-regex "tst_(qxmppcallmanager|qxmppiceconnection|qxmppserver|qxmpptransfermanager|qxmppuploadrequestmanager)"}

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSES/*
%doc AUTHORS CHANGELOG.md README.md
%{_libdir}/%{name}.so.*
%if %{with omemo}
%{_libdir}/libQXmppOmemo.so.*
%endif

%files -n %{name}-devel
%{_includedir}/qxmpp/
%{_libdir}/%{name}.so
%{_libdir}/cmake/qxmpp/
%{_libdir}/pkgconfig/qxmpp.pc
%if %{with omemo}
%{_libdir}/libQXmppOmemo.so
%{_libdir}/cmake/QXmppOmemo/
%endif

%files doc
%{_datadir}/doc/qxmpp/

%changelog
