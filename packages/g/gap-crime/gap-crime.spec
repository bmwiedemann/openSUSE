#
# spec file for package gap-crime
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


Name:           gap-crime
Version:        1.6
Release:        0
Summary:        GAP: Calculation of group cohomology and Massey products
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/crime/

Source:         https://github.com/gap-packages/crime/releases/download/v%version/crime-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
Requires:       gap-core >= 4.9

%description
This GAP package computes cohomology rings for finite p-groups using
Jon Carlson's method, both as GAP objects, and also in terms of
generators and relators. It also computes induced homomorphisms on
cohomology and Massey products in the cohomology ring.

%prep
%autosetup -n crime-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
