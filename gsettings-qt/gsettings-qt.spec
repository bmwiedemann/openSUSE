#
# spec file for package gsettings-qt
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Hillwood Yang <hillwood@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libver 1
Name:           gsettings-qt
Version:        0.1.20160329
Release:        0
Summary:        QT bindings for GSettings
License:        GPL-3.0+
Group:          Development/Libraries/X11
Url:            https://launchpad.net/gsettings-qt
Source0:        %{name}-%{version}.tar.bz2
Patch0:         dependencies.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt/QML bindings for GSettings.

%package -n libgsettings-qt1
Summary:        Libraries for gsettings-qt
Group:          System/Libraries

%description -n libgsettings-qt1
Qt/QML bindings for GSettings.

This package is Libraries for gsettings-qt.

%package devel
Summary:        Libraries for gsettings-qt
Group:          Development/Libraries/X11
Requires:       libgsettings-qt1

%description devel
Qt/QML bindings for GSettings.

This package contains the header files and developer
docs for gsettings-qt.

%prep
%setup -q
%patch0 -p1

%build

%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
make %{?_smp_mflags}

%install
%qmake5_install

# Remove useless files
rm -rf %{buildroot}/usr/tests

%post -n libgsettings-qt1 -p /sbin/ldconfig

%postun -n libgsettings-qt1 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%dir %{_libdir}/qt5/qml/GSettings.1.0
%{_libdir}/qt5/qml/GSettings.1.0/libGSettingsQmlPlugin.so
%{_libdir}/qt5/qml/GSettings.1.0/plugins.qmltypes
%{_libdir}/qt5/qml/GSettings.1.0/qmldir

%files -n libgsettings-qt1
%defattr(-,root,root,-)
%{_libdir}/libgsettings-qt.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/gsettings-qt.pc
%dir %{_includedir}/qt5/QGSettings
%{_includedir}/qt5/QGSettings/QGSettings
%{_includedir}/qt5/QGSettings/qgsettings.h
%{_libdir}/libgsettings-qt.so

%changelog
