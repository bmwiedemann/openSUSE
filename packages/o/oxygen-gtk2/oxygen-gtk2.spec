#
# spec file for package oxygen-gtk2
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


Name:           oxygen-gtk2
Version:        1.4.6
Release:        0
Summary:        A Port of the KDE Oxygen Widget Theme, to GTK 2.x
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
Source100:      baselibs.conf
# PATCH-FIX-OPENSUSE fix-menu-items-look.patch fisiu@opensuse.org -- Vertical center text in menuitems.
Patch0:         fix-menu-items-look.patch
# PATCH-FIX-OPENSUSE qt-config-path.patch sor.alexei@meowr.ru -- Search in Qt (oxygen-qt5) config path.
Patch1:         qt-config-path.patch
# PATCH-FIX-UPSTREAM fix-crash-about-invalid-columns.patch kde#338012 -- Fix crash in eclipse
Patch2:         fix-crash-about-invalid-columns.patch
# PATCH-FIX-UPSTREAM oxygen-gtk2-1.4.6-xul.patch -- Add a number of xul applications to prevent crash for these CCBUG: 341181
Patch3:         oxygen-gtk2-1.4.6-xul.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-2.0)

%description
Oxygen-Gtk2 is a port of the KDE Oxygen widget theme to Gtk 2.x.

It's primary goal is to ensure visual consistency between Gtk-based
and Qt-based applications. A secondary objective
is to also have a stand-alone nice looking gtk theme that would
behave well on other Desktop Environments.

%package -n gtk2-engine-oxygen
Summary:        Oxygen GTK 2.x Theme Engine
Group:          System/GUI/Other

%description -n gtk2-engine-oxygen
Oxygen-Gtk2 is a port of the KDE Oxygen widget theme to Gtk 2.x.

It's primary goal is to ensure visual consistency between Gtk-based
and Qt-based applications. A secondary objective
is to also have a stand-alone nice looking gtk theme that would
behave well on other Desktop Environments.

This package contains the Oxygen Gtk 2.x theme engine.

%package -n gtk2-theme-oxygen
Summary:        Oxygen GTK 2.x Theme
Group:          System/GUI/Other
Requires:       gtk2-engine-oxygen = %{version}
# oxygen-gtk2 was last used at version 1.2.0 in K:D:F
Provides:       oxygen-gtk2 = %{version}
Obsoletes:      oxygen-gtk2 < %{version}

%description -n gtk2-theme-oxygen
Oxygen-Gtk2 is a port of the KDE Oxygen widget theme to Gtk 2.x.

It's primary goal is to ensure visual consistency between Gtk-based
and Qt-based applications. A secondary objective
is to also have a stand-alone nice looking gtk theme that would
behave well on other Desktop Environments.

This package contains the Oxygen Gtk 2.x theme.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
# Switch to the oxygen-qt5 default.
sed -i 's/^\(TabStyle=\).*$/\1TS_PLAIN/' rc/oxygenrc

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n gtk2-engine-oxygen
%license COPYING
%doc AUTHORS README TODO
%{_libdir}/gtk-2.0/*/engines/liboxygen-gtk.so

%files -n gtk2-theme-oxygen
%license COPYING
%doc AUTHORS README TODO
%dir %{_datadir}/themes/oxygen-gtk/
%{_bindir}/oxygen-gtk-demo
%{_datadir}/themes/oxygen-gtk/gtk-2.0/

%changelog
