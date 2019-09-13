#
# spec file for package liblangtag
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


%define libname liblangtag1
Name:           liblangtag
Version:        0.6.2
Release:        0
Summary:        An interface library to access tags for identifying languages
License:        LGPL-3.0-or-later OR MPL-2.0
Group:          Productivity/Publishing/Word
URL:            https://bitbucket.org/tagoh/liblangtag
Source0:        https://bitbucket.org/tagoh/%{name}/downloads/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libxml-2.0)

%description
%{name} is an interface library to access tags for identifying
languages.

Features:
* several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
* handling of the language tags
  - parser
  - matching
  - canonicalizing

%package -n %{libname}
Summary:        C++ library for identification of the language from tags
Group:          System/Libraries

%description -n %{libname}
%{name} is an interface library to access tags for identifying
languages.

Features:
* several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
* handling of the language tags
  - parser
  - matching
  - canonicalizing

%package devel
Summary:        Files for Developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig(glib-2.0)

%description devel
%{name} is an interface library to access tags for identifying
languages.

This package contains the %{name} development files.

%package doc
Summary:        Documentation of %{name} API
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-test \
	--disable-introspection \
	--docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%dir %{_libdir}/%{name}/
%dir %{_datadir}/%{name}/
%{_libdir}/*.so.1*
%{_libdir}/%{name}/*
%{_datadir}/%{name}/*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_includedir}/%{name}*

%files doc
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}

%changelog
