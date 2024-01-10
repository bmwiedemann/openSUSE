#
# spec file for package gap-fga
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gap-fga
Version:        1.4.0
Release:        0
Summary:        GAP: Free Group Algorithms
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.icm.tu-bs.de/ag_algebra/software/FGA/
#Git-Clone:     https://github.com/chsievers/fga
Source:         http://www.icm.tu-bs.de/ag_algebra/software/FGA/FGA-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
The FGA package provides methods for computations with finitely
generated subgroups of free groups.

It allows you to (constructively) test membership and conjugacy, and
to compute free generators, the rank, the index, normalizers,
centralizers, and intersections where the groups involved are
finitely generated subgroups of free groups.

In addition, it provides generators and a finite presentation for the
automorphism group of a finitely generated free group and allows to
write any such automorphism as word in these generators.

%prep
%autosetup -n fga

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
