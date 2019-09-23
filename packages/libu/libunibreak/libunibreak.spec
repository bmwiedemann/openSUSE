#
# spec file for package libunibreak
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


%define         libversion 3
%define         altver  4_0
Name:           libunibreak
Version:        4.0
Release:        0
Summary:        Unicode line-breaking library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/adah1972/libunibreak
Source0:        https://github.com/adah1972/libunibreak/archive/libunibreak_%{altver}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf >= 2.69
BuildRequires:  libtool
BuildRequires:  pkg-config
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
Requires:       %{name} = %{version}
Requires:       pkgconfig
Obsoletes:      liblinebreak-devel < 2.1
Provides:       liblinebreak-devel = 2.1

%description devel
The libunibreak-devel package contains libraries and header files for
developing applications that use libunibreak.

%package -n libunibreak%{libversion}
Summary:        Unicode line-breaking library
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}

%description -n libunibreak%{libversion}
Libunibreak is the successor of liblinebreak, an implementation of the line
breaking algorithm as described in Unicode 6.0.0 Standard Annex 14, Revision
26, available at http://www.unicode.org/reports/tr14/tr14-26.html

%prep
%setup -q -n %{name}-%{name}_%{altver}

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.*a' -exec rm -f {} ';'

%post -n libunibreak%{libversion} -p /sbin/ldconfig

%postun -n libunibreak%{libversion} -p /sbin/ldconfig

%files -n libunibreak%{libversion}
%doc AUTHORS ChangeLog LICENCE NEWS README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libunibreak.pc

%changelog
