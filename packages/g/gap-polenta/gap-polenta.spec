#
# spec file for package gap-polenta
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


Name:           gap-polenta
Version:        1.3.10
Release:        0
Summary:        GAP: Polycyclic presentations for matrix groups
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/polenta/
#Git-Clone:	https://github.com/gap-packages/polenta
Source:         https://github.com/gap-packages/polenta/releases/download/v%version/polenta-%version.tar.bz2
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-alnuth >= 2.2.3
Requires:       gap-core >= 4.7
Requires:       gap-polycyclic >= 2.10.1
Requires:       gap-radiroot >= 2.4
Suggests:       gap-aclib >= 1.0

%description
The Polenta package provides methods to compute polycyclic
presentations of matrix groups (finite or infinite). As a by-product,
this package gives some functionality to compute certain module
series for modules of solvable groups. For example, if G is a
rational polycyclic matrix group, then we can compute the radical
series of the natural Q[G]-module Q^d.

%prep
%autosetup -n polenta-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
