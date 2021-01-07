#
# spec file for package faba-icon-theme
#
# Copyright (c) 2020 SUSE LLC
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


Name:           faba-icon-theme
Version:        4.3
Release:        0
Summary:        Faba Icon theme
License:        LGPL-3.0-or-later OR CC-BY-SA-4.0
Group:          System/GUI/Other
URL:            https://snwh.org/moka
Source:         https://github.com/moka-project/faba-icon-theme/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
BuildRequires:  meson
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       gnome-icon-theme

%description
Faba is a modern icon theme with Tango influences.

%prep
%setup -q
chmod a-x AUTHORS COPYING LICENSE_CC-BY-SA LICENSE_GPL README.md ./Faba/index.theme
find -name '*.svg' -type f -exec chmod a-x {} \;

%build
%meson
%meson_build

%install
%meson_install
rm -f %{buildroot}%{_datadir}/icons/Faba/AUTHORS
%{icon_theme_cache_create_ghost Faba}
%fdupes %{buildroot}%{_datadir}/icons/Faba

%post
%icon_theme_cache_post Faba

%postun
%icon_theme_cache_postun Faba

%files
%defattr(-,root,root)
%license COPYING LICENSE_CC-BY-SA LICENSE_GPL 
%doc AUTHORS README.md
%{_datadir}/icons/Faba
%ghost %{_datadir}/icons/Faba/icon-theme.cache

%changelog
