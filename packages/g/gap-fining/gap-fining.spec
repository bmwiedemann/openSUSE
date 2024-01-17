#
# spec file for package gap-fining
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


Name:           gap-fining
Version:        1.5.6
Release:        0
Summary:        GAP: Finite Incidence Geometry
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/FinInG/
#Git-Clone:     https://github.com/gap-packages/FinInG
Source:         https://github.com/gap-packages/FinInG/releases/download/v%version/fining-%version.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
BuildArch:      noarch
Requires:       gap-core >= 4.10
Requires:       gap-cvec >= 2.7.6
Requires:       gap-forms >= 1.2.5
Requires:       gap-gapdoc >= 1.6.3
Requires:       gap-genss >= 1.6.6
Requires:       gap-grape >= 4.8.2
Requires:       gap-orb >= 4.8.3

%description
FinInG is a package for computation in Finite Incidence Geometry. It
provides users with the basic tools to work in various areas of
finite geometry from the realms of projective spaces to the flat
lands of generalised polygons. The algebraic power of GAP is
employed, particularly in its facility with matrix and permutation
groups.

%prep
%autosetup -n fining-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
