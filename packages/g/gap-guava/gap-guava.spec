#
# spec file for package gap-guava
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


Name:           gap-guava
Version:        3.20
Release:        0
Summary:        GAP package for computing with error-correcting codes
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/guava/
#Git-Clone:     https://github.com/gap-packages/guava
Source:         https://github.com/gap-packages/guava/releases/download/v%version/guava-%version.tar.gz
BuildRequires:  gap-devel >= 4.8.0
BuildRequires:  gap-rpm-devel
BuildRequires:  libtool
Requires:       gap-core >= 4.8.0
Suggests:       gap-sonata >= 2.3

%description
GUAVA is a package that implements coding theory algorithms in GAP.
With GUAVA, codes can be created and manipulated and information
about codes can be calculated.

GUAVA consists of various files written in the GAP language, and an
external program for dealing with automorphism groups of codes and
isomorphism testing functions. Several algorithms that need the speed
are integrated in the GAP kernel.

%prep
%setup -qn guava-%version

%build
./configure "%gapdir"
pushd src/leon/
export CFLAGS="%optflags -Wno-error=return-type"
%configure
popd
%make_build -j1

%install
%gappkg_simple_install
rm -Rf "%buildroot/$moddir/src"

%files -f %name.files

%changelog
