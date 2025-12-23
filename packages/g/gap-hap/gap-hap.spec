#
# spec file for package gap-hap
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


Name:           gap-hap
Version:        1.73
Release:        0
Summary:        GAP: Homological Algebra Programming
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/hap/
#Git-Clone:     https://github.com/gap-packages/hap
Source:         https://github.com/gap-packages/hap/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-aclib >= 1.1
Requires:       gap-core >= 4.12
Requires:       gap-crystcat >= 1.1
Requires:       gap-fga >= 1.1
Requires:       gap-nq >= 1.1
Requires:       gap-polycyclic >= 1.1
Suggests:       gap-congruence
Suggests:       gap-edim >= 1.2.2
Suggests:       gap-gapdoc
Suggests:       gap-hapcryst >= 0.1.0
Suggests:       gap-homology
Suggests:       gap-laguna
Suggests:       gap-nq >= 1.1
Suggests:       gap-polymaking >= 0.8.4
Suggests:       gap-singular >= 06.07.23
Suggests:       gap-xmod

%description
"HAP" is a package for some basic calculations in the cohomology of
finite and infinite groups.

%prep
%autosetup -n hap-%version

%build

%install
find . -type f "(" -name ".*.swp" -o -name "*.bak" ")" -delete
find . -type f -exec grep -L '^#!/' "{}" "+" | xargs -d'\n' -r chmod a-x
find . -type f -exec grep -l "^#!/usr/local/bin/perl" "{}" "+" | \
	xargs -d'\n' -r perl -i -pe 's{#!/usr/local/bin/perl}{#!/usr/bin/perl}g'
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
