#
# spec file for package libt3highlight
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


Name:           libt3highlight
%define lname	libt3highlight2
Version:        0.4.8
Release:        0
Summary:        The Tilde Toolkit's syntax highlighting library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://os.ghalkes.nl/t3/libt3highlight.html

#Git-Clone:	git://github.com/gphalkes/t3highlight
Source:         https://os.ghalkes.nl/dist/%name-%version.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libt3config) >= 0.2.5

%description
libt3highlight is a library that provides functions for syntax
highlighting different types of text files.

%package -n %lname
Summary:        The Tilde Toolkit's syntax highlighting library
Group:          System/Libraries

%description -n %lname
libt3highlight is a library that provides functions for syntax
highlighting different types of text files.

%package devel
Summary:        Development files for libt3highlight, a syntax highlighting library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libt3highlight is a library that provides functions for syntax
highlighting different types of text files.

This subpackage contains libraries and header files for developing
applications that want to make use of libt3highlight.

%package utils
Summary:        Utilities for working with libt3highlight
Group:          Productivity/Other

%description utils
libt3highlight is a library that provides functions for syntax
highlighting different types of text files.

This subpackage contains the T3 highlighting utility.

%prep
%autosetup -p1

%build
export CC=gcc
%configure --docdir="%_docdir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post   -p /sbin/ldconfig -n %lname
%postun -p /sbin/ldconfig -n %lname

%files -n %lname
%_libdir/libt3highlight.so.2*
%_datadir/%lname/
%license COPYING

%files devel
%_includedir/t3/
%_libdir/libt3highlight.so
%_libdir/pkgconfig/libt3highlight.pc
%_docdir/%name/
%exclude %_docdir/%name/COPYING

%files utils
%_bindir/t3*
%_mandir/man1/t3*.1*

%changelog
