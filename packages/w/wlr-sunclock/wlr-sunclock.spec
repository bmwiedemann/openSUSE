#
# spec file for package wlr-sunclock
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


Name:           wlr-sunclock
Version:        1.0.0
Release:        0
Summary:        Wayland desktop widget to show to the sun's shadows on earth
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://github.com/sentriz/wlr-sunclock
Source:         https://github.com/sentriz/wlr-sunclock/archive/v%{version}.tar.gz
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(librsvg-2.0)

%description
Wayland desktop widget to show to the sun's shadows on earth.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENCE
%doc README.md
%{_bindir}/%{name}

%changelog
