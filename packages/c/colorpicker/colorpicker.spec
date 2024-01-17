#
# spec file for package colorpicker
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


Name:           colorpicker
Version:        1.1.5
Release:        0
Summary:        A Color Picker
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Visualization/Other
URL:            https://github.com/RonnyDo
Source:         https://github.com/RonnyDo/ColorPicker/archive/%{version}.tar.gz#/ColorPicker-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
A color picker program designed for Elementary OS.

%lang_package

%prep
%setup -q -n ColorPicker-%{version}

sed -i 's/\bmetainfo\b/appdata/' $(grep -rl 'metainfo')

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.ronnydo.colorpicker GTK Graphics Viewer
%find_lang com.github.ronnydo.colorpicker %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun

%files
%doc AUTHORS COPYING README.md
%{_bindir}/com.github.ronnydo.colorpicker
%dir %{_datadir}/appdata
%{_datadir}/appdata/com.github.ronnydo.colorpicker.appdata.xml
%{_datadir}/applications/com.github.ronnydo.colorpicker.desktop
%{_datadir}/glib-2.0/schemas/com.github.ronnydo.colorpicker.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.ronnydo.colorpicker.svg

%files lang -f %{name}.lang

%changelog
