#
# spec file for package libdbi
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libdbi
%define lname	libdbi3
Version:        0.9.0.g33
#Snapshot:	libdbi-0.9.0-33-gcdc4479
Release:        0
Summary:        Database Independent Abstraction Layer for C
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
URL:            http://libdbi.sf.net/

#Git-Clone:	git://git.code.sf.net/p/libdbi/libdbi
#Source:         http://downloads.sf.net/libdbi/%name-%version.tar.gz
Source:         %name-%version.tar.xz
Source2:        baselibs.conf
BuildRoot:      %_tmppath/%name-%version-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
%if 0%{?suse_version} >= 1130
# SLE_11 does not have texlive-collection-fontsrecommended
%define build_doc 1
%else
%define build_doc 0
%endif
%if %build_doc
# Only needed when doc is not already prebuilt
BuildRequires:  docbook-dsssl-stylesheets
BuildRequires:  openjade
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-pdftex-bin
%endif

%description
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of
code, programmers can leverage the power of multiple databases and
multiple simultaneous database connections by using this framework.

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
The libdbi-devel package contains the header files and documentation
needed to develop applications with libdbi.

%prep
%setup -qn %name

%build
autoreconf -fi
sed -i s,\-O20,\-O2,g configure
%configure \
%if !%build_doc
	--disable-docs \
%endif
	--disable-static --docdir="%_docdir/%name"
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm README.win32 "%buildroot/%_libdir/libdbi.la"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README*
%_libdir/libdbi.so.3*

%files devel
%defattr(-,root,root)
%_includedir/dbi/
%_libdir/libdbi.so
%_libdir/pkgconfig/dbi.pc
%if %build_doc
%_docdir/%name/
%endif

%changelog
