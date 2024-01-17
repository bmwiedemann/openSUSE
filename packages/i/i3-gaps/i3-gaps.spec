#
# spec file for package i3-gaps
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


Name:           i3-gaps
Version:        4.21.1
Release:        0
Summary:        Tiling window manager
License:        BSD-3-Clause
Group:          System/GUI/Other
URL:            https://github.com/Airblader/i3
Source0:        https://github.com/Airblader/i3/releases/download/%{version}/i3-%{version}.tar.xz#/%{name}-%{version}.tar.xz
BuildRequires:  asciidoc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libyajl-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xmlto
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon-x11)
# So that M-enter works in the default config. boo#985443
Recommends:     dmenu
Recommends:     i3lock
# introduced to fix bnc#971897 and boo#985443
Recommends:     i3status
Conflicts:      i3
# Needed to fix bnc#992972
Provides:       i3
Provides:       windowmanager
# Upstream First - Policy:
# Never add any patches to this package without the upstream commit id
# in the patch. Any patches added here without a very good reason to make
# an exception will be silently removed with the next version update.

%description
i3-gaps is a fork of i3, which adds features such as gaps between tiles.

%package devel
Summary:        Development headers for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}
# i3 and i3-gaps both provide /usr/include/i3/ipc.h and the same docs
Conflicts:      i3-devel

%description devel
Development headers for the %{name} window manager

%prep
%setup -q -n i3-%{version}

# fix rpmlint E: env-script-interpreter
sed -i 's,^#!/usr/bin/env ,#!/usr/bin/,' i3-dmenu-desktop i3-migrate-config-to-v4 i3-save-tree

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/i3.desktop

%files
%license LICENSE
%doc RELEASE-NOTES-*
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
%{_datadir}/doc/i3/refcard_style.css
%{_datadir}/doc/i3/*.png

%files devel
%dir %{_includedir}/i3/
%dir %{_datadir}/doc/i3
%doc %{_datadir}/doc/i3/*.html
%{_includedir}/i3/ipc.h

%changelog
