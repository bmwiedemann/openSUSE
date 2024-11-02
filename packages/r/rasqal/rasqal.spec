#
# spec file for package rasqal
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


Name:           rasqal
Version:        0.9.33
Release:        0
%define sonum   3
Summary:        RDF Parser Toolkit for Redland
License:        Apache-2.0+ OR GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Productivity/Other
URL:            http://librdf.org/%{name}/
Source0:        http://download.librdf.org/source/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libraptor-devel
BuildRequires:  mpfr-devel
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       lib%{name}%{sonum} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rasqal is a library providing full support for querying Resource
Description Framework (RDF) including parsing query syntaxes,
constructing the queries, executing them and returning result formats.
It currently handles the RDF Data Query Language (RDQL) and SPARQL
Query language.

%package -n lib%{name}%{sonum}
Summary:        RDF Parser Toolkit for Redland
Group:          System/Libraries

%description -n lib%{name}%{sonum}
Rasqal is a library providing full support for querying Resource
Description Framework (RDF) including parsing query syntaxes,
constructing the queries, executing them and returning result formats.
It currently handles the RDF Data Query Language (RDQL) and SPARQL
Query language.

%package -n lib%{name}-devel
Summary:        Development package for the Rasqal RDF query library
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sonum} = %{version}
Requires:       libraptor-devel >= 2.0.7

%description -n lib%{name}-devel
This package contains the files needed to develop with the Rasqal RDF
query language library.

%package -n lib%{name}-devel-doc
Summary:        Documentation package for lib%{name}-devel
Group:          Development/Languages/C and C++

%description -n lib%{name}-devel-doc
This package contains the documentation and help files to aid with
developing software using the Rasqal RDF query language library.

%prep
%setup -q

%build
%configure --enable-release \
           --disable-static \
           --with-pic \
           --with-regex-library=pcre \
           --with-html-dir=%{_docdir}/lib%{name}-devel/

make %{?_smp_mflags}

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la

%post   -n lib%{name}%{sonum} -p /sbin/ldconfig

%postun -n lib%{name}%{sonum} -p /sbin/ldconfig

%files -n lib%{name}%{sonum}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog
%license COPYING COPYING.LIB
%doc LICENSE-2.0.txt LICENSE.html LICENSE.txt
%doc NEWS NEWS.html NOTICE README README.html RELEASE.html
%{_libdir}/lib%{name}.so.%{sonum}*
%{_mandir}/man1/%{name}-config.1%{ext_man}

%files -n lib%{name}-devel
%defattr(-,root,root,-)
%{_bindir}/%{name}-config
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/lib%{name}.3%{ext_man}

%files -n lib%{name}-devel-doc
%defattr(-,root,root,-)
%{_docdir}/lib%{name}-devel/

%files
%defattr(-,root,root,-)
%{_bindir}/roqet
%{_mandir}/man1/roqet.1%{ext_man}

%changelog
