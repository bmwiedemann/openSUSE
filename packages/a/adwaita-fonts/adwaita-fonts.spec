#
# spec file for package adwaita-fonts
#
# Copyright (c) 2025 SUSE LLC
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


Name:           adwaita-fonts
Version:        48.2
Release:        0
Summary:        Adwaita Fonts
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/adwaita-fonts
Source:         https://download.gnome.org/sources/adwaita-fonts/48/%{name}-%{version}.tar.xz

# needed for directory ownership
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Adwaita Sans, a variation of Inter, and Adwaita Mono, Iosevka
customized to match Inter.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%reconfigure_fonts_scriptlets

%files
%license LICENSE
%doc README.md
%dir %{_fontsdir}/Adwaita
%{_fontsdir}/Adwaita/AdwaitaMono-Bold.ttf
%{_fontsdir}/Adwaita/AdwaitaMono-BoldItalic.ttf
%{_fontsdir}/Adwaita/AdwaitaMono-Italic.ttf
%{_fontsdir}/Adwaita/AdwaitaMono-Regular.ttf
%{_fontsdir}/Adwaita/AdwaitaSans-Italic.ttf
%{_fontsdir}/Adwaita/AdwaitaSans-Regular.ttf

%changelog

