#
# spec file for package gap-sophus
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


Name:           gap-sophus
Version:        1.27
Release:        0
Summary:        GAP: Computing in nilpotent Lie algebras
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/sophus/
#Git-Clone:     https://github.com/gap-packages/sophus
Source:         https://github.com/gap-packages/sophus/releases/download/v%version/sophus-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-autpgrp >= 1.2

%description
The Sophus package computes nilpotent Lie algebras over finite prime
fields. The cover, the list of immediate descendants, and the
automorphism group of such Lie algebras can be computed and tested
for whether two such Lie algebras are isomorphic.

The immediate descendant function of the package can be used to
classify small-dimensional nilpotent Lie algebras over a given field.
For instance, the package author obtained a classification of
nilpotent Lie algebras with dimension at most 9 over F_2.

%prep
%autosetup -n sophus-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
