#
# spec file for package gap-nilmat
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


Name:           gap-nilmat
Version:        1.4.2
Release:        0
Summary:        GAP: Computing with nilpotent matrix groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/nilmat/
#Git-Clone:     https://github.com/gap-packages/nilmat
Source:         https://github.com/gap-packages/nilmat/releases/download/v%version/nilmat-%version.tar.bz2
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-polenta >= 1.0

%description
This package contains methods for checking whether a given matrix
group is nilpotent and for computing with nilpotent matrix groups.
The considered matrix groups may be matrix groups over a finite field
or the field of rational numbers.

%prep
%autosetup -n nilmat-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
