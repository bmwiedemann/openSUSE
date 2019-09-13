#
# spec file for package antlr3c
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Mariusz Fik <fisiu@opensuse.org>.
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


%define soname libantlr3c3
Name:           antlr3c
Version:        3.4
Release:        0
Summary:        C runtime for the ANTLR parsing library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.antlr3.org/
Source:         http://www.antlr3.org/download/C/lib%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         fix-LIST-memory-leak.patch
Patch1:         antlr-64bit.diff
Patch2:         antlr-libversion.diff
Patch3:         fix-hash-double-free.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ANTLR, ANother Tool for Language Recognition, is a language tool that provides a
framework for constructing recognizers, interpreters, compilers, and translators
from grammatical descriptions containing actions in a variety of target
languages. ANTLR provides excellent support for tree construction, tree walking,
translation, error recovery, and error reporting.

%package -n %{soname}
Summary:        C runtime for the ANTLR parsing library
Group:          System/Libraries

%description -n %{soname}
ANTLR, ANother Tool for Language Recognition, is a language tool that provides a
framework for constructing recognizers, interpreters, compilers, and translators
from grammatical descriptions containing actions in a variety of target
languages. ANTLR provides excellent support for tree construction, tree walking,
translation, error recovery, and error reporting.

%package devel
Summary:        C runtime for the ANTLR parsing library
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}

%description devel
ANTLR, ANother Tool for Language Recognition, is a language tool that provides a
framework for constructing recognizers, interpreters, compilers, and translators
from grammatical descriptions containing actions in a variety of target
languages. ANTLR provides excellent support for tree construction, tree walking,
translation, error recovery, and error reporting.

This package contains header files and development libraries needed to
develop programs using the antlr3c library.

%prep
%setup -q -n lib%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%defattr(-,root,root)
%{_libdir}/libantlr3c.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_includedir}/antlr3*
%{_libdir}/libantlr3c.so

%changelog
