#
# spec file for package shutdownscheduler
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           shutdownscheduler
Version:        1.5.1
Release:        0
Summary:        Simple Shutdown Scheduler
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/bcedu
Source:         https://github.com/bcedu/ShutdownScheduler/archive/v%{version}.tar.gz#/ShutdownScheduler-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(unity)
Recommends:     %{name}-lang

%description
ShutdownSheduler is an extremely simple program used to shutdown the computer 
in a specific date time.

%lang_package

%prep
%setup -q -n ShutdownScheduler-%{version}

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.bcedu.shutdownscheduler GTK Utility X-SuSE-DesktopUtility
%find_lang com.github.bcedu.shutdownscheduler %{name}.lang
%fdupes %{buildroot}%{_datadir}

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
%license COPYING
%doc AUTHORS README.md
%{_bindir}/com.github.bcedu.shutdownscheduler
%{_datadir}/applications/com.github.bcedu.shutdownscheduler.desktop
%{_datadir}/glib-2.0/schemas/com.github.bcedu.shutdownscheduler.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.bcedu.shutdownscheduler.??g
%{_datadir}/metainfo/com.github.bcedu.shutdownscheduler.appdata.xml

%files lang -f %{name}.lang

%changelog
