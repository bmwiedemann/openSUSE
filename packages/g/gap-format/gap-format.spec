#
# spec file for package gap-format
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-format
Version:        1.4.3
Release:        0
Summary:        GAP: Computation with formations of finite solvable groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/format/
#Git-Clone:     https://github.com/gap-packages/format
Source:         https://github.com/gap-packages/format/releases/download/v%version/format-%version.tar.gz
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.5

%description
This GAP package provides functions for computing with formations of
finite solvable groups.

%prep
%autosetup -n format-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
