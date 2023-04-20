#
# spec file for package xdg-desktop-portal-lxqt
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


Name:           xdg-desktop-portal-lxqt
Version:        0.4.0
Release:        0
Summary:        A backend implementation for xdg-desktop-portal
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# like libfm-qt this one needs private headers
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem) >= 5.78
BuildRequires:  pkgconfig(Qt5Core) >= 5.15
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libfm-qt) >= 1.3.0
BuildRequires:  pkgconfig(xdg-desktop-portal)

%description
A backend implementation for xdg-desktop-portal that is using Qt/KF5/libfm-qt.
functionality needed by nearly all of its components.

%prep
%setup -q

%build
%cmake

%install
%cmake_install

%files
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_libexecdir}/xdg-desktop-portal-lxqt
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.lxqt.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%{_datadir}/xdg-desktop-portal/portals/lxqt.portal

%changelog
