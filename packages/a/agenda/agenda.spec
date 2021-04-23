#
# spec file for package agenda
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


Name:           agenda
Version:        1.1.0
Release:        0
Summary:        Task Manager for Elementary
License:        GPL-3.0-or-later
Group:          Productivity/Office/Organizers
URL:            https://github.com/dahenson/agenda
Source:         https://github.com/dahenson/agenda/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(vapigen) >= 0.26.0
Recommends:     %{name}-lang
Provides:       agenda-tasks = %{version}
Obsoletes:      agenda-tasks < %{version}

%description
A task manager for Elementary OS.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.dahenson.agenda GTK Office ProjectManagement
%find_lang com.github.dahenson.agenda %{name}.lang
%fdupes %{buildroot}/%{_datadir}

# dirlist HiDPI icons (see: hicolor/index.theme)
touch $PWD/dir.lst
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

%files -f dir.lst
%license LICENSE
%doc README.md
%{_bindir}/com.github.dahenson.agenda
%{_datadir}/applications/com.github.dahenson.agenda.desktop
%{_datadir}/glib-2.0/schemas/com.github.dahenson.agenda.gschema.xml
%{_datadir}/icons/hicolor/*/*/com.github.dahenson.agenda.??g
%{_datadir}/metainfo/com.github.dahenson.agenda.appdata.xml

%files lang -f agenda.lang

%changelog
