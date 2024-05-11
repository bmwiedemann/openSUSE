#
# spec file for package ProtonPlus
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


Name:           ProtonPlus
Version:        0.4.10
Release:        0
Summary:        A Wine and Proton-based compatibility tools manager for GNOME
License:        GPL-3.0-only
URL:            https://github.com/vysp3r/ProtonPlus
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  json-glib-devel
BuildRequires:  libgee-devel
BuildRequires:  libjson-glib-1_0-0
BuildRequires:  libsoup-devel
BuildRequires:  meson >= 0.62.0
BuildRequires:  ninja
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libarchive)

%description
ProtonPlus is a Proton version manager for installing and managing Proton
versions. It works with Steam, Lutris, Heroic Games Launcher and Bottles. It
uses GTK4.

%lang_package

%prep
%autosetup

%build
%meson --prefix=/usr
%meson_build

%install
%meson_install

%find_lang com.vysp3r.ProtonPlus

%fdupes %{buildroot}

%files
%{_bindir}/com.vysp3r.ProtonPlus
%{_datadir}/appdata/com.vysp3r.ProtonPlus.appdata.xml
%{_datadir}/applications/com.vysp3r.ProtonPlus.desktop
%{_datadir}/glib-2.0/schemas/com.vysp3r.ProtonPlus.gschema.xml
%{_datadir}/icons/hicolor/*

%files lang -f com.vysp3r.ProtonPlus.lang

%changelog
