#
# spec file for package imageburner
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


%define         appid com.github.artemanufrij.imageburner
Name:           imageburner
Version:        1.0.2
Release:        0
Summary:        Image burner
License:        GPL-3.0-or-later
URL:            https://github.com/artemanufrij/imageburner
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  contractor
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22

%description
An image burner, written especially for the Pantheon Desktop.

%lang_package

%prep
%autosetup

mv debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/{apps,mimetypes}/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/contractor/%{appid}.contract

%files lang -f %{appid}.lang

%changelog
