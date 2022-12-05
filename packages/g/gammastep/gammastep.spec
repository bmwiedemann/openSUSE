#
# spec file for package gammastep
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


%define __requires_exclude typelib\\(AppIndicator3\\)
Name:           gammastep
Version:        2.0.9
Release:        0
Summary:        Adjusts the color temperature of your screen according to time of day
License:        GPL-3.0-or-later
URL:            https://gitlab.com/chinstrap/gammastep
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-devel >= 3.2
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gio-2.0) >= 2.26
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner) >= 1.15.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xxf86vm)
Requires:       hicolor-icon-theme

%description
Gammastep adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in front
of the screen at night.

The color temperature is set according to the position of the sun. A different
color temperature is set during night and daytime. During twilight and early
morning, the color temperature transitions smoothly from night to daytime
temperature to allow your eyes to slowly adapt.

Gammastep supports wlr-gamma-control-unstable-v1 protocol for wlroots-based
wayland compositors.

%package        indicator
Summary:        GTK indicator applet for %{name}
Requires:       python3dist(pygobject)
Requires:       python3dist(pyxdg)

%description    indicator
This package provides a status icon for %{name} that allows the user
to control color temperature.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
./bootstrap
%configure \
    --with-systemduserunitdir=%{_userunitdir}
%make_build

%install
%make_install
sed -i 's|/env python3|/python3|' %{buildroot}%{_bindir}/%{name}-indicator
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%post
%systemd_user_post %{name}.service

%post indicator
%systemd_user_post %{name}-indicator.service

%preun
%systemd_user_preun %{name}.service

%preun indicator
%systemd_user_preun %{name}-indicator.service

%files -f %{name}.lang
%license COPYING
%doc README.md %{name}.conf.sample
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_userunitdir}/%{name}.service

%files indicator
%{_bindir}/%{name}-indicator
%{_datadir}/applications/%{name}-indicator.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-status-*.svg
%{_datadir}/metainfo/%{name}-indicator.appdata.xml
%{_userunitdir}/%{name}-indicator.service
%{python3_sitelib}/%{name}_indicator/

%changelog
