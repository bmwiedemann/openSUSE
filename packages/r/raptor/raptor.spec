#
# spec file for package raptor
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


Name:           raptor
Version:        2.0.15
Release:        0
Summary:        RDF Parser Toolkit
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR Apache-2.0
Group:          System/Libraries
URL:            http://librdf.org/raptor/
Source0:        http://download.librdf.org/source/%{name}2-%{version}.tar.gz
Source1:        http://download.librdf.org/source/raptor2-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch1:         https://raw.githubusercontent.com/LibreOffice/core/master/external/redland/raptor/0001-Calcualte-max-nspace-declarations-correctly-for-XML-.patch.1
Patch2:         https://raw.githubusercontent.com/LibreOffice/core/master/external/redland/raptor/ubsan.patch
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  libicu-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
%if !0%{?sles_version}
BuildRequires:  pkgconfig(libxml-2.0)
%else
BuildRequires:  libxml2-devel
%endif

%description
Raptor is the RDF Parser Toolkit for Redland that provides a set of
standalone RDF parsers, generating triples from RDF/XML or N-Triples.

%package -n libraptor2-0
Summary:        RDF Parser Toolkit
Group:          System/Libraries

%description -n libraptor2-0
Raptor is the RDF Parser Toolkit for Redland that provides a set of
standalone RDF parsers, generating triples from RDF/XML or N-Triples.

%package -n libraptor-devel
Summary:        Development package for the raptor library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libraptor2-0 = %{version}
Requires:       raptor = %{version}
Provides:       raptor-devel = %{version}
Obsoletes:      raptor-devel < %{version}

%description -n libraptor-devel
This package contains the files needed to compile programs that use the
raptor library.

%prep
%setup -q -n %{name}2-%{version}
%patch1 -p1
%patch2

%build
%configure \
	--disable-gtk-doc \
	--disable-static \
	--with-pic \
	--with-icu-config=%{_bindir}/icu-config \
	--with-html-dir=%{_docdir}
%make_build

%install
%make_install
mv %{buildroot}%{_docdir}/raptor2 %{buildroot}%{_docdir}/raptor-devel
#causes some ugly  dependency bloat..
rm -f %{buildroot}%{_libdir}/libraptor2.la

%check
export MALLOC_CHECK_=2
make check
unset MALLOC_CHECK_

%post -n libraptor2-0 -p /sbin/ldconfig
%postun -n libraptor2-0 -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB LICENSE.txt
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/rapper
%{_mandir}/man?/*

%files -n libraptor-devel
%doc %{_docdir}/raptor-devel
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%files -n libraptor2-0
%{_libdir}/libraptor2.so.0*

%changelog
