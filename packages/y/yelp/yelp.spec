#
# spec file for package yelp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           yelp
Version:        49.0
Release:        0
Summary:        Help Browser for the GNOME Desktop
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Yelp
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  AppStream
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  itstool >= 1.2.0
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.67.4
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(gtk4) >= 4.16.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6.0
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.5
BuildRequires:  pkgconfig(libxslt) >= 1.1.4
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(webkitgtk-web-process-extension-6.0)
BuildRequires:  pkgconfig(yelp-xsl) >= 42.3
# data/dtd/catalog references dtds from oasis-open.org, which we provide on docbook_4 package (bnc#770067)
Requires:       docbook_4
# We need the stylesheets from yelp-xsl
Requires:       yelp-xsl
Provides:       suse_help_viewer

%description
Yelp is the help viewer in GNOME (it's what happens when you press F1). With
gnome-doc-utils, Yelp serves as a DocBook viewer, a man page viewer and an
info page viewer.

%package -n libyelp-1-0
Summary:        Core library for the GNOME Desktop help browser
Group:          System/Libraries

%description  -n libyelp-1-0
Yelp is the help viewer in GNOME (it's what happens when you press F1). With
gnome-doc-utils, Yelp serves as a DocBook viewer, a man page viewer and an
info page viewer.

This package provides Yelp's system shared libraries.

%package devel
Summary:        Development files for libyelp
Group:          Development/Libraries/GNOME
Requires:       libyelp-1-0 = %{version}
Requires:       yelp = %{version}

%description devel
Yelp is the help viewer in GNOME (it's what happens when you press F1). With
gnome-doc-utils, Yelp serves as a DocBook viewer, a man page viewer and an
info page viewer.

This package provides Yelp's development files.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%ldconfig_scriptlets -n libyelp-1-0

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/gnome-help
%{_bindir}/yelp
%{_datadir}/applications/org.gnome.Yelp.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.yelp.gschema.xml
%{_datadir}/metainfo/org.gnome.Yelp.metainfo.xml
%{_datadir}/yelp/
%{_datadir}/yelp-xsl/xslt/common/domains/yelp.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Yelp.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Yelp-symbolic.svg
%dir %{_libdir}/yelp-1/
%dir %{_libdir}/yelp-1/web-process-extensions/
%{_libdir}/yelp-1/web-process-extensions/libyelpwebprocessextension.so

%files -n libyelp-1-0
%{_libdir}/libyelp-1.so.0*

%files devel
%doc ChangeLog
%{_includedir}/libyelp-1/
%{_libdir}/libyelp-1.so
%{_libdir}/pkgconfig/libyelp-1.pc

%files lang -f %{name}.lang

%changelog
