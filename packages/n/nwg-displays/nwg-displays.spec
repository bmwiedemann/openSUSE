#
# spec file for package nwg-displays
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


Name:           nwg-displays
Version:        0.3.10
Release:        0
Summary:        A GTK3 wrapper to display text on the desktop for wlroots
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-displays
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       libgtk-3-0
Requires:       libgtk-layer-shell0
Requires:       python3-gobject
Requires:       python3-i3ipc
Requires:       typelib(GtkLayerShell)
Recommends:     wlr-randr
BuildArch:      noarch

%description

nwg-displays is Output management utility for sway Wayland compositor,
inspired by wdisplays and wlay.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

install -Dpm 0644 %{name}.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0644 nwg-displays.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0755 %{name}.desktop -t %{buildroot}%{_datadir}/applications/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{python_sitelib}/*

%changelog
