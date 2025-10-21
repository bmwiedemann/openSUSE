#
# spec file for package gap-twistedconjugacy
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


Name:           gap-twistedconjugacy
Version:        3.1.1
Release:        0
Summary:        GAP: Computation with twisted conjugacy classes
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://stertooy.github.io/TwistedConjugacy/
#Git-Clone:     https://github.com/stertooy/TwistedConjugacy
Source:         https://github.com/stertooy/TwistedConjugacy/releases/download/v%version/TwistedConjugacy-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.14
Requires:       gap-autpgrp >= 1.11
Requires:       gap-polycyclic >= 2.16

%description
The TwistedConjugacy package provides methods for solving the twisted
conjugacy problem (including the "search" and "multiple" variants)
and for computing Reidemeister classes, numbers, spectra, and zeta
functions. It also includes utility functions for working with
(double) cosets, group homomorphisms, and group derivations.

These methods are primarily designed for use with finite groups and
with PcpGroups (finite or infinite) provided by the Polycyclic
package.

%prep
%autosetup -n TwistedConjugacy-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
