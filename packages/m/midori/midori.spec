#
# spec file for package midori
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


%define major   0
Name:           midori
Version:        v9.0
Release:        0
Summary:        Lightweight Web Browser
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            http://midori-browser.org/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  vala
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Recommends:     %{name}-lang
Recommends:     xdg-utils
Provides:       browser(npapi)
Obsoletes:      %{name}-branding-openSUSE

%description
Midori is a lightweight web browser based on WebKit and GTK+. Its major
features are:

* Tabs, windows and session management.
* Flexibly configurable Web Search.
* User scripts and user styles support.
* Straightforward bookmark management.
* Customizable and extensible interface.
* Extensions written in C and Vala.

%package -n libmidori-core%{major}
Summary:        Midori Library
Group:          System/Libraries
Obsoletes:      libmidori-core1

%description -n libmidori-core%{major}
Midori shared library.

%package devel
Summary:        Development Files for Midori
Group:          Development/Libraries/C and C++
Requires:       libmidori-core%{major} = %{version}
Requires:       typelib-1_0-Midori-0_6
Requires:       pkgconfig(gobject-introspection-1.0)
Recommends:     pkgconfig(vapigen)

%description devel
This package contains development files needed to develop extensions for
Midori.

%package -n typelib-1_0-Midori-0_6
Summary:        Midori Browser -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Midori-0_6
Midori is a lightweight web browser based on WebKit and GTK+.

This package provides the GObject Introspection bindings for Midori.

%lang_package

%prep
%autosetup

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr ..
%make_build

%install
cd build
%make_install
cd ..
%find_lang %{name} %{?no_lang_C}

# remove redundant doc directory and files
rm -rf %{buildroot}%{_datadir}/doc/midori/

%fdupes -s %{buildroot}%{_datadir}/

%post -n libmidori-core%{major}  -p /sbin/ldconfig
%postun -n libmidori-core%{major} -p /sbin/ldconfig
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc CHANGELOG.md README.md
%license COPYING
%dir %{_libdir}/%{name}
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_libdir}/%{name}/*.plugin
%{_libdir}/%{name}/*.so
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/*.xml

%files -n libmidori-core%{major}
%{_libdir}/libmidori-core.so.0
%{_libdir}/libmidori-core.so.0.6

%files devel
%{_datadir}/gir-1.0/Midori-0.6.gir
%{_libdir}/libmidori-core.so

%files -n typelib-1_0-Midori-0_6
%{_libdir}/girepository-1.0/Midori-0.6.typelib

%files lang -f %{name}.lang

%changelog
