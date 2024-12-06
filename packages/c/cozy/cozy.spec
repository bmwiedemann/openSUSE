#
# spec file for package cozy
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


%define         appid com.github.geigi.cozy
Name:           cozy
Version:        1.3.0
Release:        0
Summary:        Audio Book Player
License:        GPL-3.0-only
URL:            https://github.com/geigi/cozy
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-distro
BuildRequires:  python3-gobject
BuildRequires:  python3-mutagen
BuildRequires:  python3-peewee
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5.0
BuildRequires:  pkgconfig(python3)
Requires:       python3-distro
Requires:       python3-injector
Requires:       python3-mutagen
Requires:       python3-peewee
Requires:       python3-pytz
Requires:       python3-requests
Recommends:     gstreamer-plugins-base
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-ugly
Provides:       %{appid} = %{version}
Obsoletes:      %{appid} < %{version}
BuildArch:      noarch

%description
Play and organize your audio book collection.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license LICENSE
%doc AUTHORS.md README.md
%attr(0755,root,root) %{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/icons/hicolor/*/apps/%{appid}{.Devel,-symbolic}.svg
%{_datadir}/icons/hicolor/*/actions/*.svg
%{_datadir}/%{appid}
%{python3_sitelib}/%{name}

%files lang -f %{appid}.lang

%changelog
