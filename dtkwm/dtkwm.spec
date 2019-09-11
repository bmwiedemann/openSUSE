#
# spec file for package dtkwm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 2

Name:           dtkwm
Version:        2.0.11
Release:        0
Summary:        Deepin graphical user interface library
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dtkwm
Source0:        https://github.com/linuxdeepin/dtkwm/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libQt5PlatformSupport-devel-static
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
DtkWm is used to handle double screen for deepin desktop development.
This package contains the shared libraries.

%package -n lib%{name}%{sover}
Summary:        Dtkwm libraries
Group:          System/Libraries

%description -n lib%{name}%{sover}
DtkWm is used to handle double screen for deepin desktop development.
This package contains the shared libraries.

%package devel
Summary:        Development package for %{name}
Group:          Development/Libraries/X11
Requires:       lib%{name}%{sover} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q

%build
%qmake5 PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
make %{?_smp_mflags}

%install
%qmake5_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig

%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%defattr(-,root,root,-)
%doc README.md 
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libdtk-*/
%dir %{_libdir}/cmake/DtkWm
%{_libdir}/cmake/DtkWm/DtkWmConfig.cmake
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%dir %{_libdir}/qt5
%dir %{_libdir}/qt5/mkspecs
%dir %{_libdir}/qt5/mkspecs/modules
%{_libdir}/qt5/mkspecs/modules/qt_lib_dtkwm.pri

%changelog
