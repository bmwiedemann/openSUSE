#
# spec file for package libxslt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname %{name}1
%define exname  libexslt0
Name:           libxslt
Version:        1.1.33
Release:        0
Summary:        XSL Transformation Library
License:        MIT AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://xmlsoft.org/XSLT/
Source0:        ftp://xmlsoft.org/libxslt/libxslt-%{version}.tar.gz
Source1:        ftp://xmlsoft.org/libxslt/libxslt-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        xslt-config.1
Source99:       baselibs.conf
Patch0:         %{name}-1.1.24-no-net-autobuild.patch
Patch1:         libxslt-config-fixes.patch
Patch2:         0009-Make-generate-id-deterministic.patch
Patch3:         libxslt-random-seed.patch
# PATCH-FIX-UPSTREAM bsc#1132160 CVE-2019-11068 Fix security framework bypass
Patch4:         libxslt-CVE-2019-11068.patch
# PATCH-FIX-UPSTREAM bsc#1140095 CVE-2019-13117 Fix uninitialized read of xsl:number token
Patch5:         libxslt-CVE-2019-13117.patch
# PATCH-FIX-UPSTREAM bsc#1140101 CVE-2019-13118 Fix uninitialized read with UTF-8 grouping chars
Patch6:         libxslt-CVE-2019-13118.patch
# PATCH-FIX-UPSTREAM bsc#1154609 CVE-2019-18197 Fix dangling pointer in xsltCopyText
Patch7:         libxslt-CVE-2019-18197.patch
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
Obsoletes:      libxslt-python

%description
This C library allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

It is based on libxml (version 2) for XML parsing, tree manipulation,
and XPath support. It is written in plain C, making as few assumptions
as possible and sticks closely to ANSI C/POSIX for easy embedding.
It includes support for the EXSLT set of extension functions as well
as some common extensions present in other XSLT engines.

%package -n %{libname}
Summary:        XSL Transformation Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname}
This C library allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

It is based on libxml (version 2) for XML parsing, tree manipulation,
and XPath support. It is written in plain C, making as few assumptions
as possible and sticks closely to ANSI C/POSIX for easy embedding.
It includes support for the EXSLT set of extension functions as well
as some common extensions present in other XSLT engines.

%package devel
Summary:        Development files for libxslt
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name}-tools = %{version}
Requires:       glibc-devel
Requires:       libgcrypt-devel
Requires:       libgpg-error-devel

%description devel
libxslt allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

This subpackage contains the header files for developing
applications that want to make use of the XSLT libraries.

%package tools
Summary:        Extended Stylesheet Language (XSL) Transformation utilities
License:        MIT AND GPL-2.0-or-later
Group:          Development/Tools/Other
Provides:       %{name} = %{version}
Provides:       xsltproc = %{version}

%description tools
This package contains xsltproc, a command line interface to the XSLT engine.
xtend the

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
autoreconf -fvi
%configure \
  --disable-static \
  --without-python \
  --disable-silent-rules
make %{?_smp_mflags}

%check
%if ! 0%{?qemu_user_space_build}
make %{?_smp_mflags} check
%endif

%install
%make_install

# Unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/doc
# the manual page is required
install -D -m0644 %{SOURCE3} %{buildroot}%{_mandir}/man1/xslt-config.1
#kill all "la" files
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libxslt.so.*
%{_libdir}/libexslt.so.*

%files tools
%license COPYING*
%doc AUTHORS NEWS README Copyright TODO FEATURES
%{_bindir}/xsltproc
%{_mandir}/man1/xsltproc.1%{?ext_man}

%files devel
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/*.sh
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_includedir}/*
%{_datadir}/aclocal/*
%{_bindir}/xslt-config
%{_mandir}/man1/xslt-config.1%{?ext_man}
%{_mandir}/man3/*
%doc doc/*.html doc/html doc/tutorial doc/*.gif

%changelog
