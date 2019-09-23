#
# spec file for package gcolor3
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gcolor3
Version:        2.3.1
Release:        0
Summary:        A color chooser written in GTK3 (like gcolor2)
License:        GPL-2.0-only
Group:          Productivity/Graphics/Other
URL:            https://gitlab.gnome.org/World/gcolor3
Source0:        gcolor3.tar.gz
Patch0:         gcolor3-suse.patch
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
%autosetup -p1

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
%{_datadir}/locale/cs/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/de/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/el/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/es/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/fi/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/fr/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/gl/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/id/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/nb/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/nl/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/pl/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/ru/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/sr/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/sv/LC_MESSAGES/gcolor3.mo
%{_datadir}/locale/uk/LC_MESSAGES/gcolor3.mo

%changelog
