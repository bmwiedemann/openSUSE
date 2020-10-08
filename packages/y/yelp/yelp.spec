#
# spec file for package yelp
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


Name:           yelp
Version:        3.36.1
Release:        0
Summary:        Help Browser for the GNOME Desktop
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Yelp
Source0:        https://download.gnome.org/sources/yelp/3.36/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE yelp-lang-bundle.patch bnc#689979 vuntz@opensuse.org -- Support help documents shipped in bundles
Patch1:         yelp-lang-bundle.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  itstool >= 1.2.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.13.3
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxslt) >= 1.1.4
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.19.2
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.0) >= 2.19.2
BuildRequires:  pkgconfig(yelp-xsl) >= 3.31.90
# data/dtd/catalog references dtds from oasis-open.org, which we provide on docbook_4 package (bnc#770067)
Requires:       docbook_4
# We need the stylesheets from yelp-xsl
Requires:       yelp-xsl
Provides:       suse_help_viewer

%description
Yelp is the help viewer in GNOME (it's what happens when you press F1). With
gnome-doc-utils, Yelp serves as a DocBook viewer, a man page viewer and an
info page viewer.

%package -n libyelp0
Summary:        Core library for the GNOME Desktop help browser
Group:          System/Libraries

%description  -n libyelp0
Yelp is the help viewer in GNOME (it's what happens when you press F1). With
gnome-doc-utils, Yelp serves as a DocBook viewer, a man page viewer and an
info page viewer.

This package provides Yelp's system shared libraries.

%package devel
Summary:        Development files for libyelp
Group:          Development/Libraries/GNOME
Requires:       libyelp0 = %{version}

%description devel
Yelp is the help viewer in GNOME (it's what happens when you press F1). With
gnome-doc-utils, Yelp serves as a DocBook viewer, a man page viewer and an
info page viewer.

This package provides Yelp's development files.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch1 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%post -n libyelp0 -p /sbin/ldconfig
%postun -n libyelp0 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/gnome-help
%{_bindir}/yelp
%{_datadir}/applications/yelp.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.yelp.gschema.xml
%{_datadir}/metainfo/yelp.appdata.xml
%{_datadir}/yelp/
%{_datadir}/yelp-xsl/xslt/common/domains/yelp.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Yelp.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Yelp-symbolic.svg

%files -n libyelp0
%{_libdir}/libyelp.so.0*
%dir %{_libdir}/yelp/
%dir %{_libdir}/yelp/web-extensions/
%{_libdir}/yelp/web-extensions/libyelpwebextension.so

%files devel
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/libyelp/
%{_includedir}/libyelp/
%{_libdir}/libyelp.so

%files lang -f %{name}.lang

%changelog
