#
# spec file for package qalculate-gtk
#
# Copyright (c) 2022 SUSE LLC
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


Name:           qalculate-gtk
Version:        4.5.0
Release:        0
Summary:        Multi-purpose cross-platform desktop calculator
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://qalculate.github.io
Source0:        https://github.com/Qalculate/qalculate-gtk/releases/download/v%{version}/qalculate-gtk-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  intltool
BuildRequires:  libnghttp2-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.4
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(libqalculate) >= %{version}
BuildRequires:  pkgconfig(libxml-2.0)

%description
Qalculate! is a multi-purpose cross-platform desktop calculator. It is
simple to use but provides power and versatility normally reserved for
complicated math packages, as well as useful tools for everyday needs
(such as currency conversion and percent calculation). Features include a
large library of customizable functions, unit calculations and conversion,
symbolic calculations (including integrals and equations), arbitrary
precision, uncertainty propagation, interval arithmetic, plotting, and a
user-friendly interface (GTK+ and CLI).

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install
%find_lang %{name}

%files
%doc AUTHORS ChangeLog README TODO
%doc %{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%license COPYING
%{_mandir}/man?/%{name}.?%{ext_man}
%{_libexecdir}/qalculate-search-provider
%{_datadir}/dbus-1/services/io.github.Qalculate.SearchProvider.service
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/io.github.Qalculate.search-provider.ini
%{_datadir}/icons/hicolor/128x128/apps/qalculate.png
%{_datadir}/icons/hicolor/16x16/apps/qalculate.png
%{_datadir}/icons/hicolor/22x22/apps/qalculate.png
%{_datadir}/icons/hicolor/24x24/apps/qalculate.png
%{_datadir}/icons/hicolor/256x256/apps/qalculate.png
%{_datadir}/icons/hicolor/32x32/apps/qalculate.png
%{_datadir}/icons/hicolor/48x48/apps/qalculate.png
%{_datadir}/icons/hicolor/64x64/apps/qalculate.png
%{_datadir}/icons/hicolor/scalable/apps/qalculate.svg

%files lang -f %{name}.lang

%changelog
