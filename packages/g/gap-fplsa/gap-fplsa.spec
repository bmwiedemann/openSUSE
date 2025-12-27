#
# spec file for package gap-fplsa
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gap-fplsa
Version:        1.2.8
Release:        0
Summary:        GAP: Finitely Presented Lie Algebras
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/FPLSA/
#Git-Clone:     https://github.com/gap-packages/FPLSA
Source:         https://github.com/gap-packages/FPLSA/releases/download/v%version/FPLSA-%version.tar.gz
BuildRequires:  c_compiler
BuildRequires:  gap-devel >= 4.8
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
The FPLSA package uses a C program that implements a Lie Todd–Coxeter
method for converting finitely presented Lie algebras into isomorphic
structure constant algebras. This is called via the GAP function
IsomorphismSCTableAlgebra.

%prep
%autosetup -n FPLSA-%version -p1

%build
./configure "%gapdir" # not autoconf
%make_build

%install
%gappkg_simple_install
cd "%buildroot/$fmoddir/"
rm -Rf Makefile* configure src/

%files -f %name.files

%changelog
