#
# spec file for package gap-primgrp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gap-primgrp
Version:        4.0.2
Release:        0
Summary:        GAP: Primitive Permutation Groups Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/primgrp/
Source:         https://github.com/gap-packages/primgrp/releases/download/v%{version}/primgrp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10
Requires:       gap-gapdoc >= 1.5

%description
The PrimGrp package provides the library of primitive permutation
groups which includes, up to permutation isomorphism (i.e., up to
conjugacy in the corresponding symmetric group), all primitive
permutation groups of degree < 4096.

%prep
%autosetup -p1 -n primgrp-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
