#
# spec file for package AppStream
#
# Copyright (c) 2023 SUSE LLC
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


%define libappstream_sover 4
%define libAppStreamQt_sover 2
%define libappstream_compose_sover 0
%if 0%{?sle_version} >= 150300 && 0%{?is_opensuse} || 0%{?suse_version} > 1500
%bcond_without vala
%endif
Name:           AppStream
Version:        0.16.1
Release:        0
Summary:        Tools and libraries to work with AppStream metadata
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.freedesktop.org/software/appstream/docs/
Source0:        http://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz
Source1:        http://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch0:         support-meson0.59.patch
BuildRequires:  cairo-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  itstool
BuildRequires:  meson >= 0.59
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.62
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(xmlb) >= 0.3.6
BuildRequires:  pkgconfig(yaml-0.1)
Recommends:     curl
%if %{with vala}
BuildRequires:  vala
%endif

%description
AppStream-Core makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%package -n libappstream%{libappstream_sover}
Summary:        The main library for AppStream
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n libappstream%{libappstream_sover}
The main library for AppStream.

%package -n libAppStreamQt%{libAppStreamQt_sover}
Summary:        Qt5 bindings for AppStream
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n libAppStreamQt%{libAppStreamQt_sover}
The Qt5 bindings for AppStream.

%package -n libAppStreamQt-devel
Summary:        Header files for AppStream's Qt5 bindings
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libAppStreamQt%{libAppStreamQt_sover} = %{version}
Requires:       libappstream%{libappstream_sover} = %{version}

%description -n libAppStreamQt-devel
This package contains all necessary include files, libraries,
configuration files and development tools (with manual pages) needed to
compile and link applications using the Qt bindings for AppStream.

%package compose
Summary:        Support for appstreamcli compose
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires:       gdk-pixbuf-loader-rsvg

%description compose
This package contains all necessary files, libraries,
configuration files to add compose support to appstreamcli.

%package -n libappstream-compose%{libappstream_compose_sover}
Summary:        Libraries for appstream compose support
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n libappstream-compose%{libappstream_compose_sover}
The library for AppStream compose support.

%package compose-devel
Summary:        Header files for AppStream Compose support
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       AppStream-compose = %{version}

%description compose-devel
This package contains all necessary files, libraries,
configuration files to add compose support using compose.

%package devel
Summary:        Header files for AppStream development
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libappstream%{libappstream_sover} = %{version}

%description devel
This package contains all necessary include files, libraries,
configuration files and development tools (with manual pages) needed to
compile and link applications using AppStream.

This package contains the documentation for AppStream.

%package doc
Summary:        Documentation for AppStream
License:        GPL-2.0-or-later
Group:          Documentation/HTML
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

%prep
%autosetup -p1

%build
%meson -Dqt=true \
       -Dcompose=true \
%if %{with vala}
       -Dvapi=true \
%else
       -Dvapi=false \
%endif
       -Ddocs=false \
       -Dapidocs=false \
       -Dstemming=false
%meson_build

%install
%meson_install

# Unneeded test file
rm -r %{buildroot}%{_datadir}/installed-tests

%check
%meson_test

%find_lang appstream %{name}.lang

%ldconfig_scriptlets -n libappstream%{libappstream_sover}
%ldconfig_scriptlets -n libAppStreamQt%{libAppStreamQt_sover}
%ldconfig_scriptlets -n libappstream-compose%{libappstream_compose_sover}

%files lang -f %{name}.lang

%files
%doc NEWS
%{_bindir}/appstreamcli
%config(noreplace) %{_sysconfdir}/appstream.conf
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.freedesktop.appstream.cli.metainfo.xml
%{_mandir}/man1/appstreamcli.*

%files -n libappstream%{libappstream_sover}
%license COPYING AUTHORS
%{_libdir}/libappstream.so.%{libappstream_sover}
%{_libdir}/libappstream.so.%{version}

%files -n libAppStreamQt%{libAppStreamQt_sover}
%{_libdir}/libAppStreamQt.so.%{libAppStreamQt_sover}
%{_libdir}/libAppStreamQt.so.%{version}

%files -n libAppStreamQt-devel
%{_includedir}/AppStreamQt/
%{_libdir}/cmake/AppStreamQt/
%{_libdir}/libAppStreamQt.so

%files compose
%{_datadir}/metainfo/org.freedesktop.appstream.compose.metainfo.xml
%{_libexecdir}/appstreamcli-compose

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
%{_datadir}/doc/appstream
%{_mandir}/man1/appstreamcli-compose*.1.gz
%endif

%files -n typelib-1_0-AppStream-1.0
%{_libdir}/girepository-1.0/AppStream-1.0.typelib

%files -n typelib-1_0-AppStream-compose-1.0
%{_libdir}/girepository-1.0/AppStreamCompose-1.0.typelib

%changelog
