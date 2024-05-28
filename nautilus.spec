#
# spec file for package nautilus
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


Name:           nautilus
Version:        46.2
Release:        0
Summary:        File Manager for the GNOME Desktop
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/File utilities
URL:            https://wiki.gnome.org/Apps/Nautilus
Source0:        %{name}-%{version}.tar.zst
Source1:        set_trusted.desktop
Source2:        set_trusted.sh

# needed for directory ownership
BuildRequires:  dbus-1
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  (python3-dataclasses if python3-base < 3.7)
BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gexiv2) >= 0.14.0
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.79.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.79.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.79.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0) >= 2.79.0
BuildRequires:  pkgconfig(gnome-autoar-0) >= 0.3.0
BuildRequires:  pkgconfig(gnome-desktop-4) >= 1.0.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 42
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.13.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.0
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(pango) >= 1.44.4
BuildRequires:  pkgconfig(tracker-sparql-3.0)
# Needed for tests
BuildRequires:  python3-gobject
BuildRequires:  tracker
BuildRequires:  tracker-miner-files >= 2.99
#
Requires:       tracker-miner-files >= 2.99
Recommends:     gvfs

%description
Nautilus is the file manager for the GNOME desktop.

%package -n libnautilus-extension4
Summary:        File Manager for the GNOME Desktop -- Extension Library
Group:          System/Libraries
Conflicts:      nautilus-totem < 3.31.91

%description  -n libnautilus-extension4
Nautilus is the file manager for the GNOME desktop.

This package contains the library used by nautilus extensions.

%package -n typelib-1_0-Nautilus-4_0
Summary:        File Manager for the GNOME Desktop -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Nautilus-4_0
Nautilus is the file manager for the GNOME desktop.

This package provides the GObject Introspection bindings for the library
used by nautilus extensions.

%package -n gnome-shell-search-provider-nautilus
Summary:        File Manager for the GNOME Desktop -- Search Provider for GNOME Shell
Group:          Productivity/File utilities
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-nautilus
Nautilus is the file manager for the GNOME desktop.

This package contains a search provider to enable GNOME Shell to get
search results from Files (nautilus)

%package devel
Summary:        File Manager for the GNOME Desktop -- Development Files
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       libnautilus-extension4 = %{version}
Requires:       typelib-1_0-Nautilus-4_0 = %{version}

%description devel
Nautilus is the file manager for the GNOME desktop.

This package contains development files for nautilus.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D docs=true \
	-D tests=headless \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file org.gnome.Nautilus
%suse_update_desktop_file nautilus-autorun-software
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}
%if 0%{?sle_version}
install -m0644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/skel/.config/autostart/set_trusted.desktop
install -m0755 -D %{SOURCE2} %{buildroot}%{_bindir}/set_trusted.sh
%endif

%check
%meson_test

%ldconfig_scriptlets -n libnautilus-extension4

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/nautilus
%{_bindir}/nautilus-autorun-software
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.Tracker3.Miner.Extract.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.Tracker3.Miner.Files.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.service
%{_datadir}/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Nautilus*
%{_datadir}/metainfo/org.gnome.Nautilus.metainfo.xml
%{_datadir}/%{name}/
%{_datadir}/tracker3/domain-ontologies/org.gnome.Nautilus.domain.rule
%{_mandir}/man1/nautilus*.1%{?ext_man}
%if 0%{?sle_version}
%{_sysconfdir}/skel/.config/autostart
%{_sysconfdir}/skel/.config/autostart/set_trusted.desktop
%{_bindir}/set_trusted.sh
%endif

%files -n libnautilus-extension4
%{_libdir}/libnautilus-extension.so.4*
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-4
%{_libdir}/nautilus/extensions-4/*.so

%files -n typelib-1_0-Nautilus-4_0
%{_libdir}/girepository-1.0/Nautilus-4.0.typelib

%files -n gnome-shell-search-provider-nautilus
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Nautilus.search-provider.ini

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/doc/%{name}/

%files lang -f %{name}.lang

%changelog
