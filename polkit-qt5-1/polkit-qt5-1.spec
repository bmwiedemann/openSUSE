#
# spec file for package polkit-qt5-1
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           polkit-qt5-1
Version:        0.112.0
Release:        0
Summary:        PolicyKit Library Qt Bindings
License:        LGPL-2.1+
Group:          Development/Libraries/KDE
Url:            http://api.kde.org/kdesupport-api/kdesupport-apidocs/polkit-qt/html/
Source:         http://download.kde.org/stable/apps/KDE4.x/admin/polkit-qt-1-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM do-not-use-global-static-systembus-instance.patch
Patch0:         do-not-use-global-static-systembus-instance.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  polkit-devel
BuildRequires:  pkgconfig(Qt5Core) >= 5.1.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.1.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.1.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Polkit-qt-1 aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%package -n libpolkit-qt5-1-1
Summary:        PolicyKit Library Qt Bindings
Group:          Development/Libraries/KDE

%description -n libpolkit-qt5-1-1
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%package -n libpolkit-qt5-1-devel
Summary:        PolicyKit Library Qt Bindings
Group:          Development/Libraries/KDE
Requires:       libpolkit-qt5-1-1 = %{version}
Requires:       polkit-devel
Requires:       pkgconfig(Qt5Core) >= 5.1.0
Requires:       pkgconfig(Qt5Widgets) >= 5.1.0

%description -n libpolkit-qt5-1-devel
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%prep
%setup -q -n polkit-qt-1-%{version}
%patch0 -p1

%build
  %cmake_kf5 -d build -- -DUSE_QT5=ON -DUSE_QT4=OFF
  %make_jobs

%install
  %kf5_makeinstall -C build

%post -n libpolkit-qt5-1-1 -p /sbin/ldconfig

%postun -n libpolkit-qt5-1-1 -p /sbin/ldconfig

%files -n libpolkit-qt5-1-devel
%defattr(-,root,root)
%doc AUTHORS README COPYING*
%{_includedir}/polkit-qt5-1/
%{_kf5_libdir}/pkgconfig/polkit-qt5*
%{_kf5_libdir}/libpolkit-qt5-gui-1.so
%{_kf5_libdir}/libpolkit-qt5-core-1.so
%{_kf5_libdir}/libpolkit-qt5-agent-1.so
%{_kf5_libdir}/cmake/PolkitQt5-1/

%files -n libpolkit-qt5-1-1
%defattr(-,root,root)
%doc COPYING*
%{_kf5_libdir}/libpolkit-qt5-gui-1.so.*
%{_kf5_libdir}/libpolkit-qt5-core-1.so.*
%{_kf5_libdir}/libpolkit-qt5-agent-1.so.*

%changelog
