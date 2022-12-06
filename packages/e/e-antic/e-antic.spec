#
# spec file for package e-antic
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
%define lname	libeantic1
Name:           e-antic
Version:        1.3.0
Release:        0
Summary:        Real Embedded Algebraic Number Theory in C
License:        LGPL-2.1-or-later AND LGPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/flatsurf/e-antic

Source:         https://github.com/flatsurf/e-antic/releases/download/%version/e-antic-%version.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  antic-devel
BuildRequires:  arb-devel
BuildRequires:  automake
BuildRequires:  cereal-devel
BuildRequires:  fdupes
BuildRequires:  flint-devel >= 2.6
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libtool
BuildRequires:  python-rpm-macros
BuildRequires:  unique-factory-devel
BuildRequires:  pkgconfig(catch2)
Obsoletes:      python-pyeantic < %version-%release
Provides:       python-pyeantic = %version-%release
%python_subpackages

%description
E-ANTIC is a C/C++ library to deal with real embedded number fields
built on top of ANTIC.

%package -n %lname
Summary:        Real Embedded Algebraic Number Theory library in C
Group:          System/Libraries

%description -n %lname
E-ANTIC is a C/C++ library to deal with real embedded number fields
built on top of ANTIC.

%package devel
Summary:        Development files for e-antic
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       antic-devel
Requires:       arb-devel
Requires:       libboost_headers-devel

%description devel
E-ANTIC is a C/C++ library to deal with real embedded number fields
built on top of ANTIC.

This subpackage contains the include files and library links for
developing against the ANTIC library.

%prep
%autosetup -p1

%build
autoreconf -fi
%define _configure ../configure
%{python_expand #
mkdir p%{$python_bin_suffix}/
pushd p%{$python_bin_suffix}/
%configure --disable-static --without-benchmark --without-byexample \
	--without-pytest --without-doc PYTHON="python%{$python_bin_suffix}"
%make_build
popd
}

%install
%{python_expand #
pushd p%{$python_bin_suffix}/
%make_install
popd
}
rm -f "%buildroot/%_libdir"/*.la
find "%buildroot" -name install_files.txt -delete
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPY*
%_libdir/libeantic*.so.1*

%files -n %name-devel
%_includedir/e-antic/
%_includedir/libeantic/
%_libdir/libeantic*.so

%files %python_files
%python_sitelib/pyeantic*/

%changelog
