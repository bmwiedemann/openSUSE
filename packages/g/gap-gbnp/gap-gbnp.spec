#
# spec file for package gap-gbnp
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-gbnp
Version:        1.1.0
Release:        0
Summary:        GAP: computing Gröbner bases of noncommutative polynomials
License:        LGPL-2.1+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/gbnp/
Source:         https://github.com/gap-packages/gbnp/releases/download/v%version/gbnp-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-gapdoc >= 1.5

%description
This package enhances GAP4 to support computing Gröbner bases of
non-commutative polynomials with coefficients from a field
implemented in GAP, and some variations, such as a weighted and
truncated version and a tracing facility.

The word algorithm is interpreted loosely: in general, one cannot
expect such an algorithm to terminate, as it would imply solvability
of the word problem for finitely presented (semi)groups.

%prep
%autosetup -n gbnp-%version -p1

%build

%install
find . -type f -name .depend -print -delete
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
