#
# spec file for package pantheon-bluetooth-daemon
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


%define         appid io.elementary.bluetooth
Name:           pantheon-bluetooth-daemon
Version:        1.0.0
Release:        0
Summary:        Send and receive files via Bluetooth
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/bluetooth-daemon
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
%{summary}.

%lang_package

%prep
%autosetup -n bluetooth-daemon-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%if 0%{?suse_version} >= 1600
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mv %{buildroot}%{_sysconfdir}/xdg/autostart/%{appid}.desktop \
   %{buildroot}%{_distconfdir}/xdg/autostart/%{appid}.desktop
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%if 0%{?suse_version} >= 1600
%{_distconfdir}/xdg/autostart/%{appid}.desktop
%else
%{_sysconfdir}/xdg/autostart/%{appid}.desktop
%endif
%dir %{_datadir}/icons/hicolor/{32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files lang -f %{appid}.lang

%changelog
