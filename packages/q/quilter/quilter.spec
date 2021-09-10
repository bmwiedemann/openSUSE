#
# spec file for package quilter
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


Name:           quilter
Version:        3.3.4
Release:        0
Summary:        Writing application
License:        GPL-3.0-only
Group:          Productivity/Office/Word Processor
URL:            https://github.com/lainsce/quilter
Source:         https://github.com/lainsce/quilter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmarkdown-devel
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Recommends:     %{name}-lang

%description
A fullscreen word processor for Elementary OS.

%lang_package

%prep
%setup -q

# use default font
sed -i '/QuiltMono.ttf/d' $(grep -rl QuiltMono.ttf)
sed -i '/QuiltVier.ttf/d' $(grep -rl QuiltVier.ttf)
sed -i '/QuiltZwei.ttf/d' $(grep -rl QuiltZwei.ttf)

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r io.github.lainsce.Quilter GTK Utility TimeUtility
%find_lang io.github.lainsce.Quilter %{name}.lang
%fdupes %{buildroot}/%{_datadir}  

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/io.github.lainsce.Quilter
%{_datadir}/io.github.lainsce.Quilter/
%{_datadir}/applications/io.github.lainsce.Quilter.desktop
%{_datadir}/glib-2.0/schemas/io.github.lainsce.Quilter.gschema.xml
%{_datadir}/gtksourceview-4/styles/*.xml
%{_datadir}/icons/hicolor/*/apps/io.github.lainsce.Quilter*.??g
%{_datadir}/metainfo/io.github.lainsce.Quilter.appdata.xml

%files lang -f %{name}.lang

%changelog
