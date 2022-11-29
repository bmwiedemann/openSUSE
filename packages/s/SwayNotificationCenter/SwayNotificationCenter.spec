#
# spec file for package SwayNotificationCenter
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


Name:           SwayNotificationCenter
Version:        0.7.3
Release:        0
Summary:        A simple GTK notification daemon
License:        GPL-3.0-only
URL:            https://github.com/ErikReider/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(systemd)

%description
A simple notification daemon with a GTK gui for notifications and the control center

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/xdg/swaync
%config %{_sysconfdir}/xdg/swaync/config.json
%config %{_sysconfdir}/xdg/swaync/configSchema.json
%config %{_sysconfdir}/xdg/swaync/style.css
%{_bindir}/swaync
%{_bindir}/swaync-client
%{_userunitdir}/swaync.service
%{_datadir}/bash-completion/completions/swaync
%{_datadir}/bash-completion/completions/swaync-client
%{_datadir}/dbus-1/services/org.erikreider.swaync.service
%{_datadir}/glib-2.0/schemas/org.erikreider.swaync.gschema.xml
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/swaync-client.fish
%{_datadir}/fish/vendor_completions.d/swaync.fish
%{_mandir}/man1/swaync-client.1%{?ext_man}
%{_mandir}/man1/swaync.1%{?ext_man}
%{_mandir}/man5/swaync.5%{?ext_man}
%{_datadir}/zsh/site-functions/_swaync
%{_datadir}/zsh/site-functions/_swaync-client

%changelog
