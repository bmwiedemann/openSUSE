#
# spec file for package gap-radiroot
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


Name:           gap-radiroot
Summary:        GAP: Roots of a Polynomial as Radicals
Version:        2.9
Release:        0
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/radiroot/
Source:         https://github.com/gap-packages/radiroot/releases/download/v%{version}/radiroot-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-alnuth >= 3.0
Requires:       gap-core >= 4.7

%description
The package can compute and display an expression by radicals for the
roots of a solvable, rational polynomial. Related to this it is
possible to create the Galois group and the splitting field of a
rational polynomial.

%prep
%setup -qn radiroot-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
