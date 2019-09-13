#
# spec file for package nmapsi4
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007-2014 Packman Team <packman@links2linux.de>
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

%define basever 0.5
%define fullver 0.5-alpha1
Name:           nmapsi4
Version:        0.5_alpha1
Release:        0
Summary:        A Graphical Front-End for Nmap
# images are lgpl-3.0, couldn't find any "or later" clause
License:        GPL-2.0+ AND LGPL-3.0
Group:          Productivity/Networking/Diagnostic
URL:            http://www.nmapsi4.org
Source0:        https://sourceforge.net/projects/nmapsi/files/%{name}-%{basever}/%{name}-%{fullver}.tar.xz
BuildRequires:  cmake
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc7-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       bind-utils
Requires:       nmap >= 6.00
Requires:       nping >= 6.00
Requires:       xdg-utils

%description
NmapSI4 is a Qt5-based GUI for nmap, showing scan results in a
split-pane view separating hosts, ports/services and scan status.
It offers a history and bookmarks for recalling prior scan commands,
and includes DNS lookup and traceroute facilities.

%prep
%setup -q -n %{name}-%{fullver}

sed -i 's|kdesu\ nmapsi4|%{_bindir}/xdg-su\ -c\ %{_bindir}/%{name}|;/^X-*/d' \
src/desktop/%{name}-admin.desktop
sed -i 's|Qt4|Qt5|g' src/desktop/%{name}.desktop src/desktop/%{name}-admin.desktop
sed -i 's|kde4/||' src/CMakeLists.txt

%build
test -x "$(type -p g++-7)" && export CXX=g++-7
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%suse_update_desktop_file %{name} Network Monitor
%suse_update_desktop_file %{name}-admin Network Monitor

%files
%doc COPYING images/lgpl-3.0.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale/
%{_datadir}/%{name}/locale/%{name}_*.qm
%{_datadir}/applications/%{name}-admin.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/dbus-1/interfaces/org.%{name}.Nmapsi4.xml

%changelog
