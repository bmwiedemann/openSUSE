#
# spec file for package grim
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


Name:           grim
Version:        1.4.1
Release:        0
Summary:        Wayland compositor image grabber
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://git.sr.ht/~emersion/grim
Source:         https://git.sr.ht/~emersion/grim/refs/download/v%{version}/grim-%{version}.tar.gz
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14

%description
This tool can grab images from a Wayland compositor.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*

%changelog
