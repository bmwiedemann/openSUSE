#
# spec file for package gap-unitlib
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


Name:           gap-unitlib
Version:        4.2.0
Release:        0
Summary:        GAP: Library of normalized unit groups of modular group algebras
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/unitlib
#Git-Clone:     https://github.com/gap-packages/unitlib
Source:         https://github.com/gap-packages/unitlib/releases/download/v%version/unitlib-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11
Requires:       gap-gapdoc >= 1.6
Requires:       gap-io >= 4.5
Requires:       gap-laguna >= 3.9.4
Requires:       gzip
Suggests:       gap-scscp >= 2.2

%description
The UnitLib package extends the LAGUNA package and provides the
library of normalized unit groups of modular group algebras of all
finite p-groups of order not greater than 243 over the field of p
elements.

%prep
%setup -qn unitlib-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
