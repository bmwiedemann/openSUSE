#
# spec file for package gnome-color-manager
#
# Copyright (c) 2025 SUSE LLC
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
Version:        3.36.2
Release:        0
Summary:        Color management tools for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-color-manager
Source:         %{name}-%{version}.tar.zst

BuildRequires:  docbook-utils-minimal
BuildRequires:  libtiff-devel
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(colord) >= 1.3.1
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.10
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91.0
BuildRequires:  pkgconfig(lcms2) >= 2.2
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

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/gcm-*
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-color-manager/
%doc %{_datadir}/help/C/gnome-color-manager/
%{_datadir}/icons/hicolor/*/apps/gnome-color-manager.*
%{_mandir}/man?/*%{ext_man}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.ColorProfileViewer.appdata.xml

%files lang -f %{name}.lang

%changelog
