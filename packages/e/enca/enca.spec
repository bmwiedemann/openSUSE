#
# spec file for package enca
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           enca
Version:        1.19
Release:        0
Summary:        Detects encoding of text files
License:        GPL-2.0
Group:          Productivity/Other
Url:            http://cihar.com/software/enca/
Source:         http://dl.cihar.com/%{name}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  pkgconfig
Requires:       sed

%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings using
either a built-in converter or external libraries and tools like libiconv,
librecode, or cstocs.

Currently, it has support for Belarussian, Bulgarian, Croatian, Czech,
Estonian, Latvian, Lithuanian, Polish, Russian, Slovak, Slovene, Ukrainian,
Chinese, and some multibyte encodings (mostly variants of Unicode)
independent on the language.

This package also contains shared Enca library other programs can make use of.

Install Enca if you need to cope with text files of dubious origin
and unknown encoding and convert them to some reasonable encoding.

%package -n libenca0
Summary:        Header files and libraries for Enca development
Group:          System/Libraries

%description -n libenca0
The enca-devel package contains the static libraries and header files
for writing programs using the Extremely Naive Charset Analyser library,
and its API documentation.

Install enca-devel if you are going to create applications using the Enca
library.

%package devel
Summary:        Header files and libraries for Enca development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libenca0 = %{version}

%description devel
The enca-devel package contains the static libraries and header files
for writing programs using the Extremely Naive Charset Analyser library,
and its API documentation.

Install enca-devel if you are going to create applications using the Enca
library.

%prep
%setup -q

%build
%configure --disable-static --without-librecode
make %{?_smp_mflags}

%install
%make_install
# the .la file is not needed without static libs
rm %{buildroot}/%{_libdir}/libenca.la

%post -n libenca0 -p /sbin/ldconfig
%postun -n libenca0 -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog* FAQ README THANKS TODO
%{_bindir}/enca
%{_bindir}/enconv
%{_libexecdir}/enca
%{_mandir}/man1/enca.1%{ext_man}
%{_mandir}/man1/enconv.1%{ext_man}

%files -n libenca0
%{_libdir}/libenca.so.0*

%files devel
%{_datadir}/gtk-doc/html/*
# Own these repositories to not depend on gtk-doc while building:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_includedir}/enca.h
%{_libdir}/libenca.so
%{_libdir}/pkgconfig/enca.pc

%changelog
