#
# spec file for package kdocker
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


Name:           kdocker
Version:        6.2
Release:        0
Summary:        KDocker will help you dock any application into the system tray
License:        GPL-2.0-or-later
URL:            https://github.com/user-none/KDocker
Source0:        https://github.com/user-none/KDocker/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.18
BuildRequires:  hicolor-icon-theme
BuildRequires:  podman
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(x11-xcb)

%description
KDocker will help you dock any application in the system tray. This means you
can dock openoffice, firefox, thunderbolt, eclipse, anything!
Just point and click. Works for both Plasma and GNOME (In fact it should work
for most modern window managers that support NET WM Specification.

All you need to do is start KDocker and select an application using the mouse
and the application gets docked into the system tray.
The application can also be made to dissappear from the task bar.

%prep
%autosetup -p1 -n KDocker-%{version}

%build
%cmake_qt6 -DCMAKE_SKIP_RPATH:BOOL=TRUE

%qt6_build

%install
%qt6_install

%files
%doc AUTHORS ChangeLog README.md
%license LICENSE
%{_bindir}/kdocker
%{_datadir}/applications/com.kdocker.KDocker.desktop
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/kdocker
%{_datadir}/dbus-1/interfaces/com.kdocker.KDocker.xml
%{_datadir}/dbus-1/services/com.kdocker.KDocker.service
%{_datadir}/icons/hicolor/*/apps/com.kdocker.KDocker.*
%{_datadir}/metainfo/com.kdocker.KDocker.metainfo.xml
%{_mandir}/man1/kdocker.1.gz

%changelog
