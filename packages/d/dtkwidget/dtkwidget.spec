#
# spec file for package dtkwidget
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
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


%define libver 5
%define apiver 5.5.0
%define gtest_version %(rpm -q --queryformat '%%{VERSION}' gtest)

Name:           dtkwidget
Version:        5.5.52
Release:        0
Summary:        Deepin graphical user interface library
License:        LGPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        https://github.com/linuxdeepin/dtkwidget/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTEAM dtkwidget-fix-lost-pkgconfig.patch hillwood@opensuse.org - fix lost pkgconfig
Patch0:         dtkwidget-fix-lost-pkgconfig.patch
BuildRequires:  dtkcommon
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkcore) >= 5.5.0
BuildRequires:  pkgconfig(dtkgui) >= 5.5.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepint Tool Kit (Dtk) is the base devlopment tool of all C++/Qt Developer
work on Deepin.

%package -n lib%{name}%{libver}
Summary:        Libraries for dtkwidget
Group:          System/Libraries
Recommends:     %{name}-lang

%description -n lib%{name}%{libver}
The dtkwidget-devel package contains the header files and developer
docs for dtkcore.

%package devel
Summary:        Development tools for dtkwidget
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{libver} = %{version}

%description devel
The dtkwidget-devel package contains the header files and developer
docs for dtkcore.

%lang_package

%prep
%autosetup -p1
%if "%{gtest_version}" >= "1.14.0"
sed -i 's|c++11|c++14|g' examples/dwidget-examples/collections/collections.pro \
plugin/dtkuidemo/dtkuidemo.pro \
src/lib.pri \
src/widgets/private/keyboardmonitor/keyboardmonitor.pri \
src/widgets/private/startupnotifications/startupnotifications.pri \
tools/svgc/svgc.pro
%endif

%build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%qmake5_install

# Remove useless files
rm -rf %{buildroot}/usr/tests

%fdupes %{buildroot}

%post -n lib%{name}%{libver} -p /sbin/ldconfig

%postun -n lib%{name}%{libver} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libdtk-%{apiver}
%dir %{_libdir}/examples
%{_libdir}/examples/collections

%files -n lib%{name}%{libver}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so.*

%files devel
%doc README.md CHANGELOG.md
%license LICENSE
%defattr(-,root,root,-)
%dir %{_includedir}/libdtk-*
%{_includedir}/libdtk-*/DWidget
%{_libdir}/pkgconfig/%{name}.pc
# %{_libdir}/pkgconfig/%{name}%{pkg_ver}.pc
%{_libdir}/lib%{name}.so
%dir %{_libdir}/cmake
%{_libdir}/cmake/*
%dir %{_libdir}/qt5
%dir %{_libdir}/qt5/mkspecs
%{_libdir}/qt5/mkspecs/modules

%files lang
%defattr(-,root,root,-)
%{_datadir}/libdtk-%{apiver}

%changelog
