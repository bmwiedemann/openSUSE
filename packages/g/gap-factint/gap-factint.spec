#
# spec file for package gap-factint
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


Name:           gap-factint
Version:        1.6.3
Release:        0
Summary:        GAP: Advanced Methods for Factoring Integers
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/FactInt/

Source:         https://github.com/gap-packages/FactInt/releases/download/v%version/FactInt-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8.8
Requires:       gap-gapdoc >= 1.6

%description
FactInt is a GAP 4 package which provides routines for factoring
integers, in particular:

  * Pollard's p-1
  * Williams' p+1
  * Elliptic Curves Method (ECM)
  * Continued Fraction Algorithm (CFRAC)
  * Multiple Polynomial Quadratic Sieve (MPQS)

It also provides access to  Richard P. Brent's tables  of factors of
integers of the form b^k +/- 1.

%prep
%autosetup -n FactInt-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
