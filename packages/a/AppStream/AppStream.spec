#
# spec file for package AppStream
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == "qt6"
%define pkg_suffix -qt6
%define qt6 1
%define min_qt_version 6.2.4
%else
%define min_qt_version 5.15
%if 0%{?sle_version} >= 150400 && 0%{?is_opensuse} || 0%{?sle_version} >= 150600 || 0%{?suse_version} > 1500
%bcond_without vala
%endif
%endif
# The default Leap compiler is too old for building AppStream-qt6. use the same compiler for both flavors
%if 0%{?suse_version} == 1500
%bcond_without gcc13
%endif
%define rname AppStream
%define libappstream_sover 5
%define libAppStreamQt_sover 3
%define libappstream_compose_sover 0
Name:           AppStream%{?pkg_suffix}
Version:        1.0.4
Release:        0
Summary:        Tools and libraries to work with AppStream metadata
License:        LGPL-2.1-or-later
URL:            https://www.freedesktop.org/software/appstream/docs/
Source0:        https://www.freedesktop.org/software/appstream/releases/%{rname}-%{version}.tar.xz
Source1:        https://www.freedesktop.org/software/appstream/releases/%{rname}-%{version}.tar.xz.asc
Source2:        AppStream.keyring
# PATCH-FIX-OPENSUSE
Patch0:         support-meson0.59.patch
BuildRequires:  cairo-devel
BuildRequires:  docbook-xsl-stylesheets
%if %{with gcc13}
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%endif
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  gettext-devel
BuildRequires:  gperf
BuildRequires:  itstool
BuildRequires:  meson >= 0.59
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
%if 0%{?qt6}
BuildRequires:  pkgconfig(Qt6Core) >= %{min_qt_version}
BuildRequires:  pkgconfig(Qt6Test) >= %{min_qt_version}
%else
BuildRequires:  pkgconfig(Qt5Core) >= %{min_qt_version}
BuildRequires:  pkgconfig(Qt5Test) >= %{min_qt_version}
%endif
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.62
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(xmlb) >= 0.3.14
BuildRequires:  pkgconfig(yaml-0.1)
Recommends:     curl
%if %{with vala}
BuildRequires:  vala
%endif

%description
AppStream-Core makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%if 0%{?qt6}
%package -n libAppStreamQt%{libAppStreamQt_sover}
Summary:        Qt 6 bindings for AppStream
License:        GPL-2.0-or-later AND LGPL-2.1-or-later

%description -n libAppStreamQt%{libAppStreamQt_sover}
The Qt 6 bindings for AppStream.

%package -n appstream-qt6-devel
Summary:        Header files for AppStream's Qt 6 bindings
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       libAppStreamQt%{libAppStreamQt_sover} = %{version}
Requires:       libappstream%{libappstream_sover} = %{version}
Conflicts:      libAppStreamQt-devel < 1.0

%description -n appstream-qt6-devel
This package contains all necessary include files, libraries,
configuration files and development tools (with manual pages) needed to
compile and link applications using the Qt bindings for AppStream.
%else

%package -n libappstream%{libappstream_sover}
Summary:        The main library for AppStream
License:        GPL-2.0-or-later AND LGPL-2.1-or-later

%description -n libappstream%{libappstream_sover}
The main library for AppStream.

%package -n libAppStreamQt5-%{libAppStreamQt_sover}
Summary:        Qt 5 bindings for AppStream
License:        GPL-2.0-or-later AND LGPL-2.1-or-later

%description -n libAppStreamQt5-%{libAppStreamQt_sover}
The Qt 5 bindings for AppStream.

%package -n appstream-qt5-devel
Summary:        Header files for AppStream's Qt 5 bindings
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       libAppStreamQt5-%{libAppStreamQt_sover} = %{version}
Requires:       libappstream%{libappstream_sover} = %{version}
# Renamed after the 1.0.0 release
Provides:       libAppStreamQt-devel = %{version}
Obsoletes:      libAppStreamQt-devel < %{version}

%description -n appstream-qt5-devel
This package contains all necessary include files, libraries,
configuration files and development tools (with manual pages) needed to
compile and link applications using the Qt bindings for AppStream.

%package compose
Summary:        Support for appstreamcli compose
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       AppStream = %{version}
Requires:       gdk-pixbuf-loader-rsvg

%description compose
This package contains all necessary files, libraries,
configuration files to add compose support to appstreamcli.

%package -n libappstream-compose%{libappstream_compose_sover}
Summary:        Libraries for appstream compose support
License:        GPL-2.0-or-later AND LGPL-2.1-or-later

%description -n libappstream-compose%{libappstream_compose_sover}
The library for AppStream compose support.

%package compose-devel
Summary:        Header files for AppStream Compose support
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       AppStream = %{version}
Requires:       AppStream-compose = %{version}
Requires:       libappstream-compose%{libappstream_compose_sover} = %{version}

%description compose-devel
This package contains all necessary files, libraries,
configuration files to add compose support using compose.

%package devel
Summary:        Header files for AppStream development
License:        GPL-2.0-or-later
Requires:       AppStream = %{version}
Requires:       libappstream%{libappstream_sover} = %{version}

