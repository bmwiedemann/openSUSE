#
# spec file for package gcolor3
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global         commit be7d539383da129c0e8187946a67e062f934c8dc
%global         rev git78
Name:           gcolor3
Version:        2.3.1+%{rev}
Release:        0
Summary:        A color chooser written in GTK3 (like gcolor2)
License:        GPL-2.0-only
Group:          Productivity/Graphics/Other
URL:            https://gitlab.gnome.org/World/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.gz
Source0:        %{name}-%{commit}.tar.gz
Patch0:         gcolor3-suse.patch
BuildRequires:  cmake
BuildRequires:  gnome-common
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Gcolor3 enables picking the color from any pixel on the screen. It
also offers a palette to mix and match a couple of colors together.
Colors can be saved and retrieved.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install
%find_lang gcolor3

%files -f gcolor3.lang
%license LICENSE
%doc README.md
%attr(0755,-,-) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/metainfo/nl.hjdskes.gcolor3.appdata.xml
%{_datadir}/applications/nl.hjdskes.gcolor3.desktop
%{_datadir}/icons/hicolor/scalable/apps/nl.hjdskes.gcolor3.svg
%{_datadir}/icons/hicolor/symbolic/apps/nl.hjdskes.gcolor3-symbolic.svg

%changelog
