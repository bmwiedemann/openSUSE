#
# spec file for package nautilus
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


Name:           nautilus
Version:        3.34.1
Release:        0
Summary:        File Manager for the GNOME Desktop
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/File utilities
URL:            https://wiki.gnome.org/Apps/Nautilus

Source0:        https://download.gnome.org/sources/nautilus/3.34/%{name}-%{version}.tar.xz
# fate#308344 bgo#602147
Source1:        mount-archive.desktop
Source2:        set_trusted.desktop
Source3:        set_trusted.sh
Source99:       baselibs.conf

# needed for directory ownership
BuildRequires:  dbus-1
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gexiv2) >= 0.10.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.55.1
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.55.1
BuildRequires:  pkgconfig(glib-2.0) >= 2.55.1
BuildRequires:  pkgconfig(gmodule-no-export-2.0) >= 2.55.1
BuildRequires:  pkgconfig(gnome-autoar-0) >= 0.2.1
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.0.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.8.0
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.6
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(pango) >= 1.28.3
BuildRequires:  pkgconfig(tracker-sparql-2.0)
BuildRequires:  pkgconfig(x11)
Requires:       tracker-miner-files
Recommends:     %{name}-lang
Recommends:     gvfs

%description
Nautilus is the file manager for the GNOME desktop.

%package -n libnautilus-extension1
Summary:        File Manager for the GNOME Desktop -- Extension Library
Group:          System/Libraries

%description  -n libnautilus-extension1
Nautilus is the file manager for the GNOME desktop.

This package contains the library used by nautilus extensions.

%package -n typelib-1_0-Nautilus-3_0
Summary:        File Manager for the GNOME Desktop -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Nautilus-3_0
Nautilus is the file manager for the GNOME desktop.

This package provides the GObject Introspection bindings for the library
used by nautilus extensions.

%package -n gnome-shell-search-provider-nautilus
Summary:        File Manager for the GNOME Desktop -- Search Provider for GNOME Shell
Group:          Productivity/File utilities
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    packageand(%{name}:gnome-shell)

%description -n gnome-shell-search-provider-nautilus
Nautilus is the file manager for the GNOME desktop.

This package contains a search provider to enable GNOME Shell to get
search results from Files (nautilus)

%package devel
Summary:        File Manager for the GNOME Desktop -- Development Files
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       typelib-1_0-Nautilus-3_0 = %{version}

%description devel
Nautilus is the file manager for the GNOME desktop.

This package contains development files for nautilus.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson \
	-D docs=true
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file org.gnome.Nautilus
%suse_update_desktop_file nautilus-autorun-software
# Install the archive mime handler
test ! -e %{buildroot}%{_datadir}/applications/mount-archive.desktop
install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/mount-archive.desktop
%suse_update_desktop_file mount-archive
mkdir -p %{buildroot}/%{_libdir}/nautilus/extensions-3.0
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}
%if !0%{?is_opensuse}
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config/autostart
install -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/skel/.config/autostart/set_trusted.desktop
mkdir -p %{buildroot}%{_bindir}
install -m0755 %{SOURCE3} %{buildroot}%{_bindir}/set_trusted.sh
%endif

%post -n libnautilus-extension1 -p /sbin/ldconfig
%postun -n libnautilus-extension1 -p /sbin/ldconfig

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/nautilus
%{_bindir}/nautilus-autorun-software
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.service
%{_datadir}/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Nautilus*
%{_datadir}/metainfo/org.gnome.Nautilus.appdata.xml
%{_mandir}/man1/nautilus*.1%{ext_man}
%if !0%{?is_opensuse}
%{_sysconfdir}/skel/.config/autostart
%{_sysconfdir}/skel/.config/autostart/set_trusted.desktop
%{_bindir}/set_trusted.sh
%endif

%files -n libnautilus-extension1
%{_libdir}/libnautilus-extension.so.1*
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-3.0
%{_libdir}/nautilus/extensions-3.0/*.so

%files -n typelib-1_0-Nautilus-3_0
%{_libdir}/girepository-1.0/Nautilus-3.0.typelib

%files -n gnome-shell-search-provider-nautilus
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Nautilus.search-provider.ini

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/*

%files lang -f %{name}.lang

%changelog
