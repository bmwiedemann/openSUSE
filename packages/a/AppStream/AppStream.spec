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
%if 0%{?sle_version} >= 150300 && 0%{?is_opensuse} || 0%{?suse_version} > 1500
%bcond_without vala
%endif
Name:           AppStream
Version:        0.15.6
Release:        0
Summary:        Tools and libraries to work with AppStream metadata
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.freedesktop.org/software/appstream/docs/
Source0:        http://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz
Source1:        http://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch0:         support-meson0.59.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  itstool
BuildRequires:  meson >= 0.59
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.62
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
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

%package doc
Summary:        Documentation for AppStream
License:        GPL-2.0-or-later
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
AppStream-Core makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

This package contains the documentation files for AppStream.

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

%post -n libAppStreamQt%{libAppStreamQt_sover} -p /sbin/ldconfig
%post -n libappstream%{libappstream_sover} -p /sbin/ldconfig
%postun -n libAppStreamQt%{libAppStreamQt_sover} -p /sbin/ldconfig
%postun -n libappstream%{libappstream_sover} -p /sbin/ldconfig

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

%files -n typelib-1_0-AppStream-1.0
%{_libdir}/girepository-1.0/AppStream-1.0.typelib

%files doc
%{_datadir}/doc/appstream

%changelog
