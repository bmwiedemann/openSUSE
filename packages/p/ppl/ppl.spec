#
# spec file for package ppl
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 14
Name:           ppl
Version:        1.2
Release:        0
Summary:        The Parma Polyhedra Library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.bugseng.com/parma-polyhedra-library

#Git-Web:	http://www.cs.unipr.it/git/gitweb.cgi?p=ppl/ppl.git;a=summary
#Git-Clone:	git://git.cs.unipr.it/ppl/ppl
Source:         http://bugseng.com/products/ppl/download/ftp/releases/%version/ppl-%version.tar.xz
Source2:        http://bugseng.com/products/ppl/download/ftp/releases/%version/ppl-%version.tar.xz.sign
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel >= 4.1.3
BuildRequires:  m4
BuildRequires:  xz

%description
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial optimization
and statistical data-editing.  The Parma Polyhedra Library comes with
several user friendly interfaces, is fully dynamic (available virtual
memory is the only limitation to the dimension of anything), written in
accordance to all the applicable standards, exception-safe, rather
efficient, thoroughly documented, and free software.  This package
provides all what is necessary to run applications using the PPL
through its C and C++ interfaces.

%package devel
Summary:        Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:          Development/Libraries/C and C++
Requires:       gmp-devel >= 4.1.3
Requires:       libppl%sover = %version
Requires:       libppl_c4 = %version
Recommends:     ppl-doc = %version

%description devel
The header files, Autoconf macro, and ppl-config tool for developing
applications using the Parma Polyhedra Library through its C and C++
interfaces.

%package -n libppl%sover
Summary:        C++ interface of the Parma Polyhedra Library
Group:          System/Libraries

%description -n libppl%sover
Shared library for the Parma Polyhedra Library.

%package -n libppl_c4
Summary:        C interface of the Parma Polyhedra Library
Group:          System/Libraries

%description -n libppl_c4
Shared library for the Parma Polyhedra Library C bindings.

%package doc
Summary:        Documentation for the Parma Polyhedra Library
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains all the documentations required by programmers
using the Parma Polyhedra Library (PPL). Install this package if you
want to program with the PPL.

%prep
%autosetup -p1 -n ppl-%version

%build
if [ ! -e configure ]; then autoreconf -fi; fi
%configure \
	--disable-static --disable-rpath --disable-watchdog \
	--disable-ppl_lpsol --disable-ppl_lcdd
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%if "%name" == "ppl-testsuite"
%check
# https://www.cs.unipr.it/mantis/view.php?id=1078
# https://www.cs.unipr.it/mantis/view.php?id=2113
# both behind a stupid login wall
%make_build check

%install

%else

%install
%make_install INSTALL="install -p"
rm -f "%buildroot/%_libdir"/*.la
# We don't build the binary, so delete its manpage
rm -f %buildroot/%_mandir/man1/ppl_lpsol.1
# We don't build pwl
rm -Rf %buildroot/%_datadir/doc/pwl
# The pdf is enough
rm -f %buildroot/%_datadir/doc/%name/ppl-user-*.ps.gz
rm -f %buildroot/%_datadir/doc/%name/ChangeLog
rm -f %buildroot/%_datadir/doc/%name/README.configure
rm -f %buildroot/%_datadir/doc/%name/TODO
rm -f %buildroot/%_datadir/doc/%name/gpl.*
rm -f %buildroot/%_datadir/doc/%name/fdl.ps.gz
rm -f %buildroot/%_datadir/doc/%name/fdl.pdf
rm -Rf %buildroot/%_datadir/doc/%name/ppl-user-prolog-interface-%{version}*
rm -Rf %buildroot/%_datadir/doc/%name/ppl-user-ocaml-interface-%{version}*
rm -Rf %buildroot/%_datadir/doc/%name/ppl-user-java-interface-%{version}*
# %%name == ppl
%endif
%fdupes -s %buildroot

%post   -n libppl%sover -p /sbin/ldconfig
%postun -n libppl%sover -p /sbin/ldconfig
%post   -n libppl_c4 -p /sbin/ldconfig
%postun -n libppl_c4 -p /sbin/ldconfig

%if "%name" == "ppl"
%files
%dir %_datadir/doc/%name
%doc %_datadir/doc/%name/BUGS
%doc %_datadir/doc/%name/COPYING
%doc %_datadir/doc/%name/CREDITS
%doc %_datadir/doc/%name/NEWS
%doc %_datadir/doc/%name/README
%_bindir/ppl_pips
%_mandir/man1/ppl_pips.1.gz

%files -n libppl%sover
%_libdir/libppl.so.*

%files -n libppl_c4
%_libdir/libppl_c.so.*

%files devel
%_includedir/ppl.hh
%_includedir/ppl_c.h
%_libdir/libppl.so
%_libdir/libppl_c.so
%_bindir/ppl-config
%_mandir/man1/ppl-config.1.gz
%_mandir/man3/libppl.3.gz
%_mandir/man3/libppl_c.3.gz
%dir %_datadir/aclocal
%_datadir/aclocal/ppl.m4
%_datadir/aclocal/ppl_c.m4

%files doc
%doc %_datadir/doc/%name/README.doc
%doc %_datadir/doc/%name/fdl.txt
%doc %_datadir/doc/%name/ppl-user-%version-html/
%doc %_datadir/doc/%name/ppl-user-c-interface-%version-html/
%doc %_datadir/doc/%name/ppl-user-%version.pdf
%doc %_datadir/doc/%name/ppl-user-c-interface-%version.pdf
%endif

%changelog
