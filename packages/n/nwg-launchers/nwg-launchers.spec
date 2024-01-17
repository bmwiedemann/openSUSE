#
# spec file for package nwg-launchers
#
# Copyright (c) 2022 SUSE LLC
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


Name:           nwg-launchers
Version:        0.7.1.1
Release:        0
Summary:        GTK launchers and menu for sway and i3
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://github.com/nwg-piotr/nwg-launchers
Source:         %{url}/archive/v%{version}.tar.gz
Patch0:         nwg-launchers-readme.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  gtkmm3-devel
BuildRequires:  librsvg-devel
BuildRequires:  meson
BuildRequires:  nlohmann_json-devel

%description
GTK-based launchers: application grid, button bar, dmenu for sway and other window managers.

%prep
%setup -q
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/nwgbar
%{_bindir}/nwgdmenu
%{_bindir}/nwggrid
%{_bindir}/nwggrid-server
%dir %{_datadir}/nwg-launchers
%{_datadir}/nwg-launchers/nwgbar
%{_datadir}/nwg-launchers/nwgdmenu
%{_datadir}/nwg-launchers/nwggrid
%{_datadir}/nwg-launchers/icon-missing.png
%{_datadir}/nwg-launchers/icon-missing.svg

%changelog
