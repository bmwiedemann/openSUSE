#
# spec file for package switcheroo
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


%define appid   io.gitlab.adhami3310.Converter
%define rurl    d9666e26d4a8a183ea1b1ca5d9b6cd1a
Name:           switcheroo
Version:        2.2.0
Release:        0
Summary:        Convert and manipulate images
License:        GPL-3.0-only
URL:            https://gitlab.com/adhami3310/Switcheroo
Source:         %{url}/uploads/%{rurl}/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  blueprint-compiler
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

%description
Switcheroo is designed to give you a simple, quick, and easy-to-use tool
to convert and manipulate your images in whatever way you like. It is
built on top of the most advanced image editing libraries, ImageMagick.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%license COPYING
%doc README*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appid}*svg
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{name}.lang

%changelog
