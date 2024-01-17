#
# spec file for package gap-edim
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


Name:           gap-edim
Version:        1.3.7
Release:        0
Summary:        GAP: Elementary Divisors of Integer Matrices
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/EDIM/index.html
#Git-Clone:     https://github.com/frankluebeck/EDIM
Source:         https://www.math.rwth-aachen.de/~Frank.Luebeck/EDIM/EDIM-%version.tar.bz2
BuildRequires:  gap-devel >= 4.12
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.6

%description
This package provides a collection of functions for computing the
Smith normal form of integer matrices and some related utilities.

%prep
%autosetup -n EDIM-%version

%build
./configure "%gapdir"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
rm -Rf src/
popd

%files -f %name.files

%changelog
