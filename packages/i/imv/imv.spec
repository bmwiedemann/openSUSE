#
# spec file for package imv
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


Name:           imv
Version:        4.4.0
Release:        0
Summary:        Image viewer for X11/Wayland
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Graphics/Viewers
URL:            https://git.sr.ht/~exec64/imv
Source:         https://git.sr.ht/~exec64/imv/archive/v%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  freeimage-devel
BuildRequires:  libicu-devel
BuildRequires:  libinih-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.44
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)

%description
imv is a command line image viewer intended for use with tiling window managers.

%prep
%autosetup -n %{name}-v%{version}

%build
%meson -Dlibnsgif=disabled
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-dir.desktop
%{_mandir}/man?/%{name}*
%{_sysconfdir}/%{name}_config

%changelog
