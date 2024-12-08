#
# spec file for package agenda
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


%define         appid com.github.dahenson.agenda
Name:           agenda
Version:        1.1.2
Release:        0
Summary:        Task Manager for Elementary
License:        GPL-3.0-or-later
URL:            https://github.com/dahenson/agenda
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(vapigen) >= 0.26.0
Provides:       agenda-tasks = %{version}
Obsoletes:      agenda-tasks < %{version}

%description
A task manager for the Pantheon Desktop.

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
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2,64x64@2/apps}

%files lang -f %{appid}.lang

%changelog
