#
# spec file for package adwaita-icon-theme
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


Name:           adwaita-icon-theme
Version:        44.0
Release:        0
Summary:        GNOME Icon Theme
License:        CC-BY-SA-3.0 OR LGPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme
Source0:        https://download.gnome.org/sources/adwaita-icon-theme/44/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  gtk3-tools >= 3.24.2
BuildRequires:  pkgconfig
# To make sure the icon theme cache gets generated
Requires(post): (gtk3-tools if libgtk-3-0)
Requires(post): (gtk4-tools if libgtk-4-1)
Provides:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description
The default GNOME icon theme, Adwaita.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
# Those folders disappeared in the upgrade from 2.28.0 -> 2.29.0
# FIXME: eventually no application should install any files there
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/actions
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/apps
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/categories
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/devices
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/emblems
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/emotes
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/mimetypes
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/places
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/status
mkdir -p %{buildroot}%{_datadir}/icons/Adwaita/scalable/stock/generic
# Add internet-web-browser symlink (to web-browser) to adwaita-icon-theme (bnc#767437)
for folder in %{buildroot}%{_datadir}/icons/Adwaita/*x[0-9]*; do
 ln ${folder}/apps/web-browser.png ${folder}/apps/internet-web-browser.png || :
done
%{icon_theme_cache_create_ghost Adwaita}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING COPYING_LGPL COPYING_CCBYSA3
%doc AUTHORS NEWS
%ghost %{_datadir}/icons/Adwaita/icon-theme.cache
%{_datadir}/icons/Adwaita/
%{_datadir}/pkgconfig/adwaita-icon-theme.pc

%changelog
