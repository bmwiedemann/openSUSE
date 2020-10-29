#
# spec file for package geany
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


Name:           geany
Version:        1.37
Release:        0
Summary:        GTK-based integrated development environment
License:        GPL-2.0-or-later
Group:          Development/Tools/IDE
URL:            https://geany.org
Source0:        https://download.geany.org/%{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM geany-appstream.patch gh#geany/geany#1142 badshah400@gmail.com -- Downstream created appstream file, submitted upstream
Patch0:         geany-appstream.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docutils
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
%lang_package

%description
Geany is a text editor using the GTK+ toolkit with basic features of
an integrated development environment. It can do syntax highlighting
for many formats, case folding, symbol name autocompletion, autoclose
XML/HTML tags, provides code navigation and has a plugin interface.

%package devel
Summary:        Development files for the Geany IDE
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gtk3-devel

%description devel
Geany is a text editor using the GTK+ toolkit with basic features of
an integrated development environment.

%package -n libgeany0
Summary:        Geany libraries
Group:          System/Libraries

%description -n libgeany0
Geany's core library

%package doc
Summary:        Geany documentation
Group:          Documentation/Other
Requires:       %{name} >= %{version}

%description doc
Geany's developers documentation

%prep
%setup -q
%patch0 -p1

%build
autoreconf -i
%configure \
	--enable-gtk3 \
	--docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
# FIXME: add lb to filesystem?
rm %{buildroot}%{_datadir}/locale/lb/LC_MESSAGES/*
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{name}
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post
%icon_theme_cache_post Tango

%postun
%desktop_database_postun
%icon_theme_cache_postun
%icon_theme_cache_postun Tango

%post   -n libgeany0 -p /sbin/ldconfig
%postun -n libgeany0 -p /sbin/ldconfig

%files
%{_mandir}/man1/geany.1%{ext_man}
%{_bindir}/geany
%{_datadir}/applications/geany.desktop
%{_datadir}/geany/
%{_datadir}/icons/hicolor/
%{_datadir}/icons/Tango/
%dir %{_libdir}/geany
%{_libdir}/geany/*.so
%dir %{_datadir}/appdata
%{_datadir}/appdata/geany.appdata.xml

%files -n libgeany0
%{_libdir}/libgeany.so.*

%files doc
# AUTHORS, COPYING, README, etc. are installed during make install
%doc %{_defaultdocdir}/geany/

%files devel
%{_includedir}/geany/
%{_libdir}/pkgconfig/geany.pc
%{_libdir}/libgeany.so

%files lang -f %{name}.lang

%changelog
