#
# spec file for package gap-qpa
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-qpa
Version:        1.34
Release:        0
Summary:        GAP: Quivers and Path Algebras
License:        GPL-2.0
Group:          Productivity/Scientific/Math
URL:            https://folk.ntnu.no/oyvinso/QPA/
#Git-Clone:     https://github.com/gap-packages/qpa
Source:         https://folk.ntnu.no/oyvinso/QPA/qpa-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
Requires:       gap-core >= 4.5
Requires:       gap-gbnp >= 0.9.5

%description
The QPA package provides data structures and algorithms for doing
computations with finite dimensional quotients of path algebras, and
finitely generated modules over such algebras. The current version of
the QPA package has data structures for quivers, quotients of path
algebras, and modules, homomorphisms and complexes of modules over
quotients of path algebras.

%prep
%autosetup -n qpa-%version

%build

%install
%gappkg_simple_install
find "%buildroot" -type f "(" -name "*.g?" -o -name "*.xml" ")" \
	-exec chmod a-x "{}" "+"

%files -f %name.files

%changelog
