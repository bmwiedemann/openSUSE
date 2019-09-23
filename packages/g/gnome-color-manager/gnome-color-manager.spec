#
# spec file for package gnome-color-manager
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Luis Medinas, Portugal
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


Name:           gnome-color-manager
Version:        3.32.0
Release:        0
Summary:        Color management tools for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-color-manager
Source:         https://download.gnome.org/sources/gnome-color-manager/3.32/%{name}-%{version}.tar.xz

BuildRequires:  docbook-utils
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(colord) >= 1.3.1
BuildRequires:  pkgconfig(colord-gtk) >= 0.1.20
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.10
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91.0
BuildRequires:  pkgconfig(lcms2) >= 2.2
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(vte-2.91)
Requires:       argyllcms
Requires:       colord
Requires:       colord-color-profiles
# We only recommend PackageKit - knowing that some features are not available if not present
# For managed setups, this does not matter, as the user is not supposed to be bothered with
# such things anyway (see bnc#895997).
Recommends:     PackageKit
Obsoletes:      gnome-color-manager-devel < %{version}
Obsoletes:      libcolor-glib1 < %{version}

%description
GNOME Color Manager is a session framework that makes it easy to manage,
install and generate color profiles in the GNOME desktop.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file gcm-calibrate
%suse_update_desktop_file gcm-import
%suse_update_desktop_file gcm-picker
%suse_update_desktop_file org.gnome.ColorProfileViewer HardwareSettings
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS MAINTAINERS README
%{_bindir}/gcm-*
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-color-manager/
%doc %{_datadir}/help/C/gnome-color-manager/
%{_datadir}/icons/hicolor/*/apps/gnome-color-manager.*
%{_mandir}/man?/*%{ext_man}
%{_libexecdir}/gcm-helper-exiv
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.ColorProfileViewer.appdata.xml

%files lang -f %{name}.lang

%changelog
