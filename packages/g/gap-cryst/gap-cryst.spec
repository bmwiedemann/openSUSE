#
# spec file for package gap-cryst
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


Name:           gap-cryst
Version:        4.1.27
Release:        0
Summary:        GAP: Computing with crystallographic groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
#Git-Clone:     https://github.com/gap-packages/cryst

Source:         https://www.math.uni-bielefeld.de/~gaehler/gap/Cryst/cryst-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
Requires:       gap-core >= 4.11
Requires:       gap-polycyclic >= 2.16
Suggests:       gap-caratinterface >= 2.3.3
Suggests:       gap-crystcat >= 1.1.9
Suggests:       gap-xgap >= 4.22

%description
Cryst provides a rich set of methods to compute with affine
crystallographic groups, in particular space groups. Affine
crystallographic groups are fully supported both in the
representation acting from the right and in the representation acting
from the left. The latter representation is the one preferred by
crystallographers. There are also functions to determine
representatives of all space group types of a given dimension.

%prep
%setup -qn cryst

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
