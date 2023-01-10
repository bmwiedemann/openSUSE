#
# spec file for package eog
#
# Copyright (c) 2023 SUSE LLC
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


Name:           eog
Version:        43.2
Release:        0
Summary:        Image Viewer for GNOME
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://wiki.gnome.org/Apps/EyeOfGnome
Source0:        https://download.gnome.org/sources/eog/43/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  libjpeg-devel
BuildRequires:  meson >= 0.44.0
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(exempi-2.0) >= 1.99.5
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.36.5
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.53.4
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.53.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.53.4
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 2.91.2
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 2.91.92
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.15
BuildRequires:  pkgconfig(gtk+-unix-print-3.0) >= 3.5.4
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0) >= 0.7.4
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 0.7.4
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.44.0
BuildRequires:  pkgconfig(shared-mime-info) >= 0.20

%description
Eye of GNOME (eog) is a simple graphics viewer for the GNOME desktop
which uses the gdk-pixbuf library. It can deal with large images, and
zoom and scroll with constant memory usage.

%package devel
Summary:        Development files for eog, an image viewer
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
Eye of GNOME (eog) is a simple graphics viewer for the GNOME desktop
which uses the gdk-pixbuf library.

This subpackage contains all the necessary files and documentation for
developing eog plugins.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D libexif=true \
	-D cms=true \
	-D xmp=true \
	-D libjpeg=true \
	-D librsvg=true \
	-D gtk_doc=true \
	-D introspection=true \
	-D installed_tests=false \
	-D libportal=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/org.gnome.eog.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.%{name}*.svg
%{_datadir}/%{name}/
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
# %%{_datadir}/eog/gir-1.0/ goes to the -devel package.
%exclude %{_datadir}/%{name}/gir-1.0/

%files devel
%doc AUTHORS ChangeLog HACKING MAINTAINERS TODO
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/%{name}-3.0/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/gir-1.0/

%files lang -f %{name}.lang

%changelog
