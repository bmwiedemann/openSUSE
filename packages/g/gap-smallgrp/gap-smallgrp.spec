#
# spec file for package gap-smallgrp
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gap-smallgrp
Version:        1.5.4
Release:        0
Summary:        GAP: Small Groups Library
License:        Artistic-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/smallgrp/
#Git-Clone:     https://github.com/gap-packages/SmallGrp
Source:         https://github.com/gap-packages/SmallGrp/releases/download/v%version/SmallGrp-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Requires:       gap-gapdoc >= 1.5

%description
The SmallGrp package provides the library of groups of certain
"small" orders. The groups are sorted by their orders and they are
listed up to isomorphism; that is, for each of the available orders a
complete and irredundant list of isomorphism type representatives of
groups is given.

%prep
%autosetup -n SmallGrp-%version

%build
find . -type f -name "*.g" -exec chmod a-x "{}" "+"
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
