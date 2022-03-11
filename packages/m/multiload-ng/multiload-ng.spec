#
# spec file for package multiload-ng
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           multiload-ng
Version:        git20210103.743885d
Release:        0
Summary:        Modern graphical system monitor for any panel
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            https://github.com/udda/multiload-ng
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libxfce4panel-2.0)
BuildRequires:  pkgconfig(libxfce4ui-2)

%description
This spec will build a 'base' multiload-ng package and an 'xfce4' multiload-ng package.

%package base
Summary: Base multiload-ng package
%description base
Multiload-ng is a modern graphical system monitor. It's a near-complete rewrite of the good old GNOME multiload applet, that aims to support every existing panel.

It supports the following panels:
[] XFCE (xfce4-panel)
[x] LXDE (lxpanel)
[x] MATE (mate-panel)
[x] Ubuntu Unity (through libappindicator)
[] Every panel with support for Application Indicators
[] System tray (virtually any panel with a systray, in particular those without external plugins support, like tint2)
[] Standalone (has its own window, not embedded in any panel)
[x] Avant Window Navigator (EXPERIMENTAL)

Multiload-ng can be built with GTK2 and GTK3, so can be embedded within GTK2/GTK3 builds of all the panels above.

%prep base
%setup -q

%build base
./autogen.sh
%configure --disable-autostart --with-systray --with-xfce4
%make_build

%install base
%make_install

%find_lang multiload-ng %{?no_lang_C}

%files base -f multiload-ng.lang
%doc AUTHORS COPYING README.md
%{_bindir}/multiload-ng
%{_bindir}/multiload-ng-systray
%{_datadir}/applications/multiload-ng-standalone.desktop
%{_datadir}/applications/multiload-ng-systray.desktop
%{_datadir}/locale/de/LC_MESSAGES/multiload-ng.mo
%{_datadir}/locale/es/LC_MESSAGES/multiload-ng.mo
%{_datadir}/locale/fr/LC_MESSAGES/multiload-ng.mo
%{_datadir}/locale/it/LC_MESSAGES/multiload-ng.mo
%{_datadir}/locale/lt/LC_MESSAGES/multiload-ng.mo
%{_datadir}/locale/ru/LC_MESSAGES/multiload-ng.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/multiload-ng.mo

# -----

%package xfce4
Summary:        XFCE4 multiload-ng package
Requires:       multiload-ng-base
%description xfce4
Provides required files for XFCE4 panel integration.
%files xfce4
%{_libdir}/xfce4/panel/plugins/libmultiload-ng.la
%{_libdir}/xfce4/panel/plugins/libmultiload-ng.so
%{_datadir}/xfce4/panel/plugins/multiload-ng-xfce4.desktop

%changelog

