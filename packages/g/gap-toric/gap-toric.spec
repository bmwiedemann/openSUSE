#
# spec file for package gap-toric
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


Name:           gap-toric
Summary:        GAP: toric varieties and some combinatorial geometry computations
Version:        1.9.5
Release:        0
License:        MIT
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/toric
Source:         https://github.com/gap-packages/toric/releases/download/v%{version}/Toric-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.5

%description
"toric" is a package that implements some computations related to
toric varieties and combinatorial geometry in GAP. With "toric",
affine toric varieties can be created and related information about
them can be calculated. "toric" is written entirely in the GAP
language by D. Joyner.

%prep
%setup -qn Toric-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
