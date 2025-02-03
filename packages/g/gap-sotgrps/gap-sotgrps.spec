#
# spec file for package gap-sotgrps
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gap-sotgrps
Version:        1.3
Release:        0
Summary:        GAP: Small Order Type group construction and identification
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/io/
#Git-Clone:     https://github.com/gap-packages/sotgrps
Source:       	https://github.com/gap-packages/sotgrps/releases/download/v%version/SOTGrps-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-devel >= 4.10
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10

%description
This package for the GAP computer algebra system is complementary to an MPhil
thesis "Groups of small order type" and the joint paper "Groups whose order
factorise into at most four primes" (Dietrich, Eick, & Pan, 2020) from
<https://doi.org/10.1016/j.jsc.2021.04.005>.

%prep
%autosetup -n SOTGrps-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
