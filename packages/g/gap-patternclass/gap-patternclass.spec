#
# spec file for package gap-patternclass
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


Name:           gap-patternclass
Version:        2.4.3
Release:        0
Summary:        GAP: Permutation pattern class
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/PatternClass/

#Git-Clone:     https://github.com/gap-packages/PatternClass
Source:         https://github.com/gap-packages/PatternClass/releases/download/v%version/PatternClass-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-automata >= 1.13
Requires:       gap-core >= 4.8
Requires:       gap-gapdoc >= 1.5

%description
The PatternClass package is built on the idea of token passing
networks building permutation pattern classes. Those classes are best
determined by their basis. Both sets can be encoded by rank encoding
their permutations. Each, the class and its basis, in their encoded
form build a rational language. Rational languages can be computed by
using automata, which also can be build directly from the token
passing networks. Both ways will build the same language, i.e. the
same automaton.

%prep
%autosetup -n PatternClass-%version

%build

%install
rm -Rf scripts
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
