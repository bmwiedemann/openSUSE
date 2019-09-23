#
# spec file for package tasque
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


%define dbus_min_version 0.60-26
%if 0%{?suse_version}
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
%else
%define suse_update_desktop_file true
%endif
Name:           tasque
Version:        0.1.12
Release:        0
Summary:        A simple task management app (TODO list) for the Linux Desktop
License:        LGPL-2.1-or-later AND MIT
Group:          Productivity/Office/Organizers
URL:            http://live.gnome.org/Tasque
Source:         http://download.gnome.org/sources/tasque/0.1/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  notify-sharp
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-sharp-1.0)
BuildRequires:  pkgconfig(dbus-sharp-glib-1.0)
Requires:       dbus-1-glib >= %{dbus_min_version}
Requires:       dbus-1-x11 >= %{dbus_min_version}
Requires:       mono-data-sqlite
Recommends:     %{name}-lang
Provides:       tasky = %{version}
Obsoletes:      tasky < %{version}

%description
Tasky is a simple task management app (TODO list) for the Linux
Desktop.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure \
    --enable-standard-backends
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}

%if 0%{?suse_version} > 1130
%post
%desktop_database_post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} > 1130
%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%{_bindir}/%{name}
%{_prefix}/lib/pkgconfig/tasque.pc
%{_prefix}/lib/tasque/
%{_datadir}/applications/tasque.desktop
%{_datadir}/dbus-1/services/org.gnome.Tasque.service
%{_datadir}/icons/hicolor/*/apps/tasque*.*
%{_datadir}/pixmaps/tasque-*.png
%{_datadir}/tasque/

%files lang -f %{name}.lang

%changelog
