#
# spec file for package gnome-photos
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


Name:           gnome-photos
Version:        43.0
Release:        0
Summary:        Photo viewer for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://wiki.gnome.org/Design/Apps/Photos
Source0:        https://download.gnome.org/sources/gnome-photos/43/%{name}-%{version}.tar.xz
# PATCH-NEEDS-REBASE gnome-photos-on-demand-activate-dleyna.patch bsc#992420, glgo#GNOME/gnome-photos#75 sckang@suse.com -- Activate dleyna-renderer-service on demand instead of on start-up. WAS PATCH-FIX-UPSTREAM
Patch0:         gnome-photos-on-demand-activate-dleyna.patch
# PATCH-FIX-UPSTREAM 64c6f733a44bac5b7f08445a686c000681f93f5f.patch -- Use babl-0.1
Patch1:         https://gitlab.gnome.org/GNOME/gnome-photos/-/commit/64c6f733a44bac5b7f08445a686c000681f93f5f.patch
# PATCH-FIX-UPSTREAM 9db32c3508a8c5d357a053d5f8278c34b4df18f3.patch -- build: accept both babl and babl-0.1
Patch2:         https://gitlab.gnome.org/GNOME/gnome-photos/-/commit/9db32c3508a8c5d357a053d5f8278c34b4df18f3.patch


BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
# Technically seen, glib2-tools would require this, but it introduces a loop there. So explictly require here
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  itstool
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  (pkgconfig(babl) or pkgconfig(babl-0.1))
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(exempi-2.0) >= 1.99.5
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.32
BuildRequires:  pkgconfig(gegl-0.4) >= 0.4.0
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(goa-1.0) >= 3.8.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.16
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdazzle-1.0) >= 3.26.0
BuildRequires:  pkgconfig(libexif) >= 0.6.14
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.26.0
BuildRequires:  pkgconfig(tracker-sparql-3.0)
# gnome-photos references tracker's glib schemas
Requires:       tracker >= 3
# and also org.freedesktop.Tracker.Miner3.Files, which lives in tracker-miner-files
Requires:       tracker-miner-files >= 3
# If we want to be able to send photos to a remote DLNA renderer, we require the dbus service for it
Recommends:     dbus(dleyna-renderer-service)

%description
Photos, like Documents, Music and Videos, is one of the core GNOME
applications meant for find and reminding the user about her content.
The internal architecture Photos is based on Documents -- the document
manager application for GNOME, because they share similar UI/UX
patterns and objectives.

%package -n gnome-shell-search-provider-gnome-photos
Summary:        GNOME Photos -- Search Provider for GNOME Shell
Group:          Productivity/Graphics/Viewers
Requires:       %{name} = %{version}
Supplements:    (gnome-shell and %{name})

%description -n gnome-shell-search-provider-gnome-photos
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Photos.

%lang_package

%prep
%autosetup -N
%patch1 -p1
%patch2 -p1

%build
%meson
%meson_build

%install
%meson_install

rm %{buildroot}%{_datadir}/doc/%{name}/{ARTISTS,AUTHORS,NEWS,README}
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc ARTISTS AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Photos.desktop
%{_datadir}/dbus-1/services/org.gnome.Photos.service
%{_datadir}/glib-2.0/schemas/org.gnome.photos.gschema.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Photos*
%{_datadir}/metainfo/org.gnome.Photos.appdata.xml
%{_libexecdir}/gnome-photos-thumbnailer
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libgnome-photos.so

%files -n gnome-shell-search-provider-gnome-photos
# Own dirs so we don't have to depend on gnome-shell.
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Photos.search-provider.ini

%files lang -f %{name}.lang

%changelog
