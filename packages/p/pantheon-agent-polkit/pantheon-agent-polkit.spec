#
# spec file for package pantheon-agent-polkit
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


%define         appid io.elementary.desktop.agent-polkit
Name:           pantheon-agent-polkit
Version:        8.0.1
Release:        0
Summary:        Polkit authorization designed for Pantheon
License:        LGPL-2.1-or-later
URL:            https://github.com/elementary/pantheon-agent-polkit
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pantheon-wayland-1)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)

%description
An agent for Polkit authorization designed for Pantheon desktop environment.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes -s %{buildroot}%{_datadir}

%if %{?suse_version} >= 1600
# move the xdg autostart file into /usr/etc
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mv %{buildroot}%{_sysconfdir}/xdg/autostart/%{appid}.desktop \
   %{buildroot}%{_distconfdir}/xdg/autostart/%{appid}.desktop
%endif

%files
%license COPYING
%doc README.md
%{_datadir}/applications/%{appid}.desktop
%{_libexecdir}/policykit-1-pantheon
%if %{?suse_version} >= 1600
%{_distconfdir}/xdg/autostart/%{appid}.desktop
%else
%{_sysconfdir}/xdg/autostart/%{appid}.desktop
%endif
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{appid}.lang

%changelog
