#
# spec file for package hfst
#
# Copyright (c) 2025 SUSE LLC
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
Version:        3.16.2
Release:        0
Summary:        Helsinki Finite-State Transducer Technology
License:        Apache-2.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND GPL-3.0-only
Group:          Development/Tools/Other
URL:            https://hfst.github.io/

Source:         https://github.com/hfst/hfst/archive/refs/tags/v%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  foma-devel >= 0.9.18+git20210604
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  readline-devel
BuildRequires:  openfst-devel
BuildRequires:  pkgconfig(icu-uc) >= 50
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
Requires:       grep
Requires:       sed

%description
The Helsinki Finite-State Transducer software is intended for the
implementation of morphological analyzers and other tools which are
based on weighted and unweighted finite-state transducer technology.

%package -n libhfst55
Summary:        Helsinki Finite-State Transducer C++ API Library
License:        GPL-3.0-only
Group:          System/Libraries

%description -n libhfst55
The Helsinki Finite-State Transducer software is intended for the
implementation of morphological analyzers and other tools which are
based on weighted and unweighted finite-state transducer technology.

%ifarch %ix86
On 32-bit x86, this package requires the presence of SSE2.
%endif

%package -n libhfst_c0
Summary:        Helsinki Finite-State Transducer C API Library
License:        GPL-3.0-only
Group:          System/Libraries

%description -n libhfst_c0
The Helsinki Finite-State Transducer software is intended for the
implementation of morphological analyzers and other tools which are
based on weighted and unweighted finite-state transducer technology.

%package devel
Summary:        Development files for the Helsinki Finite-State Transducer
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Requires:       libhfst55 = %version
Requires:       libhfst_c0 = %version

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
export CXXFLAGS="%optflags -std=c++17"
%configure --disable-static --with-readline \
	--enable-all-tools --includedir="%_includedir/%name" \
	--with-foma-upstream
%make_build

%install
%make_install
rm -fv "%buildroot/%_libdir"/*.la
# headers not installed
rm -fv "%buildroot/%_libdir/"{libfoma,libfst,libsfst}.so
%fdupes %buildroot/%_prefix

%check
%make_build check -j1

%ldconfig_scriptlets -n libhfst55
%ldconfig_scriptlets -n libhfst_c0

%files
%_bindir/hfst*
%_mandir/man1/*.1*
%doc NEWS README
%license COPYING

%files -n libhfst55
%_libdir/libhfst.so.55*

%files -n libhfst_c0
%_libdir/libhfst_c.so.0*

%files devel
%_includedir/*
%_libdir/libhfst.so
%_libdir/libhfst_c.so
%_libdir/pkgconfig/*.pc
%_datadir/aclocal/

%changelog
