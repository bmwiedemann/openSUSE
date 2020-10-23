#
# spec file for package mint-x-icon-theme
#
# Copyright (c) 2020 SUSE LLC
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


%define _name   Mint-X
Name:           mint-x-icon-theme
Version:        1.5.5
Release:        0
Summary:        Mint-X icon theme
License:        GPL-3.0-or-later
URL:            https://github.com/linuxmint/mint-x-icons
Source:         http://packages.linuxmint.com/pool/main/m/mint-x-icons/mint-x-icons_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
A mint/metal theme based on mintified versions of
Clearlooks Revamp, Elementary and Faenza.

%prep
%setup -q -n mint-x-icons

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/icons/
ls .%{_datadir}/icons/ | while read icons; do
    sed -i 's/^\(Inherits=\).*$/\1Adwaita/' .%{_datadir}/icons/$icons/index.theme
    cp -a .%{_datadir}/icons/$icons %{buildroot}%{_datadir}/icons/$icons
    # %%icon_theme_cache_create_ghost fails to work here.
    touch %{buildroot}%{_datadir}/icons/$icons/icon-theme.cache
done
%fdupes %{buildroot}%{_datadir}/icons/

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post %{_name}
%icon_theme_cache_post %{_name}-Aqua
%icon_theme_cache_post %{_name}-Blue
%icon_theme_cache_post %{_name}-Brown
%icon_theme_cache_post %{_name}-Dark
%icon_theme_cache_post %{_name}-Grey
%icon_theme_cache_post %{_name}-Orange
%icon_theme_cache_post %{_name}-Pink
%icon_theme_cache_post %{_name}-Purple
%icon_theme_cache_post %{_name}-Red
%icon_theme_cache_post %{_name}-Sand
%icon_theme_cache_post %{_name}-Teal
%icon_theme_cache_post %{_name}-Yellow

# No need for %%icon_theme_cache_postun in %%postun since themes won't exist anymore.
%endif

%files
%license debian/copyright
%doc debian/changelog
%{_datadir}/icons/%{_name}*
%ghost %{_datadir}/icons/%{_name}*/icon-theme.cache

%changelog
