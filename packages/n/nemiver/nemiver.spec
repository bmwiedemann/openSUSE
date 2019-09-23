#
# spec file for package nemiver
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


%define scm_bootstrap 0
Name:           nemiver
Version:        0.9.6
Release:        0
Summary:        Nemiver graphical debugger
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            http://home.gna.org/nemiver/
Source0:        http://download.gnome.org/sources/nemiver/0.9/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM nemiver-build-fix.patch bgo#763840 zaitor@opensuse.org -- Fix build with new mm stack
Patch0:         nemiver-build-fix.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  intltool
BuildRequires:  libgtop-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gdlmm-3.0) >= 3.0
BuildRequires:  pkgconfig(giomm-2.4) >= 2.15.2
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtkhex-3) >= 2.90
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.0
BuildRequires:  pkgconfig(gtksourceviewmm-3.0) >= 3.0
BuildRequires:  pkgconfig(vte-2.91) >= 0.28
Requires:       gdb
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires
%if 0%{?scm_bootstrap}
BuildRequires:  gnome-common
%endif
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
Nemiver is a standalone graphical debugger that integrates well in the
GNOME desktop environment. It currently features a backend which uses
the well known GNU Debugger gdb to debug C / C++ programs.

%package devel
Summary:        Nemiver graphical debugger - Development files
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}

%description devel
Nemiver is a standalone graphical debugger that integrates well in the
GNOME desktop environment. It currently features a backend which uses
the well known GNU Debugger gdb to debug C / C++ programs.

This package contains the development files to build debugger backend.

%lang_package

%prep
%setup -q
%patch0 -p1
# Disabled from ver 0.9.6, it breaks the build.
#translation-update-upstream

%build
%if 0%{?scm_bootstrap}
NOCONFIGURE=1 gnome-autogen.sh
%endif
%configure --disable-static --with-pic\
        --enable-gsettings
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file nemiver
%find_lang %{name} %{?no_lang_C}
# remove la files
find %{buildroot} -type f -name "*.la" -delete -print
# create symlinks for man pages
%fdupes -s %{buildroot}/%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}

%if 0%{?suse_version} > 1130
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post
%endif

%if 0%{?suse_version} > 1130
%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%doc AUTHORS README NEWS TODO
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/*
%{_libdir}/nemiver/
%{_datadir}/nemiver/
%dir %{_datadir}/appdata
%{_datadir}/appdata/nemiver.appdata.xml
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/org.nemiver.gschema.xml
# Own dirs for oS 13.2
%dir %{_datadir}/icons/hicolor/symbolic/
%dir %{_datadir}/icons/hicolor/symbolic/apps
%{_datadir}/icons/hicolor/*/apps/nemiver*.*
%{_mandir}/man1/nemiver.1%{ext_man}

%files devel
%doc AUTHORS README NEWS TODO
%{_includedir}/nemiver/

%files lang -f %{name}.lang

%changelog
