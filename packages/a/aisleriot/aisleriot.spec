#
# spec file for package aisleriot
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


Name:           aisleriot
Version:        3.22.27
Release:        0
Summary:        Solitaire Card Games for GNOME
License:        GPL-3.0-or-later
URL:            https://wiki.gnome.org/Apps/Aisleriot
Source0:        https://gitlab.gnome.org/GNOME/aisleriot/-/archive/%{version}/aisleriot-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# Needed to get lsb data
BuildRequires:  lsb-release
BuildRequires:  meson >= 0.49
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires:  pkgconfig(guile-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       guile

%description
Aisleriot is a compilation of 80 different solitaire card games.

%package themes
Summary:        Extra themes for the Aisleriot solitaire card game program
Requires:       %{name} = %{version}
Enhances:       %{name}
BuildArch:      noarch

%description themes
Aisleriot is a compilation of 80 different solitaire card games.

This package provides extra themes for Aisleriot.

%lang_package

%prep
%autosetup -p1

%build
%meson \
    -Dtheme_kde=false
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}%{_datadir}/help
%suse_update_desktop_file -N "AisleRiot" -G "Solitaire" sol
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING.GFDL
%doc AUTHORS README.md
%doc %{_datadir}/help/C/aisleriot/
%{_bindir}/sol
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/sol.metainfo.xml
%{_datadir}/applications/sol.desktop
%{_datadir}/aisleriot/
%dir %{_libdir}/aisleriot
%dir %{_libdir}/aisleriot/guile
%dir %{_libdir}/aisleriot/guile/*
%dir %{_libdir}/aisleriot/guile/*/aisleriot
%{_libdir}/aisleriot/guile/*/aisleriot/api.go
%{_libdir}/aisleriot/guile/*/*.go
%if "%{_libdir}" != "%{_libexecdir}"
%dir %{_libexecdir}/aisleriot
%endif
%{_libexecdir}/aisleriot/ar-cards-renderer
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_datadir}/icons/hicolor/*/apps/gnome-aisleriot*
%{_datadir}/icons/hicolor/*/apps/gnome-freecell.*
%{_mandir}/man?/sol*%{ext_man}
# Kind of ugly to own the valgrind directory, but the other solutions (a dep on
# valgrind, a subpackage, etc.) are not worth it
%dir %{_libdir}/valgrind
%{_libdir}/valgrind/aisleriot.supp
# Exclude files that are in themes
%exclude %{_datadir}/aisleriot/cards/anglo.svgz
%exclude %{_datadir}/aisleriot/cards/anglo_bitmap.svgz
%exclude %{_datadir}/aisleriot/cards/bellot.svgz
%exclude %{_datadir}/aisleriot/cards/bonded.svgz
%exclude %{_datadir}/aisleriot/cards/dondorf.svgz
%exclude %{_datadir}/aisleriot/cards/gnomangelo_bitmap.svgz
%exclude %{_datadir}/aisleriot/cards/ornamental.svgz

%files themes
%{_datadir}/aisleriot/cards/anglo.svgz
%{_datadir}/aisleriot/cards/anglo_bitmap.svgz
%{_datadir}/aisleriot/cards/bellot.svgz
%{_datadir}/aisleriot/cards/bonded.svgz
%{_datadir}/aisleriot/cards/dondorf.svgz
%{_datadir}/aisleriot/cards/gnomangelo_bitmap.svgz
%{_datadir}/aisleriot/cards/ornamental.svgz

%files lang -f aisleriot.lang

%changelog
