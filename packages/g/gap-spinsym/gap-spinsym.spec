#
# spec file for package gap-spinsym
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


Name:           gap-spinsym
Summary:        GAP: Brauer tables of spin-symmetric groups
Version:        1.5.2
Release:        0
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/spinsym/
#Git-Clone:     https://github.com/gap-packages/spinsym
Source:         https://github.com/gap-packages/spinsym/releases/download/v%version/spinsym-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.5
Requires:       gap-ctbllib >= 1.2.2
Requires:       gap-gapdoc >= 1.5

%description
This package contains Brauer tables of Schur covers of symmetric and
alternating groups, and provides some related functionalities.

%prep
%autosetup -n spinsym-%version

%build
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
