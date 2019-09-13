#
# spec file for package goobox
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


Name:           goobox
Version:        3.6.0
Release:        0
# FIXME: Enable libcoverart support.
Summary:        CD Player and Ripper for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Grabbers
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/goobox/3.6/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libbrasero-media3)
#BuildRequires:  pkgconfig(libcoverart) >= 1.0.0
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(libmusicbrainz5) >= 5.0.0
BuildRequires:  pkgconfig(libnotify) >= 0.4.3
BuildRequires:  pkgconfig(sm)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
Goobox is a CD player and ripper that always knows just what to do.

%lang_package

%prep
%autosetup -p1
translation-update-upstream po goobox

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file org.gnome.Goobox AudioVideo Player CD
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%post
%glib2_gsettings_schema_post
%desktop_database_post
%icon_theme_cache_post

%postun
%glib2_gsettings_schema_postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/goobox
%{_datadir}/applications/org.gnome.Goobox.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Goobox.gschema.xml
%{_datadir}/icons/hicolor/*/apps/goobox.png
%{_datadir}/icons/hicolor/scalable/apps/goobox-symbolic.svg
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Goobox.appdata.xml

%files lang -f %{name}.lang

%changelog
