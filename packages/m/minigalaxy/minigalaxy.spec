#
# spec file for package minigalaxy
#
# Copyright (c) 2019 SUSE LLC
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


Name:           minigalaxy
Version:        0.9.1
Release:        0
Summary:        A GOG client for Linux that lets you download and play your GOG Linux games
License:        GPL-3.0
URL:            https://github.com/sharkwouter/minigalaxy
Source0:        https://github.com/sharkwouter/minigalaxy/archive/%{version}.tar.gz
Patch0:         minigalaxy-0.9.0-desktop.patch
BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildRequires:  gobject-introspection 
Requires:       python3-gobject >= 3.30
Requires:       python3-requests
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%description
A GOG client for Linux that lets you download and play your GOG Linux games.

%prep
%setup -q
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%license LICENSE
/usr/bin/minigalaxy
/usr/share/applications/minigalaxy.desktop
/usr/share/minigalaxy/
/usr/share/pixmaps/minigalaxy.png
%{python3_sitelib}/{m,M}inigalaxy*

%changelog
