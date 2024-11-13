#
# spec file for package cinnamon-session
#
# Copyright (c) 2024 SUSE LLC
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


Name:           cinnamon-session
Version:        6.2.1
Release:        0
Summary:        The session manager for the Cinnamon Desktop
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/linuxmint/cinnamon-session
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-logind.gschema.override
BuildRequires:  docbook
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
BuildRequires:  update-desktop-files
BuildRequires:  xmlto
BuildRequires:  xtrans
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoxft)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xapp) >= 1.2.0
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xtst)
Requires:       /usr/bin/dbus-launch
Requires:       cinnamon
Requires:       cinnamon-settings-daemon
Requires:       upower >= 0.9.0

%description
This packages contains the session manager for the Cinnamon Desktop.

%prep
%autosetup

%build
%meson \
  -Dfrequent_warnings=true \
  -Dipv6=true    \
  -Dxtrans=true
%meson_build

%install
%meson_install

# We should own this directory.
mkdir -p %{buildroot}%{_datadir}/%{name}/sessions/

# Use systemd-logind for suspend by default.
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_datadir}/glib-2.0/schemas/org.cinnamon.desktop.session.gschema.override

%files
%license COPYING
%doc AUTHORS README README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-quit
%{_libexecdir}/*
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.cinnamon.*
%{_datadir}/icons/hicolor/*/apps/%{name}-properties.*
%{_mandir}/man?/%{name}*.?%{?ext_man}

%changelog
