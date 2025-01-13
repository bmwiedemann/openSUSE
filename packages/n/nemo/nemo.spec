#
# spec file for package nemo
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


%define         sover   1
Name:           nemo
Version:        6.4.3
Release:        0
Summary:        File browser for Cinnamon
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/nemo
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.10.0
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xapp) >= 1.9.0
Requires:       desktop-file-utils >= 0.7
Requires:       glib2-tools
Requires:       gvfs >= 1.3.2
Requires:       python3
Requires:       shared-mime-info >= 0.50
Recommends:     gdk-pixbuf-loader-rsvg
Recommends:     gvfs-backends
Recommends:     python3dist(xlrd)
Suggests:       xdg-user-dirs
Suggests:       xplayer
Suggests:       xreader
Suggests:       xviewer

%description
Nemo is the file manager for the Cinnamon desktop environment.

%package devel
Summary:        Development files for Nemo
Requires:       %{name} = %{version}
Requires:       lib%{name}-extension%{sover} = %{version}
Requires:       typelib-1_0-Nemo-3_0 = %{version}

%description devel
Nemo is the file manager for the Cinnamon desktop environment.

This package provides the development files for Nemo.

%package -n lib%{name}-extension%{sover}
Summary:        Nemo extension shared libraries
Group:          System/Libraries

%description -n lib%{name}-extension%{sover}
Nemo is the file manager for the Cinnamon desktop environment.

This package provides Nemo's shared libraries.

%package -n  typelib-1_0-Nemo-3_0
Summary:        File Browser for Cinnamon -- Introspection Bindings
Group:          System/Libraries

%description -n typelib-1_0-Nemo-3_0
Nemo is the file manager for the Cinnamon desktop environment.

This package provides the GObject Introspection bindings for Nemo.

%prep
%autosetup

sed -i 's|/usr/bin/env bash|/usr/bin/bash|g' search-helpers/%{name}-epub2text

%build
%meson \
  -Ddeprecated_warnings=true \
  -Dexif=true \
  -Dxmp=true \
  -Dgtk_doc=true \
  -Dselinux=true \
  -Dempty_view=false \
  -Dtracker=true \
  --libexecdir=%{_libexecdir}/%{name}
%meson_build

%install
%meson_install

# We need to own this directory.
mkdir -p %{buildroot}%{_libdir}/nemo/extensions-3.0/

%fdupes %{buildroot}%{_datadir}

%post -n lib%{name}-extension%{sover}
%ldconfig

%postun -n lib%{name}-extension%{sover}
%ldconfig

%files
%license COPYING*
%doc AUTHORS README.md debian/changelog
%{_bindir}/%{name}*
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man?/%{name}*%{?ext_man}
%{_datadir}/dbus-1/services/nemo.service
%{_datadir}/dbus-1/services/nemo.FileManager1.service
%{_datadir}/glib-2.0/schemas/org.nemo.gschema.xml
%{_datadir}/gtksourceview-{2.0,3.0,4}/*
%{_datadir}/polkit-1/actions/org.nemo.root.policy

%files -n typelib-1_0-Nemo-3_0
%{_libdir}/girepository-1.0/Nemo-3.0.typelib

%files -n lib%{name}-extension%{sover}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/extensions-3.0
%{_libdir}/lib%{name}-extension.so.%{sover}*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}-extension.so
%{_libdir}/pkgconfig/lib%{name}-extension.pc
%{_datadir}/gir-1.0/Nemo-3.0.gir
%{_datadir}/gtk-doc/html/libnemo-extension

%changelog
