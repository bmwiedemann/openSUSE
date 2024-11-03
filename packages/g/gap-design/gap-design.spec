#
# spec file for package gap-design
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


Name:           gap-design
Summary:        GAP: The Design Package for GAP
Version:        1.8.2
Release:        0
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/design/
#Git-Clone:     https://github.com/gap-packages/design
Source:         https://github.com/gap-packages/design/releases/download/v%version/design-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
Requires:       gap-core >= 4.10
Requires:       gap-grape >= 4.8
Suggests:       gap-gapdoc >= 1.6
BuildArch:      noarch

%description
The DESIGN package is for constructing, classifying, partitioning and
studying block designs.

%prep
%autosetup -n design-%version -p1

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
