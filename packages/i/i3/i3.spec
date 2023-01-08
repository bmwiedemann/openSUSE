#
# spec file for package i3
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


Name:           i3
Version:        4.22
Release:        0
Summary:        Tiling window manager
License:        BSD-3-Clause
Group:          System/GUI/Other
URL:            https://i3wm.org/
Source0:        https://i3wm.org/downloads/%{name}-%{version}.tar.xz
Source1:        %{name}.png
Source2:        %{name}.keyring
Source3:        https://i3wm.org/downloads/%{name}-%{version}.tar.xz.asc
Patch1:         i3-desktop_file_valid.patch
BuildRequires:  asciidoc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libyajl-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xmlto
BuildRequires:  pkgconfig(cairo) >= 1.14.4
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libpcre2-8) >= 10
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon-x11)
# Required for i3-save-tree.
Requires:       perl-AnyEvent-I3
Recommends:     dmenu
Recommends:     i3lock
Recommends:     i3status
Recommends:     xorg-x11-server
Provides:       windowmanager
# Since 4.22, gaps are merged
Obsoletes:      i3-gaps < 4.19.1
# Upstream First - Policy:
# Never add any patches to this package without the upstream commit id
# in the patch. Any patches added here without a very good reason to make
# an exception will be silently removed with the next version update.

%description
i3 is a tiling window manager for X11. It supports tiling, stacking,
and tabbing layouts, which it handles dynamically. Configuration is
achieved via plain text file and extending i3 is possible using its
Unix domain socket and JSON based IPC interface.

%package devel
Summary:        Development headers for i3
Group:          Development/Libraries/C and C++
Requires:       %{name}

%description devel
Development headers for the i3 window manager.

%prep
%autosetup -p1

# fix rpmlint E: env-script-interpreter
sed -i 's,^#!/usr/bin/env ,#!/usr/bin/,' i3-dmenu-desktop i3-migrate-config-to-v4 i3-save-tree

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%license LICENSE
%doc RELEASE-NOTES-%{version}
%{_mandir}/man1/i3*.1%{?ext_man}
%{_bindir}/i3
%{_bindir}/i3-dump-log
%{_bindir}/i3-with-shmlog
%{_bindir}/i3bar
%{_bindir}/i3-config-wizard
%{_bindir}/i3-dmenu-desktop
%{_bindir}/i3-input
%{_bindir}/i3-migrate-config-to-v4
%{_bindir}/i3-msg
%{_bindir}/i3-nagbar
%{_bindir}/i3-save-tree
%{_bindir}/i3-sensible-editor
%{_bindir}/i3-sensible-pager
%{_bindir}/i3-sensible-terminal
%dir %{_sysconfdir}/i3/
%config %{_sysconfdir}/i3/config
%config %{_sysconfdir}/i3/config.keycodes
%{_datadir}/xsessions/i3.desktop
%{_datadir}/xsessions/i3-with-shmlog.desktop
%{_datadir}/applications/i3.desktop
%{_datadir}/pixmaps/i3.png
%{_datadir}/doc/i3/refcard_style.css
%{_datadir}/doc/i3/*.png

%files devel
%dir %{_includedir}/i3/
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/*.html
%{_includedir}/i3/ipc.h

%changelog
