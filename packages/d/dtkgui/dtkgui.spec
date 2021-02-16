#
# spec file for package dtkgui
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2020 Hillwood Yang <hillwood@opensuse.org>
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


%define libver  5
%define apiver  5.0.0

Name:           dtkgui
Version:        5.4.0
Release:        0
Summary:        Deepin Toolkit gui
License:        LGPL-3.0
Group:          System/GUI/Other
Url:            https://github.com/linuxdeepin/dtkgui
Source0:        https://github.com/linuxdeepin/dtkgui/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  libQt5Gui-private-headers-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Toolkit, gui module for DDE look and feel

%package -n lib%{name}%{libver}
Summary:        Deepin Toolkit gui libraries
Group:          System/Libraries

%description -n lib%{name}%{libver}
Deepint Tool Kit (Dtk) gui is the base devlopment tool of all C++/Qt Developer work 
on Deepin.

%package devel
Summary:        Development tools for dtkgui
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{libver} = %{version}

%description devel
The dtkgui-devel package contains the header files and developer
docs for dtkgui.

You shoud firstly read the "Deepin Application Specification".

%prep
%setup -q

%build
qmake-qt5 DEFINES+=QT_NO_DEBUG_OUTPUT \
          PREFIX=%{_prefix} \
          LIB_INSTALL_DIR=%{_libdir}

%install
%qmake5_install

# Workaround boo#1181642
rm -rf %{buildroot}%{_sysconfdir}/dbus-1/system.d/com.deepin.dtk.FileDrag.conf

%post -n lib%{name}%{libver} -p /sbin/ldconfig
%postun -n lib%{name}%{libver} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{_libdir}/libdtk-%{apiver}
%dir %{_libdir}/libdtk-%{apiver}/DGui
%dir %{_libdir}/libdtk-%{apiver}/DGui/bin
%{_libdir}/libdtk-%{apiver}/DGui/bin/deepin-gui-settings
%{_libdir}/libdtk-%{apiver}/DGui/bin/taskbar
# %config %{_sysconfdir}/dbus-1/system.d/com.deepin.dtk.FileDrag.conf

%files -n lib%{name}%{libver}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_includedir}/libdtk-%{apiver}/DGui
%{_libdir}/cmake/DtkGui
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/qt5/mkspecs/modules/qt_lib_%{name}.pri

%changelog

