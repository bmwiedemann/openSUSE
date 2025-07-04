#
# spec file for package xfce4-whiskermenu-plugin
#
# Copyright (c) 2025 SUSE LLC
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


%define panel_version 4.16
%define plugin whiskermenu
Name:           xfce4-whiskermenu-plugin
Version:        2.10.0
Release:        0
Summary:        Alternate Xfce Menu
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-whiskermenu-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/2.10/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(accountsservice) >= 0.6.45
BuildRequires:  pkgconfig(exo-2) >= 4.16
BuildRequires:  pkgconfig(garcon-1) >= 0.6.4
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.7
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.16
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.16
BuildRequires:  pkgconfig(libxfconf-0) >= 4.16
# BuildRequires:  xfce4-dev-tools
Recommends:     %{name}-lang
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
Whisker Menu is an alternate application launcher for Xfce. When
opened, it shows a list of applications marked as favorites.
Installed applications can be browsed by clicking on the category
buttons on the side. Whisker Menu keeps a list of most recent used
applications launched from it.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang xfce4-whiskermenu-plugin %{?no_lang_C}

%files
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/xfce4-popup-whiskermenu
%{_libdir}/xfce4/panel/plugins/libwhiskermenu.so
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.whiskermenu.*
%{_datadir}/xfce4/panel/plugins/whiskermenu.desktop
%{_mandir}/man?/xfce4-popup-whiskermenu.*

%files lang -f xfce4-whiskermenu-plugin.lang

%changelog
