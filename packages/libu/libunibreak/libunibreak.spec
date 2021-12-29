#
# spec file for package libunibreak
#
# Copyright (c) 2021 SUSE LLC
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


%define         libversion 5
%define         altver  5_0
Name:           libunibreak
Version:        5.0
Release:        0
Summary:        Unicode line-breaking library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/adah1972/libunibreak
Source0:        https://github.com/adah1972/libunibreak/releases/download/libunibreak_%{altver}/%{name}-%{version}.tar.gz
Source1:        http://www.unicode.org/Public/UNIDATA/auxiliary/LineBreakTest.txt
Source2:        http://www.unicode.org/Public/UNIDATA/auxiliary/WordBreakTest.txt
Source3:        http://www.unicode.org/Public/UNIDATA/auxiliary/GraphemeBreakTest.txt
BuildRequires:  pkgconfig
Obsoletes:      liblinebreak < 2.1
Provides:       liblinebreak = 2.1

%description
Libunibreak is the successor of liblinebreak, an implementation of the line
breaking algorithm as described in Unicode 6.0.0 Standard Annex 14, Revision
26, available at http://www.unicode.org/reports/tr14/tr14-26.html

It is designed to be used in a generic text renderer. FBReader is one
real-world example, and you may also check some simple sample code, like
showbreak and breaktext.

%package devel
Summary:        Development files for libunibreak
Group:          Development/Libraries/C and C++
Requires:       %{name}%{libversion} = %{version}
Requires:       pkgconfig
Obsoletes:      liblinebreak-devel < 2.1
Provides:       liblinebreak-devel = 2.1

%description devel
The libunibreak-devel package contains libraries and header files for
developing applications that use libunibreak.

%package -n libunibreak%{libversion}
Summary:        Unicode line-breaking library
Group:          Development/Libraries/C and C++

%description -n libunibreak%{libversion}
Libunibreak is an implementation of the line breaking and word breaking
algorithm as described in Unicode Standard Annex 14 and Unicode Standard
Annex 29.

%prep
%setup -q
for source in %{SOURCE1} %{SOURCE2} %{SOURCE3}; do
	install -m0644 $source src/
done

%build
%configure \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.*a' -print -delete

%check
%make_build check

%post -n libunibreak%{libversion} -p /sbin/ldconfig
%postun -n libunibreak%{libversion} -p /sbin/ldconfig

%files -n libunibreak%{libversion}
%license LICENCE
%{_libdir}/*.so.%{libversion}{,.*}

%files devel
%license LICENCE
%doc AUTHORS NEWS README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libunibreak.pc

%changelog
