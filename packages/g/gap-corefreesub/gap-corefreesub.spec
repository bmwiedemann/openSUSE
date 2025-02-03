#
# spec file for package gap-corefreesub
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


Name:           gap-corefreesub
Version:        0.6
Release:        0
Summary:        GAP: 
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/corefreesub/
#Git-Clone:     https://github.com/CAPiedade/corefreesub
Source:       	https://github.com/CAPiedade/corefreesub/releases/download/v%version/corefreesub-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-devel >= 4.11
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11
Requires:       gap-polycyclic >= 2.16
Requires:       graphviz >= 2.43.0
#Requires:      dot2tex

%description
A GAP Package for calculating the core-free subgroups and their
faithful transitive permutation representations.

%prep
%autosetup -n corefreesub-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
