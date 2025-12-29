#
# spec file for package tags
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           tags
Version:        1.8
Release:        0
Summary:        A simple text tagger
License:        X11
URL:            https://github.com/phastmike/tags
Source:         https://github.com/phastmike/tags/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6

%description
A GNOME text tagger inspired by the TextAnalysisTool.NET tool.

The main goal is to aid log analysis by tagging lines with user defined colors.
Tags have a match pattern, description name, visibility toggle, color scheme
and hit counter.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/tags
%{_datadir}/appdata/io.github.phastmike.tags.appdata.xml
%{_datadir}/applications/io.github.phastmike.tags.desktop
%{_datadir}/glib-2.0/schemas/io.github.phastmike.tags.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.github.phastmike.tags.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.github.phastmike.tags-symbolic.svg

%changelog
