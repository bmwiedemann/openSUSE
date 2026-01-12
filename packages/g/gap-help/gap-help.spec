#
# spec file for package gap-help
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gap-help
Version:        4.1
Release:        0
Summary:        GAP: Hertweck-Luthar-Passi method
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/HeLP/
Source:         https://github.com/gap-packages/HeLP/releases/download/v%version/HeLP-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
# 4ti2: to get /usr/bin/zsolve
Requires:       4ti2 >= 1.6.5
Requires:       gap-4ti2interface >= 2015.04.29
Requires:       gap-atlasrep >= 1.5
Requires:       gap-core >= 4.13
Requires:       gap-ctbllib >= 1.2.2
Requires:       gap-io >= 4.2
Requires:       gap-normalizinterface >= 1.4.1

%description
HeLP is a package to compute constraints on partial augmentations of
torsion units in integral group rings using a method developed by
Luthar, Passi and Hertweck. The package can be employed to verify the
Zassenhaus Conjecture and the Prime Graph Question for finite groups,
once characters are known. It uses an interface to the software
package 4ti2 to solve integral linear inequalities.

%prep
%autosetup -n HeLP-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
