#
# spec file for package maliit-framework
#
# Copyright (c) 2022 SUSE Software Solutions Germany GmbH, Nuernberg, Germany.
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


%define _libname_base libmaliit
%define _minsover 3.0
%define _sover 2
%define _name framework

Name:           maliit-framework
Version:        2.3.0
Release:        0
License:        LGPL-2.1-only
Summary:        Maliit input method framework
Group:          System/GUI/Other
Url:            https://github.com/maliit/framework
Source0:        https://github.com/maliit/%{_name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE maliit-framework-2.3.0-fix-ut_mimserveroptions-test-case-with-GCC-12-ADL.patch ionic@ionic.de -- Fixes building the test cases with GCC 12+.
Patch0:         maliit-framework-2.3.0-fix-ut_mimserveroptions-test-case-with-GCC-12-ADL.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5XkbCommonSupport)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  doxygen
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel

%description
Maliit provides a flexible and cross-platform input method framework.
It has a plugin-based client-server architecture where applications
act as clients and communicate with the Maliit server via input
context plugins. The communication link currently uses D-Bus. Maliit
is an open source framework (LGPL 2) with open source plugins (BSD).
This package also provides plugin support.

%package        doc
Summary:        Maliit Framework documentation
Group:          Documentation/HTML
%description    doc
Provides doxygen documentation for the Maliit Framework.

%package     -n %{_libname_base}-devel
Summary:        Maliit Framework development packages
Group:          Development/Libraries/C and C++
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < %{version}
Requires:       %{_libname_base}-plugins%{_sover} = %{version}-%{release}
Requires:       %{_libname_base}-glib%{_sover} = %{version}-%{release}
%description -n %{_libname_base}-devel
Provides headers and CMake files built for the Maliit Framework.

%package     -n %{_libname_base}-plugins%{_sover}
Summary:        Maliit Framework plugins shared library
Group:          System/GUI/Other
Requires:       %{name}
Obsoletes:      %{_libname_base}0 < %{version}
%description -n %{_libname_base}-plugins%{_sover}
Provides the plugin-related shared libraries built for the Maliit
Framework.

%package     -n %{_libname_base}-glib%{_sover}
Summary:        Maliit Framework glib shared library
Group:          System/GUI/Other
Requires:       %{name}
Obsoletes:      %{_libname_base}0 < %{version}
%description -n %{_libname_base}-glib%{_sover}
Provides the glib-related shared libraries built for the Maliit
Framework.

%package        tests
Summary:        Maliit Framework tests
Group:          System/GUI/Other
%description    tests
Provides unit tests of the Maliit Framework.

%prep
%autosetup -p1 -n %{_name}-%{version}/

%build
%cmake  -Denable-dbus-activation=ON \
        -Denable-hwkeyboard=ON \
        -Denable-qt5-inputcontext=ON \
        -Denable-wayland=ON \
        -Denable-xcb=ON \
        -Denable-glib=ON \
        -Denable-tests=ON \
        -Denable-docs=ON \
        -Denable-examples=OFF \
        -Dinstall-tests=ON
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_prefix}

%ldconfig_scriptlets -n %{_libname_base}-plugins%{_sover}
%ldconfig_scriptlets -n %{_libname_base}-glib%{_sover}

%files doc
%{_datadir}/doc/maliit-framework-doc/
%{_datadir}/doc/maliit-framework/

%files -n %{_libname_base}-devel
%{_includedir}/maliit-2
%{_libdir}/cmake/{MaliitGLib,MaliitPlugins}/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libmaliit-plugins.so
%{_libdir}/libmaliit-glib.so
%{_libdir}/qt5/mkspecs/features/*.prf

%files tests
%{_libdir}/maliit-framework-tests

%files -n %{_libname_base}-plugins%{_sover}
%{_libdir}/libmaliit-plugins.so.%{_sover}
%{_libdir}/libmaliit-plugins.so.%{_sover}.%{_minsover}

%files -n %{_libname_base}-glib%{_sover}
%{_libdir}/libmaliit-glib.so.%{_sover}
%{_libdir}/libmaliit-glib.so.%{_sover}.%{_minsover}

%files
%doc README.md
%license LICENSE.LGPL
%{_bindir}/maliit-server
%{_libdir}/qt5/plugins/platforminputcontexts/libmaliitplatforminputcontextplugin.so
%{_libdir}/qt5/plugins/wayland-shell-integration/libinputpanel-shell.so
%{_datadir}/dbus-1/services/org.maliit.server.service

%changelog
