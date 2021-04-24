#
# spec file for package mint-y-icon-theme
#
# Copyright (c) 2021 SUSE LLC
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


%define _name   Mint-Y
Name:           mint-y-icon-theme
Version:        1.5.0
Release:        0
Summary:        Mint-Y icon theme
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later
URL:            https://github.com/linuxmint/mint-y-icons
Source:         http://packages.linuxmint.com/pool/main/m/mint-y-icons/mint-y-icons_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
Requires:       adwaita-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
The flat, colourful, and modern theme based on Paper and Moka.

%prep
%setup -q -n mint-y-icons

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/icons/

for color in Mint-Y Mint-Y-Aqua Mint-Y-Blue Mint-Y-Brown \
Mint-Y-Grey Mint-Y-Orange Mint-Y-Pink Mint-Y-Purple Mint-Y-Red \
Mint-Y-Sand Mint-Y-Teal Mint-Y-Yellow
    do cp -a .%{_datadir}/icons/${color} %{buildroot}%{_datadir}/icons/${color}
    %icon_theme_cache_create_ghost ${color}
done

%fdupes %{buildroot}%{_datadir}/icons/

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post %{_name}*

# No need for %%icon_theme_cache_postun in %%postun since themes won't exist anymore.
%endif

%files
%license debian/copyright
%doc debian/changelog
%{_datadir}/icons/%{_name}*
%ghost %{_datadir}/icons/%{_name}*/icon-theme.cache

%changelog
