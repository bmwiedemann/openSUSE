#
# spec file for package image-optimizer
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         appid com.github.gijsgoudzwaard.image-optimizer
Name:           image-optimizer
Version:        0.5.0
Release:        0
Summary:        Simple lossless image compression
License:        GPL-3.0-or-later
URL:            https://github.com/gijsgoudzwaard/Image-Optimizer
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12
Requires:       jpegoptim
Requires:       optipng

%description
Compress your images with ease using JpegOptim and OptiPng.

%lang_package

%prep
%autosetup -n Image-Optimizer-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

#fix upstream
chmod -x %{buildroot}%{_datadir}/icons/hicolor/*/apps/%{appid}.svg

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml

%files lang -f %{appid}.lang

%changelog
