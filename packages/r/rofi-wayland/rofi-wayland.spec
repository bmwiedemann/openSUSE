#
# spec file for package rofi-wayland
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rofi-wayland
Version:        1.7.8+wayland1+git.1737536808.03a3a58
Release:        0
Summary:        A window switcher, run dialog and dmenu replacement
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/lbonn/rofi
Source:         rofi-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  check-devel
BuildRequires:  flex >= 2.5.39
BuildRequires:  gcc-c++
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  librsvg-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  meson
BuildRequires:  pandoc
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  startup-notification-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
Conflicts:      rofi
Provides:       rofi-launcher

%description
This is a fork of rofi with added support for Wayland via the layer shell protocol.

%package devel
Summary:        Development files for rofi
Group:          Development/Libraries/C and C++
Conflicts:      rofi-devel

%description devel
Development files and headers for rofi

%prep
%autosetup -p1 -n rofi-%{version}

sed -i '1s,%{_bindir}/env bash,/bin/bash,' script/rofi-sensible-terminal \
    script/rofi-theme-selector

%build
%meson -Dxcb=disabled
%meson_build

%install
%meson_install

%files
%license COPYING
%doc Changelog README.md
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%dir %{_datadir}/rofi/
%{_datadir}/rofi/themes/
%{_datadir}/applications/rofi*
%{_datadir}/icons/hicolor/scalable/apps/rofi.svg
%{_mandir}/man1/rofi.1%{?ext_man}
%{_mandir}/man1/rofi-sensible-terminal.1%{?ext_man}
%{_mandir}/man1/rofi-theme-selector.1%{?ext_man}
%{_mandir}/man5/rofi-debugging.5%{?ext_man}
%{_mandir}/man5/rofi-dmenu.5%{?ext_man}
%{_mandir}/man5/rofi-keys.5%{?ext_man}
%{_mandir}/man5/rofi-script.5%{?ext_man}
%{_mandir}/man5/rofi-theme.5%{?ext_man}
%{_mandir}/man5/rofi-thumbnails.5%{?ext_man}

%files devel
%{_includedir}/rofi/
%{_libdir}/pkgconfig/rofi.pc

%changelog
