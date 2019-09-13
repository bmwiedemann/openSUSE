#
# spec file for package hfst
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


Name:           hfst
Version:        3.15.0
Release:        0
Summary:        Helsinki Finite-State Transducer Technology
License:        GPL-3.0-or-later AND GPL-3.0-only AND GPL-2.0-or-later AND GPL-2.0-only AND GPL-3.0-only AND Apache-2.0
Group:          Development/Tools/Other
URL:            https://hfst.github.io/

Source:         https://github.com/hfst/hfst/releases/download/v%version/hfst-%version.tar.gz
Patch1:         hfst-wrong-flags.diff
Patch2:         hfst-split-libs.diff
Patch3:         hfst-nodate.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
Requires:       grep
Requires:       sed

%description
The Helsinki Finite-State Transducer software is intended for the
implementation of morphological analyzers and other tools which are
based on weighted and unweighted finite-state transducer technology.

%package -n libfoma-hfst0
Summary:        Multi-purpose finite-state toolkit
License:        GPL-2.0-only
Group:          System/Libraries

%description -n libfoma-hfst0
Foma is a multi-purpose finite-state toolkit designed for
applications ranging from natural language processing and research in
automata theory. It should be upwardly compatible with Xerox xfst and
lexc, with the exception of binary file reading and writing.

%package -n libfst-hfst0
Summary:        OpenFST Finite State Transducer library
License:        Apache-2.0
Group:          System/Libraries

%description -n libfst-hfst0
OpenFst is a library for constructing, combining, optimizing, and
searching weighted finite-state transducers (FSTs).

%package -n libhfst52
Summary:        Helsinki Finite-State Transducer Technology Libraries
License:        GPL-3.0-only
Group:          System/Libraries

%description -n libhfst52
The Helsinki Finite-State Transducer software is intended for the
implementation of morphological analyzers and other tools which are
based on weighted and unweighted finite-state transducer technology.

%package -n libsfst-hfst0
Summary:        SFST Finite State Tools
# HFST is missing the license file; a look in SFST upstream code
# (https://code.google.com/p/cistern/wiki/SFST) reveals it is GPL-2.0.
License:        GPL-2.0-only
Group:          System/Libraries

%description -n libsfst-hfst0
SFST is a toolkit for the implementation of morphological analyzers
and other tools which are based on finite state transducer
technology.

%package devel
Summary:        Development files for the Helsinki Finite-State Transducer
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Requires:       libhfst52 = %version

%description devel
The Helsinki Finite-State Transducer software is intended for the
implementation of morphological analyzers and other tools which are
based on weighted and unweighted finite-state transducer technology.

This subpackage contains the files necessary to build programs that
want to make use of the HFST library.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static --with-unicode-handler=glib --with-readline \
	--enable-all-tools --includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
# headers not installed
rm -f "%buildroot/%_libdir/"{libfoma,libfst,libsfst}.so
%fdupes %buildroot/%_prefix

%post   -n libfoma-hfst0 -p /sbin/ldconfig
%postun -n libfoma-hfst0 -p /sbin/ldconfig
%post   -n libfst-hfst0 -p /sbin/ldconfig
%postun -n libfst-hfst0 -p /sbin/ldconfig
%post   -n libhfst52 -p /sbin/ldconfig
%postun -n libhfst52 -p /sbin/ldconfig
%post   -n libsfst-hfst0 -p /sbin/ldconfig
%postun -n libsfst-hfst0 -p /sbin/ldconfig

%files
%_bindir/hfst*
%_mandir/man1/*.1*
%doc AUTHORS COPYING NEWS README

%files -n libfoma-hfst0
%_libdir/libfoma-hfst.so.0*
%doc back-ends/foma/COPYING

%files -n libfst-hfst0
%_libdir/libfst-hfst.so.0*
%doc back-ends/openfst/COPYING

%files -n libhfst52
%_libdir/libhfst.so.52*

%files -n libsfst-hfst0
%_libdir/libsfst-hfst.so.0*

%files devel
%_includedir/*
%_libdir/libhfst.so
%_libdir/pkgconfig/*.pc
%_datadir/aclocal/

%changelog
