#
# spec file for package gap-homalg
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


Name:           gap-homalg
Version:        2022.11.01
%define sillyver 2022.11-01
Release:        0
Summary:        GAP: A homological algebra meta-package for computable Abelian categories
License:        GPL-2.0
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/homalg
#Git-Clone:	https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/homalg-%sillyver/homalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-toolsforhomalg >= 2012.10.27

%description
The package homalg is the foundational part of the homalg project. It
provides procedures to construct basic objects in homological
algebra:

* filtrations of objects
* complexes (of objects and of complexes)
* chain morphisms
* bicomplexes
* bigraded (differential) objects
* spectral sequences
* functors

%prep
%autosetup -n homalg-%sillyver

%build
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
