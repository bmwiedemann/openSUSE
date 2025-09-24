#
# spec file for package adwaita-icon-theme-legacy
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           adwaita-icon-theme-legacy
Version:        46.2
Release:        0
Summary:        GNOME Icon Theme - Legacy fallback icons
License:        CC-BY-SA-3.0 OR LGPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme-legacy
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  fdupes
BuildRequires:  gtk3-tools >= 3.24.2
BuildRequires:  meson >= 0.64.0
BuildRequires:  pkgconfig
# To make sure the icon theme cache gets generated
Requires(post): (gtk3-tools if libgtk-3-0)
Requires(post): (gtk4-tools if libgtk-4-1)
BuildArch:      noarch

%description
A fullcolor icon theme providing fallback for legacy apps.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%dnl we package those license files properly using %license
rm -r %{buildroot}%{_datadir}/licenses/adwaita-icon-theme
%{icon_theme_cache_create_ghost AdwaitaLegacy}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING COPYING_LGPL COPYING_CCBYSA3
%doc NEWS
%ghost %{_datadir}/icons/AdwaitaLegacy/icon-theme.cache
%{_datadir}/icons/AdwaitaLegacy/
%{_datadir}/pkgconfig/adwaita-icon-theme-legacy.pc

%changelog
