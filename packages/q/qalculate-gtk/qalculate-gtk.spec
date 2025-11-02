#
# spec file for package qalculate-gtk
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        5.8.1
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
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.4
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(libqalculate) >= 5.6.0
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       qalculate-data >= %{version}

%description
Qalculate is a multi-purpose cross-platform desktop calculator. It is
simple to use but provides power and versatility normally reserved for
complicated math packages, as well as useful tools for everyday needs
(such as currency conversion and percent calculation). Features include a
large library of customizable functions, unit calculations and conversion,
symbolic calculations (including integrals and equations), arbitrary
precision, uncertainty propagation, interval arithmetic, plotting, and a
user-friendly interface (GTK+ and CLI).

%package -n gnome-shell-search-provider-qalculate-gtk
Summary:        Search provider for GNOME shell overview for qalculate-gtk
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-qalculate-gtk
Qalculate is a multi-purpose cross-platform desktop calculator. This package
provides a search provider for qalculate on the gnome-shell overview.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --enable-gnome-search
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%doc %{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}.?%{ext_man}
%{_datadir}/icons/hicolor/*/apps/qalculate.*

%files -n gnome-shell-search-provider-qalculate-gtk
%license COPYING
%{_libexecdir}/qalculate-search-provider
%{_datadir}/dbus-1/services/io.github.Qalculate.SearchProvider.service
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/io.github.Qalculate.search-provider.ini

%files lang -f %{name}.lang

%changelog
