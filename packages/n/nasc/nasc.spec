#
# spec file for package nasc
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           nasc
Version:        0.5.4
Release:        0
Summary:        Do maths like a normal person
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            http://parnold-x.github.io/nasc/
Source:         https://github.com/parnold-x/nasc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(cln)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(libsoup-2.4)
Requires:       qalculate
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libcln.so) --qf '%%{NAME} >= %%{VERSION}')
%glib2_gsettings_schema_requires

%description
This is an application where you do calculations "like a normal
person". It lets you type whatever you want, smartly figures out what
computations are needed, and outputs an answer on the right pane.
Then you can plug those answers in to future equations and if that
answer changes, so does the equations it is used in.

%prep
%setup -q

%build
%cmake \
    -DGSETTINGS_COMPILE=FALSE \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined"

make %{?_smp_mflags}

%install
%cmake_install %{?_smp_mflags}

%post
%if 0%{?suse_version} < 1500
%glib2_gsettings_schema_post
%icon_theme_cache_post
%desktop_database_post

%postun
%glib2_gsettings_schema_postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/metainfo
%{_bindir}/com.github.parnold-x.nasc
%{_datadir}/applications/com.github.parnold-x.nasc.desktop
%{_datadir}/glib-2.0/schemas/com.github.parnold-x.nasc.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.parnold-x.nasc.??g
%{_datadir}/metainfo/com.github.parnold-x.nasc.appdata.xml
%{_datadir}/qalculate/

%changelog
