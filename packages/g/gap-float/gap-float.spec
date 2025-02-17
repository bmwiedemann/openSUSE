#
# spec file for package gap-float
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gap-float
Version:        1.0.5
Release:        0
Summary:        GAP: Integration of mpfr, mpfi, mpc, fplll and cxsc in GAP
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/float/
#Git-Clone:	https://github.com/gap-packages/float
Source:         https://github.com/gap-packages/float/releases/download/v%version/float-%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gap-devel >= 4.11
BuildRequires:  gap-rpm-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  mpc-devel
BuildRequires:  mpfi-devel
BuildRequires:  mpfr-devel
BuildRequires:  pkgconfig(fplll) >= 5
Requires:       gap-core >= 4.11
Requires:       gap-gapdoc >= 1.0

%description
The Float package allows GAP to manipulate floating-point numbers
with arbitrary precision. It is based on MPFR, MPFI, MPC, CXSC,
FPLLL.

%prep
%autosetup -n float-%version -p1

%build
autoreconf -fi
%configure --with-gaproot="%gapdir" --without-cxsc
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
rm -Rf aclocal.m4 autom4* build-aux config.* configu* libtool* m4 src/
popd

%files -f %name.files

%changelog
