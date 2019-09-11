#
# spec file for package libtranslate
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Name:           libtranslate
Version:        0.99
Release:        0
Summary:        Library for translating text
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.nongnu.org/libtranslate/

Source:         %{name}-%{version}.tar.gz

#official patches
#patch fixing HTTP charset parsing
Patch0:         %{name}-%{version}-charsetparse.diff
#patch fixing occasional translate_session_translate_text() lockup
Patch1:         %{name}-%{version}-condfix.diff
#patch fixing memory exhaustion on 64-bit platforms
Patch2:         %{name}-%{version}-int64.diff

#unofficial patches, contributed by Dmitry Butskoy (taken from official site)
#patch allowing to omit the post-marker element
Patch3:         %{name}-%{version}-postmarker.diff
#patch updating services.xml
Patch4:         %{name}-%{version}-services.diff

#unofficial patches, contributed by Dan Winship (taken from official site)
#patch adding support for libsoup >= 2.4
Patch5:         %{name}-%{version}-libsoup24.diff

Patch6:         libtranslate-m4.diff

BuildRequires:  autoconf >= 2.52
BuildRequires:  automake
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libsoup-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.4.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.4.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.4.0
BuildRequires:  pkgconfig(libxml-2.0)
%if 0%{?suse_version} <= 1140
BuildRequires:  libxslt
%endif

%description
libtranslate is a library for translating text and web pages
between natural languages. Its modular infrastructure allows
to implement new translation services separately from the core
library.

%package -n libtranslate0
Summary:        Library for translating text
Group:          Development/Libraries/C and C++

%description -n libtranslate0
libtranslate is a library for translating text and web pages
between natural languages. Its modular infrastructure allows
to implement new translation services separately from the core
library.

%package devel
Summary:        Header files for libtranslate
Group:          Development/Libraries/C and C++
Requires:       libtranslate0 = %{version}
Requires:       pkgconfig(glib-2.0)

%description devel
This package contain header files for libtranslate.

%package progs
Summary:        Library for translating text
Group:          Productivity/Office/Dictionary

%description progs
libtranslate is a library for translating text and web pages
between natural languages. Its modular infrastructure allows
to implement new translation services separately from the core
library.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch -P 6 -p1

%build
autoreconf -fi
intltoolize -f
%configure --disable-static --enable-generic --disable-talkfilters
make %{?_smp_mflags}

%install
%make_install

%find_lang libtranslate

%post -n %{name}0 -p /sbin/ldconfig
%postun -n %{name}0 -p /sbin/ldconfig

%files -n libtranslate0
%defattr (-,root,root,-)
%doc COPYING README
%{_libdir}/*.so.*
%{_libdir}/libtranslate
%{_datadir}/libtranslate

%files progs -f libtranslate.lang
%defattr (-,root,root,-)
%{_bindir}/translate
%{_mandir}/*/*

%files devel
%defattr (-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
