#
# spec file for package agenda
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


Name:           agenda
Version:        1.0.12
Release:        0
Summary:        Task Manager for Elementary
License:        GPL-3.0-or-later
Group:          Productivity/Office/Organizers
URL:            https://github.com/dahenson/agenda
Source:         https://github.com/dahenson/agenda/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-build.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(granite) >= 0.5
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
%patch0 -p1

%build
%cmake -DGSETTINGS_COMPILE=OFF
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file -r com.github.dahenson.agenda GTK Office ProjectManagement
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc README.md
%{_bindir}/com.github.dahenson.agenda
%{_datadir}/applications/com.github.dahenson.agenda.desktop
%{_datadir}/glib-2.0/schemas/com.github.dahenson.agenda.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.dahenson.agenda.??g
%{_datadir}/metainfo/com.github.dahenson.agenda.appdata.xml

%files lang -f agenda.lang

%changelog
