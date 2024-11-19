#
# spec file for package pantheon-shortcut-overlay
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


%define         appid io.elementary.shortcut-overlay
Name:           pantheon-shortcut-overlay
Version:        8.0.0
Release:        0
Summary:        A native OS-wide shortcut overlay to be launched by Gala
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/shortcut-overlay
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
Provides:       elementary-shortcut-overlay = %{version}
Obsoletes:      elementary-shortcut-overlay < %{version}

%description
This Granite applet should read window manager and OS keyboard shortcuts from
dconf and expose them to the user when launched.

%lang_package

%prep
%autosetup -n shortcut-overlay-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{appid}.lang

%changelog
