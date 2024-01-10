#
# spec file for package gap-permut
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


Name:           gap-permut
Version:        2.0.4
Release:        0
Summary:        GAP: Permutability in finite groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/permut/

#Git-Clone:     https://github.com/gap-packages/permut
Source:         https://github.com/gap-packages/permut/releases/download/v%version/permut-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7.4
Requires:       gap-format >= 1.3

%description
This package provides functions for computing with permutability in
finite groups.

%prep
%autosetup -n permut-%version

%build

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
