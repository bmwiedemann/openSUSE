#
# spec file for package frogr
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           frogr
Version:        1.5
Release:        0
Summary:        Tool to Manage Flickr Accounts
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
Url:            https://wiki.gnome.org/Apps/Frogr
Source:         http://download.gnome.org/sources/frogr/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  meson
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2
BuildRequires:  pkgconfig(libexif) >= 0.6.14
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.34
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.8
Recommends:     %{name}-lang

%description
Frogr is a application for the GNOME desktop that allows users to
manage their accounts in the Flickr image hosting website. It supports
all the basic Flickr features, including uploading pictures, adding
descriptions, setting tags and managing sets and groups pools.

%lang_package

%prep
%autosetup

%build
%meson \
	-D enable-header-bar=true \
	-D enable-video=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file org.gnome.frogr Viewer

%files
%doc NEWS README
%license COPYING
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.frogr.appdata.xml
%{_datadir}/applications/org.gnome.%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.gnome.frogr*.*
%{_mandir}/man1/frogr.1%{ext_man}

%files lang -f %{name}.lang

%changelog
