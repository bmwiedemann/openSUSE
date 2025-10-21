#
# spec file for package gap-inducereduce
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


Name:           gap-inducereduce
Version:        1.3
Release:        0
Summary:        GAP: Unger's algorithm
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/InduceReduce/
#Git-Clone:     https://github.com/gap-packages/InduceReduce
Source:         https://github.com/gap-packages/InduceReduce/releases/download/v%version/InduceReduce-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Requires:       gap-gapdoc >= 1.5

%description
The package "InduceReduce" provides an implementation of Unger's
algorithm for computing the table of ordinary irreducile characters
of a finite group. The algorithm works by inducing characters from
suitably chosen elementary subgroups and finding an orthogonal basis
of the resulting lattice of characters by LLL lattice reduction.

%prep
%autosetup -n InduceReduce-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
