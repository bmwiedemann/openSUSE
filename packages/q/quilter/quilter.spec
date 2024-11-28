#
# spec file for package quilter
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


%define         appid io.github.lainsce.Quilter
Name:           quilter
Version:        3.3.4
Release:        0
Summary:        Writing application
License:        GPL-3.0-only
URL:            https://github.com/lainsce/quilter
Source:         https://github.com/lainsce/quilter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

%description
A fullscreen word processor for the Pantheon Desktop.

%lang_package

%prep
%autosetup

# use default font
sed -i '/QuiltMono.ttf/d' $(grep -rl QuiltMono.ttf)
sed -i '/QuiltVier.ttf/d' $(grep -rl QuiltVier.ttf)
sed -i '/QuiltZwei.ttf/d' $(grep -rl QuiltZwei.ttf)

%build
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types -Wno-int-conversion"
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{appid}
%{_datadir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/gtksourceview-4/styles/%{appid}*.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.svg
%{_datadir}/metainfo/%{appid}.appdata.xml

%files lang -f %{appid}.lang

%changelog
