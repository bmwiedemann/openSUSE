#
# spec file for package moka-icon-theme
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2016 Sam Hewitt
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


Name:           moka-icon-theme
Version:        5.4.0
Release:        0
Summary:        Moka Icon theme
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://snwh.org/moka
Source:         https://github.com/snwh/moka-icon-theme/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
BuildRequires:  meson
BuildArch:      noarch

%description
Moka is a simple and modern icon theme with Material Design influences.

%prep
%setup -q
find -L . -type l -print -delete
chmod a-x AUTHORS README.md

%build
%meson
%meson_build

%install
%meson_install
rm -f %{buildroot}%{_datadir}/icons/Moka/AUTHORS
%fdupes %{buildroot}%{_datadir}/icons/Moka

%post
%icon_theme_cache_post Moka

%files
%license COPYING
%doc AUTHORS LICENSE_* README.md
%{_datadir}/icons/Moka
%ghost %{_datadir}/icons/Moka/icon-theme.cache

%changelog
