#
# spec file for package gap-mapclass
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


Name:           gap-mapclass
Version:        1.4.6
Release:        0
Summary:        GAP: Package for Mapping Class Orbit Computation
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/MapClass
#Git-Clone:     https://github.com/gap-packages/MapClass
Source:         https://github.com/gap-packages/MapClass/releases/download/v%version/MapClass-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9

%description
The MapClass package calculates the mapping class group orbits for a
given finite group.

%prep
%autosetup -n MapClass-%version

%build

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
