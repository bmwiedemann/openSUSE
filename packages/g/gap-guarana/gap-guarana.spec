#
# spec file for package gap-guarana
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


Name:           gap-guarana
Version:        0.96.3
Release:        0
Summary:        GAP: Lie methods for computations with infinite polycyclic groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/guarana/
#Git-Clone:     https://github.com/gap-packages/guarana
Source:         https://github.com/gap-packages/guarana/releases/download/v%version/guarana-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7
Requires:       gap-gapdoc >= 1.3
Requires:       gap-polenta >= 1.2.3
Requires:       gap-polycyclic >= 2.11
Requires:       gap-radiroot >= 2.0
Suggests:       gap-alnuth >= 3.0.0
Suggests:       gap-nq >= 2.0

%description
This package demonstrates the algorithmic usefulness of the so-called
Mal'cev correspondence for computations with infinite polycyclic
groups; it is a correspondence that associates to every $\Q$-powered
nilpotent group $H$ a unique rational nilpotent Lie algebra $L_H$ and
vice-versa. The Mal'cev correspondence was discovered by Anatoly
Mal'cev in 1951.

%prep
%autosetup -n guarana-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
