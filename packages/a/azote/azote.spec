#
# spec file for package azote
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


%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
Name:           azote
Version:        1.7.14
Release:        0
Summary:        Wallpaper manager for Sway, i3 and some other WMs
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/nwg-piotr/azote
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gobject-introspection
BuildRequires:  python3-Pillow
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
Requires:       feh
Requires:       python3-Pillow
Requires:       python3-Send2Trash
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       wget
Requires:       wmctrl
Requires:       xrandr
# for screen color picker on both Sway and X11
Requires:       ImageMagick
# for alacritty.yml toolbox
Requires:       python3-PyYAML
BuildArch:      noarch

%description
Azote is a GTK+ 3-based picture browser and a wallpaper setter, as the frontend to the swaybg (Sway/Wayland) and feh (X windows) commands.

%prep
%setup -q

%build
%python3_build

%install
%python3_install
install -D -m 0755 dist/azote %{buildroot}%{_bindir}/azote
install -D -m 0644 dist/azote.svg %{buildroot}%{_datadir}/azote/azote.svg
install -D -m 0644 dist/azote.desktop %{buildroot}%{_datadir}/applications/azote.desktop

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/azote
%{_datadir}/applications/azote.desktop
%{_datadir}/azote/
%{python_sitelib}/*

%changelog
