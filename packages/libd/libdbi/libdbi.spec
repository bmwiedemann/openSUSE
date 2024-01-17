#
# spec file for package libdbi
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%global flavor @BUILD_FLAVOR@%nil

%global sname libdbi
%if "%flavor" == "devel-doc"
%global psuffix -devel-doc
%endif

Name:           libdbi%{?psuffix}
%define lname	libdbi3
Version:        0.9.0.g33
#Snapshot:	libdbi-0.9.0-33-gcdc4479
Release:        0
%if "%flavor" == ""
Summary:        Database Independent Abstraction Layer for C
Group:          Development/Libraries/C and C++
%endif
License:        LGPL-2.1-or-later
URL:            http://libdbi.sourceforge.net/

#Git-Clone:	git://git.code.sf.net/p/libdbi/libdbi
#Source:         http://downloads.sf.net/libdbi/%%name-%%version.tar.gz
Source:         %sname-%version.tar.xz
Source2:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
%if "%flavor" == "devel-doc"
# Only needed when doc is not already prebuilt
BuildRequires:  docbook-dsssl-stylesheets
BuildRequires:  openjade
BuildRequires:  tex(8r.enc)
BuildRequires:  tex(t1ptm.fd)
BuildRequires:  tex(t1phv.fd)
BuildRequires:  tex(uwasy.fd)
BuildRequires:  tex(wasy10.tfm)
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-pdftex-bin
Provides:       libdbi-devel:%_docdir/libdbi/driver-guide.pdf
%endif

%if "%flavor" == ""
%description
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of
code, programmers can leverage the power of multiple databases and
multiple simultaneous database connections by using this framework.

%else
Summary:        Development documentation for libdbi
Group:          Documentation/Other
BuildArch:      noarch

%description
The libdbi-devel-doc package contains libdbi programmers-guide
and driver-guide.
%endif

%package -n %lname
Summary:        Database Independent Abstraction Layer for C
Group:          System/Libraries

%description -n %lname
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of
code, programmers can leverage the power of multiple databases and
multiple simultaneous database connections by using this framework.

%package devel
Summary:        Development files for libdbi (Database Independent Abstraction Layer for C)
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The libdbi-devel package contains the header files needed to develop
applications with libdbi.


%prep
%setup -qn %sname

%build
autoreconf -fi
sed -i s,\-O20,\-O2,g configure
%configure \
%if "%flavor" == ""
	--disable-docs \
%else
	--enable-docs \
%endif
	--docdir="%_docdir/libdbi" \
	--disable-static

%if "%flavor" == ""
%make_build
%else
%make_build -C doc
%endif

%install
%if "%flavor" == ""
%make_install
rm "%buildroot/%_libdir/libdbi.la"

%else
%make_install -C doc
%endif


%if "%flavor" == ""
%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%doc AUTHORS ChangeLog README
%license COPYING
%_libdir/libdbi.so.3*

%files devel
%_includedir/dbi/
%_libdir/libdbi.so
%_libdir/pkgconfig/dbi.pc

%else

%files -n %sname-devel-doc
%dir %_docdir/libdbi
%_docdir/libdbi/*-guide*

%endif

%changelog
