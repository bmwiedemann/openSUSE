#
# spec file for package pantheon-onboarding
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


%define         appid io.elementary.onboarding
Name:           pantheon-onboarding
Version:        8.0.3
Release:        0
Summary:        Setting General Preferences
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/onboarding
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pantheon-wayland-1)
Provides:       elementary-onboarding = %{version}
Obsoletes:      elementary-onboarding < %{version}

%description
Quickly change common settings on first-run.

%lang_package

%prep
%autosetup -n onboarding-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} >= 1600
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mv %{buildroot}%{_sysconfdir}/xdg/autostart/%{appid}.desktop \
   %{buildroot}%{_distconfdir}/xdg/autostart/%{appid}.desktop
%endif

%files
%license COPYING
%doc README.md
%{_sysconfdir}/guest-session
%if 0%{?suse_version} >= 1600
%{_distconfdir}/xdg/autostart/%{appid}.desktop
%else
%{_sysconfdir}/xdg/autostart/%{appid}.desktop
%endif
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files lang -f %{appid}.lang

%changelog
