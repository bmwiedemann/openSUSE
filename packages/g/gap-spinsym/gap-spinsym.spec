#
# spec file for package gap-spinsym
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gap-spinsym
Version:        1.5.3
Release:        0
Summary:        GAP: Brauer tables of spin-symmetric groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/spinsym/
#Git-Clone:     https://github.com/gap-packages/spinsym
Source:         https://github.com/gap-packages/spinsym/releases/download/v%version/spinsym-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12
Requires:       gap-ctbllib >= 1.3.0

%description
This package contains Brauer tables of Schur covers of symmetric and
alternating groups, and provides some related functionalities.

%prep
%autosetup -n spinsym-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
