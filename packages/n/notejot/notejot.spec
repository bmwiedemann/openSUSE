#
# spec file for package notejot
#
# Copyright (c) 2021 SUSE LLC
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


Name:           notejot
Version:        3.4.9
Release:        0
Summary:        A Sticky Note App
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://lainsce.us/
Source:         https://github.com/lainsce/notejot/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
Recommends:     %{name}-lang

%description
A sticky notes application for any type of short term notes
or ideas.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang io.github.lainsce.Notejot %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/io.github.lainsce.Notejot
%{_datadir}/applications/io.github.lainsce.Notejot.desktop
%{_datadir}/glib-2.0/schemas/io.github.lainsce.Notejot.gschema.xml
%{_datadir}/icons/hicolor/*/apps/io.github.lainsce.Notejot*.??g
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/metainfo/io.github.lainsce.Notejot.appdata.xml

%files lang -f %{name}.lang

%changelog
