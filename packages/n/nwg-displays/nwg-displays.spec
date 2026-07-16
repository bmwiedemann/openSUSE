#
# spec file for package nwg-displays
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           nwg-displays
Version:        0.4.3
Release:        0
Summary:        Output management utility for sway, Hyprland and Niri
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-displays
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-gobject
Requires:       python3-i3ipc
Requires:       typelib(GtkLayerShell)
BuildArch:      noarch

%description

nwg-displays is an output management utility for the Sway, Hyprland and Niri Wayland compositors,
inspired by wdisplays and wlay.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

install -Dpm 0644 %{name}.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0644 %{name}.desktop -t %{buildroot}%{_datadir}/applications/

# remove unnecessary shebangs
sed -i '1{/^#!.*python.*/d;}' \
   %{buildroot}%{python3_sitelib}/nwg_displays/main.py \
   %{buildroot}%{python3_sitelib}/nwg_displays/profiles.py \
   %{buildroot}%{python3_sitelib}/nwg_displays/tools.py

%fdupes %{buildroot}%{python3_sitelib}/nwg_displays

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-apply
%{_bindir}/%{name}-toggle-wallpapers
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.svg
%{python3_sitelib}/nwg_displays
%{python3_sitelib}/nwg_displays-*.egg-info

%changelog
