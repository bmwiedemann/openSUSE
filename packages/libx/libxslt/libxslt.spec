#
# spec file for package libxslt
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


%define libver 1
%define libexver 0
Name:           libxslt
Version:        1.1.34
Release:        0
Summary:        XSL Transformation Library
License:        GPL-2.0-or-later AND MIT
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
# PATCH-FIX-UPSTREAM gitlab.gnome.org/GNOME/libxslt/commit/9ae2f94df1721e002941b40665efb762aefcea1a
Patch4:         libxslt-Stop-using-maxParserDepth-XPath-limit.patch
# PATCH-FIX-UPSTREAM gitlab.gnome.org/GNOME/libxslt/commit/77c26bad0433541f486b1e7ced44ca9979376908
Patch5:         libxslt-Do-not-set-maxDepth-in-XPath-contexts.patch
Patch6:         Recreate-xsltproc-man-page-with-old-Docbook-styleshe.patch
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel >= 2.9.12
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

%package -n libxslt%{libver}
Summary:        XSL Transformation Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libxslt%{libver}
This C library allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

It is based on libxml (version 2) for XML parsing, tree manipulation,
and XPath support. It is written in plain C, making as few assumptions
as possible and sticks closely to ANSI C/POSIX for easy embedding.
It includes support for the EXSLT set of extension functions as well
as some common extensions present in other XSLT engines.

%package -n libexslt%{libexver}
Summary:        EXSLT Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libexslt%{libexver}
This is the EXSLT C library developed for libxslt.
EXSLT is a community initiative to provide extensions to XSLT.

%package devel
Summary:        Development files for libxslt
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}-tools = %{version}
Requires:       glibc-devel
Requires:       libexslt%{libexver} = %{version}
Requires:       libgcrypt-devel
Requires:       libgpg-error-devel
Requires:       libxslt%{libver} = %{version}

%description devel
libxslt allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

This subpackage contains the header files for developing
applications that want to make use of the XSLT libraries.

%package tools
Summary:        Extended Stylesheet Language (XSL) Transformation utilities
License:        GPL-2.0-or-later AND MIT
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

%build
autoreconf -fvi
%configure \
  --disable-static \
  --without-python \
  --disable-silent-rules
%make_build

%check
%make_build check

%install
%make_install

# Unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/doc
# the manual page is required
install -D -m0644 %{SOURCE3} %{buildroot}%{_mandir}/man1/xslt-config.1
#kill all "la" files
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libxslt%{libver} -p /sbin/ldconfig
%postun -n libxslt%{libver} -p /sbin/ldconfig
%post -n libexslt%{libexver} -p /sbin/ldconfig
%postun -n libexslt%{libexver} -p /sbin/ldconfig

%files -n libxslt%{libver}
%license COPYING* Copyright
%{_libdir}/libxslt.so.%{libver}*

%files -n libexslt%{libexver}
%license COPYING* Copyright
%{_libdir}/libexslt.so.%{libexver}*

%files tools
%license COPYING* Copyright
%doc AUTHORS NEWS README TODO FEATURES
%{_bindir}/xsltproc
%{_mandir}/man1/xsltproc.1%{?ext_man}

%files devel
%license COPYING* Copyright
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
