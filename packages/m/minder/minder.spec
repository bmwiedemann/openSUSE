#
# spec file for package minder
#
# Copyright (c) 2020 SUSE LLC
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


Name:           minder
Version:        1.11.1
Release:        0
Summary:        Mind-mapping app
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://github.com/phase1geo
Source:         https://github.com/phase1geo/Minder/archive/%{version}.tar.gz#/Minder-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-lang

%description
A program to create, develop, visualize, organize and manage ideas.

%lang_package

%prep
%setup -q -n Minder-%{version}

# Fix: script-without-shebang
find -name \*.svg -exec chmod 0644 {} \+

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.phase1geo.minder GTK Office FlowChart
%find_lang com.github.phase1geo.minder %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/com.github.phase1geo.minder
%{_datadir}/applications/com.github.phase1geo.minder.desktop
%{_datadir}/glib-2.0/schemas/com.github.phase1geo.minder.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.??g
%{_datadir}/metainfo/com.github.phase1geo.minder.appdata.xml
%{_datadir}/mime/packages/com.github.phase1geo.minder.xml
%{_datadir}/gtksourceview-3.0/

%files lang -f %{name}.lang

%changelog
