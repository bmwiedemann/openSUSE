#
# spec file for package libqxmpp
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 3
Name:           libqxmpp
Version:        1.3.1
Release:        0
Summary:        Qt XMPP Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/qxmpp-project/qxmpp/
Source0:        https://github.com/qxmpp-project/qxmpp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake >= 3.3
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.7.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vpx)

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
# Disable tests needing a network connection
sed -i 's,add_simple_test(qxmppserver),#add_simple_test(qxmppserver),' tests/CMakeLists.txt
sed -i 's,add_simple_test(qxmppcallmanager),#add_simple_test(qxmppcallmanager),' tests/CMakeLists.txt
sed -i 's,add_simple_test(qxmppiceconnection),#add_simple_test(qxmppiceconnection),' tests/CMakeLists.txt
sed -i 's,add_subdirectory(qxmpptransfermanager),#add_subdirectory(qxmpptransfermanager),' tests/CMakeLists.txt
sed -i 's,add_subdirectory(qxmppuploadrequestmanager),#add_subdirectory(qxmppuploadrequestmanager),' tests/CMakeLists.txt

%build
%cmake \
  -DWITH_SPEEX=ON \
  -DWITH_OPUS=ON \
  -DWITH_THEORA=ON \
  -DWITH_VPX=ON \
  -DWITH_GSTREAMER=ON \
  -DBUILD_DOCUMENTATION=ON \
  -DBUILD_EXAMPLES=ON \
  -DBUILD_TESTS=ON

%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/doc/qxmpp/

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license LICENSE.LGPL
%doc AUTHORS CHANGELOG.md README.md
%{_libdir}/%{name}.so.*

%files -n %{name}-devel
%{_includedir}/qxmpp/
%{_libdir}/%{name}.so
%{_libdir}/cmake/qxmpp/
%{_libdir}/pkgconfig/qxmpp.pc

%files doc
%{_datadir}/doc/qxmpp/

%changelog
