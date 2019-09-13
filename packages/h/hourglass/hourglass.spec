#
# spec file for package hourglass
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


Name:           hourglass
Version:        1.1.1
Release:        0
Summary:        Clock gadget for Elementary OS
License:        GPL-3.0
Group:          System/X11/Utilities
URL:            https://github.com/sgpthomas
Source:         https://github.com/sgpthomas/hourglass/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.28
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
A clock application that is designed to fit perfectly into
Elementary's design scheme.

%lang_package

%prep
%setup -q

sed -i 's/\bmetainfo\b/appdata/' $(grep -rwl 'metainfo')

%build
%cmake \
      -DGSETTINGS_COMPILE=OFF
make %{?_smp_mflags}

%install
%cmake_install %{?_smp_mflags}
%suse_update_desktop_file -r com.github.sgpthomas.hourglass GTK Utility Clock
%fdupes %{buildroot}%{_datadir}
%find_lang %{name}

%post
%glib2_gsettings_schema_post
%icon_theme_cache_post
%desktop_database_post

%postun
%glib2_gsettings_schema_postun
%icon_theme_cache_postun
%desktop_database_postun

%files
%doc AUTHORS COPYING README.md
%{_bindir}/com.github.sgpthomas.hourglass
%{_bindir}/com.github.sgpthomas.hourglass-daemon
%dir %{_datadir}/appdata
%{_datadir}/appdata/com.github.sgpthomas.hourglass.appdata.xml
%{_datadir}/applications/com.github.sgpthomas.hourglass.desktop
%{_datadir}/glib-2.0/schemas/com.github.sgpthomas.hourglass.gschema.xml
%{_datadir}/hourglass/
%{_datadir}/icons/hicolor/*/apps/hourglass.??g
%{_datadir}/pixmaps/hourglass.svg
%{_sysconfdir}/xdg/autostart/com.github.sgpthomas.hourglass-daemon.desktop

%files lang -f %{name}.lang

%changelog
