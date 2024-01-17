#
# spec file for package gap-standardff
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


Name:           gap-standardff
Version:        0.9.4
Release:        0
Summary:        GAP: Standard finite fields and cyclic generators
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/gap/StandardFF/index.html
Source:         https://www.math.rwth-aachen.de/~Frank.Luebeck/gap/StandardFF//StandardFF-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.6.5
Suggests:       gap-ctbllib >= 1.3.1
Suggests:       gap-factint >= 1.6.3

%description
StandardFF provides a reproducible construction of the algebraic closure K of
each finite prime field GF(p). It also implements the construction of
standardized generators of any given order of subgroups of the multiplicative
group of K.

The package contains some utility functions: embeddings of GAP's fields GF(q)
which are defined via Conway polynomials, rewriting of Brauer character values,
discrete logarithms in finite fields, irreducibility test and minimal
polynomials over finite fields.

%prep
%autosetup -n StandardFF-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
