#
# spec file for package appstream-glib
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           appstream-glib
Version:        0.8.2
Release:        0
Summary:        AppStream Abstraction Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://people.freedesktop.org/~hughsient/appstream-glib/
Source0:        %{name}-%{version}.tar.xz
Source1:        openSUSE-appstream-process

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcab >= 0.6
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
# We still need some part to build the man pages
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.31.5
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.45.8
BuildRequires:  pkgconfig(glib-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.1.2
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl) >= 7.56.0
BuildRequires:  pkgconfig(libgcab-1.0)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(yaml-0.1)
Requires:       gcab
# Required in order to be able to convert .svg icons
Requires:       gdk-pixbuf-loader-rsvg
Requires:       pngquant >= 2.8

%description
This library provides GObjects and helper methods to read and write
AppStream metadata. It also provides a DOM implementation to edit
nodes and convert to and from the standardized XML representation.

This library allows to:

* Read and write compressed AppStream XML files
* Add and search for applications in an application store
* Get screenshot image data and release announcements
* Easily retrieve the best application data for the current locale
* Efficiently interface with more heavy-weight parsers like expat

%package -n libappstream-glib8
Summary:        AppStream Abstraction Library
License:        LGPL-2.1-or-later

%description -n libappstream-glib8
This library provides GObjects and helper methods to read and write
AppStream metadata. It also provides a DOM implementation to edit
nodes and convert to and from the standardized XML representation.

%package -n typelib-1_0-AppStreamGlib-1_0
Summary:        Introspection bindings for the AppStream abstraction library
License:        LGPL-2.1-or-later

%description -n typelib-1_0-AppStreamGlib-1_0
This library provides GObjects and helper methods to read and write
AppStream metadata. It also provides a DOM implementation to edit
nodes and convert to and from the standardized XML representation.

%package devel
Summary:        Development files for the AppStream abstraction library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       %{name} = %{version}
Requires:       libappstream-glib8 = %{version}
Requires:       typelib-1_0-AppStreamGlib-1_0 = %{version}
# appdata-tools was consumed into appstream-glib and is no longer maintained upstream
Obsoletes:      appdata-tools < 0.1.9
Provides:       appdata-tools = 0.1.9
# Also obsolete the -lang package; or we end up with strange conflicts
Obsoletes:      appdata-tools-lang < 0.1.9

%description devel
This library provides GObjects and helper methods to read and write
AppStream metadata. It also provides a DOM implementation to edit
nodes and convert to and from the standardized XML representation.

This library allows to:

* Read and write compressed AppStream XML files
* Add and search for applications in an application store
* Get screenshot image data and release announcements
* Easily retrieve the best application data for the current locale
* Efficiently interface with more heavy-weight parsers like expat

%package -n openSUSE-appstream-process
Summary:        Appstream processor employed by kiwi
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       appstream-glib >= %{version}
Requires:       openSUSE-appdata-extra

%description -n openSUSE-appstream-process
A wrapper around appstream-builder, called by kiwi in order to produce AppStream metadata
for the repositories to be published

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Ddep11=true \
	-Dbuilder=true \
	-Drpm=true \
	-Dalpm=false \
	-Dfonts=false \
	-Dstemmer=false \
	-Dman=true \
	-Dgtk-doc=true \
	-Dintrospection=true \
	%{nil}
%meson_build

%install
%meson_install
# We don't care for 'installed tests'; that's used by GNOME Smoke Testing.
rm %{buildroot}%{_datadir}/installed-tests/appstream-glib/*.test

# install the appstream process script to be used by kiwi
install -d -m 0755 %{_buildroot}%{_bindir}
install -m 0755 -D %{SOURCE1} %{buildroot}%{_bindir}/$(basename %{SOURCE1})

%find_lang %{name}

%check
if %meson_test; then
  echo CHECKS passed
  exit 0
else
  echo CHECKS failed... dumping log file
  find -name testlog.txt -exec cat {} +
  exit 0
fi

%ldconfig_scriptlets -n libappstream-glib8

%files
%doc AUTHORS NEWS
%{_bindir}/appstream-builder
%{_bindir}/appstream-compose
%{_bindir}/appstream-util
%{_datadir}/bash-completion/completions/appstream-builder
%{_datadir}/bash-completion/completions/appstream-util
%{_libdir}/asb-plugins-5/
%{_mandir}/man1/appstream-builder.1%{?ext_man}
%{_mandir}/man1/appstream-compose.1%{?ext_man}
%{_mandir}/man1/appstream-util.1%{?ext_man}

%files -n libappstream-glib8
%license COPYING
%{_libdir}/libappstream-glib.so.*

%files -n typelib-1_0-AppStreamGlib-1_0
%{_libdir}/girepository-1.0/AppStreamGlib-1.0.typelib

%files devel
%doc MAINTAINERS README.md
%{_datadir}/aclocal/appdata-xml.m4
%{_datadir}/aclocal/appstream-xml.m4
%dir %{_datadir}/gettext/its
%{_datadir}/gettext/its/appdata.*
%{_datadir}/gir-1.0/AppStreamGlib-1.0.gir
%{_datadir}/gtk-doc/html/appstream-glib/
%{_includedir}/libappstream-glib/
%{_libdir}/pkgconfig/appstream-glib.pc
%{_libdir}/libappstream-glib.so

%files -n openSUSE-appstream-process
%{_bindir}/openSUSE-appstream-process

%files lang -f %{name}.lang

%changelog
