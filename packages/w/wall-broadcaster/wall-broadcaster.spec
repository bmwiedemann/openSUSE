#
# spec file for package wall-broadcaster
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           wall-broadcaster
Version:        0.4.0+git20260513.fc6c03a
Release:        0
Summary:        Service to broadcast wall messages via dbus
License:        GPL-2.0-or-later
URL:            https://github.com/thkukuk/wall-broadcaster
Source:         %{name}-%{version}.tar.xz
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libsystemd) >= 257

%description
Wall Broadcaster is a service which registers itself as session with
systemd-logind, listens to it's TTY for wall messages and forwards
them via D-BUS. Clients, e.g. for graphical desktops, can listen to it
and display the messages to the user.

%package gtk4
Summary:        GTK4 application showing wall broadcast messages

%description gtk4
This package contains a GTK4 application, which watches for dbus
messages from wall-broadcaster and displays them.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%pre
%service_add_pre wall-broadcaster.service

%preun
%service_del_preun wall-broadcaster.service

%post
%service_add_post wall-broadcaster.service

%postun
%service_del_postun wall-broadcaster.service

%files
%license LICENSE
%doc README.md
%{_bindir}/wall-bcst-gateway
%{_bindir}/wall-bcst-send
%{_bindir}/wall-bcst-watcher
%{_datadir}/applications/wall-bcst-gateway.desktop
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.opensuse.WallBroadcast.conf
%{_libexecdir}/wall-broadcaster
%{_mandir}/man1/wall-bcst-gateway.1%{?ext_man}
%{_mandir}/man1/wall-bcst-send.1%{?ext_man}
%{_mandir}/man1/wall-bcst-watcher.1%{?ext_man}
%{_mandir}/man8/wall-broadcaster.8%{?ext_man}
%{_prefix}/lib/systemd/system/wall-broadcaster.service

%files gtk4
%license LICENSE
%{_bindir}/wall-bcst-watcher-gtk4
%{_datadir}/applications/wall-bcst-watcher.desktop
%{_mandir}/man1/wall-bcst-watcher-gtk4.1%{?ext_man}

%changelog
