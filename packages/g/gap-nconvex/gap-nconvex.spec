#
# spec file for package gap-nconvex
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


Name:           gap-nconvex
Version:        2022.09.01
%define sillyver 2022.09-01
Release:        0
Summary:        GAP: Polyhedral computations
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/NConvex
Source:         https://github.com/homalg-project/NConvex/releases/download/v%sillyver/NConvex-%sillyver.tar.gz
BuildRequires:  gap-rpm-devel
Requires:       gap-autodoc >= 2018.02.14
Requires:       gap-cddinterface >= 2020.06.24
Requires:       gap-core >= 4.11.1
Requires:       gap-modules >= 0.5
Requires:       gap-normalizinterface >= 1.1.0
Suggests:       gap-4ti2interface >= 2018.07.06
Suggests:       gap-topcominterface >= 2019.06.15

%description
The NConvex package is a GAP package. Its aim is to carry out
polyhedral constructions and computations, namely computing
properties and attributes of cones, polyhedrons, polytopes and fans.

%prep
%autosetup -n NConvex-%sillyver

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
