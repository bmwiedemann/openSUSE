#
# spec file for package gap-congruence
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-congruence
Version:        1.2.5
Release:        0
Summary:        GAP: Congruence subgroups of SL(2,Z)
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/congruence/
Source:         https://github.com/gap-packages/congruence/releases/download/v%version/congruence-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
Requires:       gap-core >= 4.8
Requires:       gap-gapdoc >= 1.5.1

%description
The Congruence package provides functions to construct several types
of canonical congruence subgroups in SL_2(Z), and also intersections
of a finite number of such subgroups. Furthermore, it implements the
algorithm for generating Farey symbols for congruence subgroups and
using them to produce a system of independent generators for these
subgroups.

%prep
%autosetup -n congruence-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