%description devel
This package contains all necessary include files, libraries,
configuration files and development tools (with manual pages) needed to
compile and link applications using AppStream.

This package contains the documentation for AppStream.

%package doc
Summary:        Documentation for AppStream
License:        GPL-2.0-or-later
BuildArch:      noarch

%description doc
AppStream-Core makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

This package contains the documentation files for AppStream.

%package -n typelib-1_0-AppStream-compose-1.0
Summary:        Introspection bindings for  AppStream Compose
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-AppStream-compose-1.0
GObject introspection bindings for interfaces provided by AppStream Compose

%package -n typelib-1_0-AppStream-1.0
Summary:        Introspection bindings for AppStream
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-AppStream-1.0
GObject introspection bindings for interfaces provided by AppStream.

%lang_package
%endif

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%define common_options -Ddocs=false -Dapidocs=false -Dstemming=false
%if %{with vala}
%define build_vapi true
%else
%define build_vapi false
%endif

%if 0%{?qt6}
%define options -Dqt=true -Dqt-versions=6 -Dvapi=false -Dcompose=false -Dgir=false
%else
%define options -Dqt=true -Dqt-versions=5 -Dcompose=true -Dvapi=%{build_vapi}
%endif

%if %{with gcc13}
export CC=gcc-13 CXX=g++-13
%endif

%meson %{common_options} %{options}

%meson_build

%install
%meson_install

# Unneeded test file
rm -r %{buildroot}%{_datadir}/installed-tests

# Only keep the Qt6 library when using the qt6 flavor
%if 0%{?qt6}
rm %{buildroot}%{_bindir}/appstreamcli
rm %{buildroot}%{_libdir}/libappstream.so*
rm -r %{buildroot}%{_datadir}/{appstream,doc,gettext,locale,man,metainfo}
rm -r %{buildroot}%{_includedir}/appstream
rm -r %{buildroot}%{_libdir}/pkgconfig
%else
%find_lang appstream %{name}.lang
%endif

%check
%meson_test

%if 0%{?qt6}
%ldconfig_scriptlets -n libAppStreamQt%{libAppStreamQt_sover}
%else
%ldconfig_scriptlets -n libappstream%{libappstream_sover}
%ldconfig_scriptlets -n libAppStreamQt5-%{libAppStreamQt_sover}
%ldconfig_scriptlets -n libappstream-compose%{libappstream_compose_sover}
%endif

%if 0%{?qt6}
%files -n libAppStreamQt%{libAppStreamQt_sover}
%{_libdir}/libAppStreamQt.so.%{libAppStreamQt_sover}
%{_libdir}/libAppStreamQt.so.%{version}

%files -n appstream-qt6-devel
%{_includedir}/AppStreamQt/
%{_libdir}/cmake/AppStreamQt/
%{_libdir}/libAppStreamQt.so

%else

%files lang -f %{name}.lang

%files
%doc NEWS
%{_bindir}/appstreamcli
%dir %{_datadir}/appstream
%{_datadir}/appstream/appstream.conf
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.freedesktop.appstream.cli.metainfo.xml
%{_mandir}/man1/appstreamcli.*

%files -n libappstream%{libappstream_sover}
%license COPYING AUTHORS
%{_libdir}/libappstream.so.%{libappstream_sover}
%{_libdir}/libappstream.so.%{version}

%files -n libAppStreamQt5-%{libAppStreamQt_sover}
%{_libdir}/libAppStreamQt5.so.%{libAppStreamQt_sover}
%{_libdir}/libAppStreamQt5.so.%{version}

%files -n appstream-qt5-devel
%{_includedir}/AppStreamQt5/
%{_libdir}/cmake/AppStreamQt5/
%{_libdir}/libAppStreamQt5.so

%files compose
%{_datadir}/metainfo/org.freedesktop.appstream.compose.metainfo.xml
%{_libexecdir}/appstreamcli-compose
%{_mandir}/man1/appstreamcli-compose*.1.gz

%files -n libappstream-compose%{libappstream_compose_sover}
%{_libdir}/libappstream-compose.so.%{version}
%{_libdir}/libappstream-compose.so.%{libappstream_compose_sover}

%files compose-devel
%{_libdir}/libappstream-compose.so
%{_libdir}/pkgconfig/appstream-compose.pc
%{_includedir}/appstream-compose/
%{_datadir}/gir-1.0/AppStreamCompose-1.0.gir

%files devel
%{_libdir}/libappstream.so
%{_libdir}/pkgconfig/appstream.pc
%{_includedir}/appstream/
%{_datadir}/gir-1.0/AppStream-1.0.gir
%{_datadir}/gettext/
%if %{with vala}
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/appstream.deps
%{_datadir}/vala/vapi/appstream.vapi
%endif

%files doc
%{_datadir}/doc/appstream

%files -n typelib-1_0-AppStream-1.0
%{_libdir}/girepository-1.0/AppStream-1.0.typelib

%files -n typelib-1_0-AppStream-compose-1.0
%{_libdir}/girepository-1.0/AppStreamCompose-1.0.typelib
%endif

%changelog
