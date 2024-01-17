#
# spec file for package gap-normalizinterface
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gap-normalizinterface
Version:        1.3.6
Release:        0
Summary:        GAP: wrapper for Normaliz
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/NormalizInterface/
#Git-Clone:     https://github.com/gap-packages/NormalizInterface
Source:         https://github.com/gap-packages/NormalizInterface/releases/download/v%{version}/NormalizInterface-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gap-devel >= 4.9
BuildRequires:  gap-rpm-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  normaliz-devel >= 3.5.4
Requires:       gap-core >= 4.9

%description
The NormalizInterface package provides a GAP interface to Normaliz,
enabling direct access to the complete functionality of Normaliz,
such as computations in affine monoids, vector configurations,
lattice polytopes, and rational cones.

%prep
%autosetup -n NormalizInterface-%version
# Use C++14 for libnormalize with e-antic, see
# https://github.com/gap-packages/NormalizInterface/issues/110
sed -i -e '/AX_CXX_COMPILE_STDCXX/ s/11,/14,/' configure.ac
sed -i -e '/CXXFLAGS/ s/gnu++11/gnu++14/' Makefile.in

%build
autoreconf -fi
%configure --with-gaproot="%gapdir" --with-normaliz="%_prefix"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$moddir"
rm -Rf autom4te.cache config.log config.status configure~ gen/src/*.{o,d}
popd
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
