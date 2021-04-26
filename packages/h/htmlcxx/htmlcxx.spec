#
# spec file for package htmlcxx
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Klaus Singvogel, Kaierberg, Germany.
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


Name:           htmlcxx
Version:        0.87
Release:        0
Summary:        HTML and CSS APIs for C++
License:        LGPL-2.0-only AND Apache-2.0
Group:          Productivity/File utilities
URL:            http://htmlcxx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:         %{name}-0.84-cstddef.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
This is a simple non-validating css1 and html parser for C++. Although there are several other html parsers available, htmlcxx has some characteristics that make it unique:

- STL like navigation of DOM tree, using excelent's tree.hh library from Kasper Peeters
- It is possible to reproduce exactly, character by character, the original document from the parse tree
- Bundled css parser
- Optional parsing of attributes
- C++ code that looks like C++ (not so true anymore)
- Offsets of tags/elements in the original document are stored in the nodes of the DOM tree

%package devel
Summary:        Headers and Static Library for htmlcxx
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The htmlcxx-devel package contains libraries and header files for
developing applications that use htmlcxx.

%prep
%setup -q
%patch1 -p1
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir}

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    OPTFLAGS="%{optflags}" \
    OPTLDFLAGS=""

find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files
%license COPYING LGPL_V2 ASF-2.0
%doc AUTHORS ChangeLog README
%{_bindir}/htmlcxx
%{_datadir}/htmlcxx/
%{_libdir}/libcss_parser.so.*
%{_libdir}/libcss_parser_pp.so.*
%{_libdir}/libhtmlcxx.so.*

%files devel
%{_includedir}/htmlcxx/
%{_libdir}/libcss_parser.so
%{_libdir}/libcss_parser_pp.so
%{_libdir}/libhtmlcxx.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
