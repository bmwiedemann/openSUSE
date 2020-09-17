#
# spec file for package cinnamon-session
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.6.2
Release:        0
Summary:        The session manager for the Cinnamon Desktop
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon-session
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-logind.gschema.override
BuildRequires:  docbook
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
BuildRequires:  update-desktop-files
BuildRequires:  xmlto
BuildRequires:  xtrans
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gconf-2.0)
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
Requires:       cinnamon
Requires:       cinnamon-settings-daemon
Requires:       dbus-1-x11
Requires:       upower >= 0.9.0
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
This packages contains the session manager for the Cinnamon Desktop.

%prep
%setup -q

%build
%meson \
  -Dwith-docbook=true \
  -Dwith-gconf=false  \
%if 0%{?suse_version} >= 1500
  -Dwith-qt5-theme-support=true \
%else
  -Dwith-qt5-theme-support=false \
%endif
  -Dwith-ipv6=true    \
  -Dwith-xtrans=true
%meson_build

%install
%meson_install

# We should own this directory.
mkdir -p %{buildroot}%{_datadir}/%{name}/sessions/

# Fix documentation location.
mkdir -p %{buildroot}%{_docdir}/
mv -f %{buildroot}%{_datadir}/doc/%{name}/ \
  %{buildroot}%{_docdir}/%{name}/

# Use systemd-logind for suspend by default.
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_datadir}/glib-2.0/schemas/org.cinnamon.desktop.session.gschema.override

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS README README.md
%dir %{_docdir}/%{name}/dbus/
%doc %{_docdir}/%{name}/dbus/%{name}.html
%{_bindir}/%{name}
%{_bindir}/%{name}-quit
%{_libexecdir}/%{name}-check-accelerated*
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.cinnamon.*
%{_datadir}/icons/hicolor/*/apps/%{name}-properties.*
%{_mandir}/man?/%{name}*.?%{?ext_man}

%changelog
