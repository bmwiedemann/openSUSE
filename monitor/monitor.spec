#
# spec file for package monitor
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           monitor
Version:        0.3.7
Release:        0
Summary:        Simple Task Manager
License:        GPL-3.0
Group:          System/GUI/Other
URL:            https://github.com/stsdc/monitor
Source:         https://github.com/stsdc/monitor/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  elementary-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.40.6
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
Manage processes and monitor system resources for elementary OS.

%lang_package

%prep
%setup -q

sed -i 's/\bmetainfo\b/appdata/' $(grep -rwl 'metainfo')

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.stsdc.monitor GTK System Monitor
%find_lang com.github.stsdc.monitor %{name}.lang
%fdupes %{buildroot}/%{_datadir}

# dirlist HiDPI icons (see: hicolor/index.theme)
_dirlist=$PWD/dir.lst
pushd %{buildroot}
find ./ | while read _list; do
    echo $_list | grep '[0-9]\@[0-9]' || continue
    _path=$(echo $_list | sed 's/[^/]//')
    if ! ls ${_path%/*}; then
        grep -xqs "\%dir\ ${_path%/*}" $_dirlist || echo "%dir ${_path%/*}" >> $_dirlist
    fi
done
popd

%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun

%files -f dir.lst
%doc AUTHORS LICENSE README.md
%{_bindir}/com.github.stsdc.monitor
%{_datadir}/appdata/com.github.stsdc.monitor.appdata.xml
%{_datadir}/applications/com.github.stsdc.monitor.desktop
%{_datadir}/glib-2.0/schemas/com.github.stsdc.monitor.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.stsdc.monitor.??g

%files lang -f %{name}.lang

%changelog
