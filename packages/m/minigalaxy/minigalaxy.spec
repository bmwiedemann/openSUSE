#
# spec file for package minigalaxy
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.9.2
Release:        0
Summary:        A GOG client for Linux that lets you download and play your GOG Linux games
License:        GPL-3.0-only
URL:            https://github.com/sharkwouter/minigalaxy
Source0:        https://github.com/sharkwouter/minigalaxy/archive/%{version}.tar.gz
Patch0:         minigalaxy-0.9.0-desktop.patch
BuildRequires:  gobject-introspection
BuildRequires:  python3
BuildRequires:  python3-setuptools
Requires:       python3-gobject >= 3.30
Requires:       python3-gobject-Gdk
Requires:       python3-requests
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
%{_bindir}/minigalaxy
%{_datadir}/applications/minigalaxy.desktop
%{_datadir}/minigalaxy/
%dir %{_datadir}/icons
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/192x192/
%{_datadir}/icons/hicolor/192x192/apps/
%{_datadir}/metainfo/minigalaxy.metainfo.xml
%{python3_sitelib}/{m,M}inigalaxy*

%changelog
