#
# spec file for package libqxmpp
#
# Copyright (c) 2024 SUSE LLC
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
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt5"
%define qt5 1
%define pkg_suffix -qt5
%define lib_suffix Qt5
%endif
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define lib_suffix Qt6
%endif
%define sover 5
Name:           libqxmpp%{?pkg_suffix}
Version:        1.9.1
Release:        0
Summary:        Qt XMPP Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/qxmpp-project/qxmpp/
Source0:        https://github.com/qxmpp-project/qxmpp/archive/v%{version}.tar.gz#/libqxmpp-%{version}.tar.gz
BuildRequires:  cmake
%if 0%{?qt5}
BuildRequires:  doxygen
BuildRequires:  fdupes
%endif
# c++-17 is required
%if 0%{?suse_version} < 1550
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%endif
BuildRequires:  pkgconfig
%if 0%{?qt5}
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)
%else
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
%endif
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libomemo-c)

%description
QXmpp is a cross-platform C++ XMPP client library based on Qt and C++.

%package -n libQXmpp%{lib_suffix}-%{sover}
Summary:        Qt XMPP Library
Group:          System/Libraries
Provides:       libqxmpp-qt5-0 = %{version}
Obsoletes:      libqxmpp-qt5-0 < %{version}
# Renamed in the 1.5.4 release
%if 0%{?qt5}
Provides:       libqxmpp4 = %{version}
Obsoletes:      libqxmpp4 < %{version}
%endif

%description -n libQXmpp%{lib_suffix}-%{sover}
QXmpp is a cross-platform C++ XMPP client library based on Qt and C++.

%package -n libQXmpp%{lib_suffix}-devel
Summary:        Qxmpp Development Files
Group:          Development/Libraries/C and C++
Requires:       libQXmpp%{lib_suffix}-%{sover} = %{version}
Requires:       libqxmpp-devel = %{version}
Requires:       pkgconfig(gstreamer-1.0)
%if 0%{?qt5}
Provides:       libqxmpp-qt5-devel = %{version}
Obsoletes:      libqxmpp-qt5-devel < %{version}
%endif

%description -n libQXmpp%{lib_suffix}-devel
Development package for qxmpp.

%if 0%{?qt5}
# Backward compatibility module, it can be used for both Qt5 and Qt6 variants
%package -n libqxmpp-devel
Summary:        Compatibility helper for libqxmpp
Requires:       (libQXmppQt5-devel = %{version} if libQt5Core-devel)
Requires:       (libQXmppQt6-devel = %{version} if qt6-core-devel)

%description -n libqxmpp-devel
This package provides a backward compatibility helper for CMake users.
If 'QT_VERSION_MAJOR' is not set in the dependent package, the CMake module
will try to determine the needed QXmpp variant based on which Qt version was
already found by CMake.



# No need to build it twice
%package -n libqxmpp-doc
Summary:        Qxmpp library documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description -n libqxmpp-doc
This packages provides documentation of Qxmpp library API.
%endif

%prep
%autosetup -p1 -n qxmpp-%{version}

%build
%if 0%{?suse_version} < 1550
  export CXX=g++-13
%endif

# Due to the cmake maintainers bad idea, CMAKE_INSTALL_DOCDIR has to be redefined
%cmake \
  -DWITH_GSTREAMER=ON \
%if 0%{?qt5}
  -DCMAKE_INSTALL_DOCDIR=%{_datadir}/doc/qxmpp \
  -DBUILD_DOCUMENTATION=ON \
%endif
  -DBUILD_TESTS=ON \
  -DBUILD_OMEMO=ON

%cmake_build

%install
%cmake_install

%if 0%{?qt5}
%fdupes %{buildroot}%{_datadir}/doc/qxmpp/
%endif

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

# Exclude tests needing a network connection
%{ctest --exclude-regex "tst_(qxmppcallmanager|qxmppiceconnection|qxmppserver|qxmpptransfermanager|qxmppuploadrequestmanager)"}

%ldconfig_scriptlets -n libQXmpp%{lib_suffix}-%{sover}

%files -n libQXmpp%{lib_suffix}-%{sover}
%license LICENSES/*
%doc AUTHORS CHANGELOG.md README.md
%{_libdir}/libQXmpp%{lib_suffix}.so.*
%{_libdir}/libQXmppOmemo%{lib_suffix}.so.*

%files -n libQXmpp%{lib_suffix}-devel
%{_includedir}/QXmpp%{lib_suffix}/
%{_libdir}/libQXmpp%{lib_suffix}.so
%{_libdir}/libQXmppOmemo%{lib_suffix}.so
%{_libdir}/cmake/QXmpp%{lib_suffix}/
%{_libdir}/cmake/QXmppOmemo%{lib_suffix}/
%{_libdir}/pkgconfig/QXmpp%{lib_suffix}.pc
%if 0%{?qt5}
%{_libdir}/pkgconfig/qxmpp.pc
%endif

%if 0%{?qt5}
%files -n libqxmpp-devel
%{_libdir}/cmake/QXmpp/

%files -n libqxmpp-doc
%{_datadir}/doc/qxmpp/
%endif

%changelog
