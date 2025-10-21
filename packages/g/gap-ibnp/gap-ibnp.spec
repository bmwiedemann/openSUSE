#
# spec file for package gap-ibnp
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


Name:           gap-ibnp
Version:        0.17
Release:        0
Summary:        GAP: Involutive Bases for Noncommutative Polynomials
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/ibnp/
#Git-Clone:     https://github.com/gap-packages/ibnp
Source:         https://github.com/gap-packages/ibnp/releases/download/v%version/IBNP-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.13
Requires:       gap-gapdoc >= 1.6.1
Requires:       gap-gbnp >= 1.1.0
Requires:       gap-utils >= 0.81

%description
The IBNP package provides methods for computing an involutive
(Groebner) basis B for an ideal J over a polynomial ring R in both
the commutative and noncommutative cases. Secondly, methods are
provided to involutively reduce a given polynomial to its normal form
in R/J.

%prep
%autosetup -n IBNP-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
