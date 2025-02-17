#
# spec file for package gap-gauss
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


Name:           gap-gauss
Version:        2024.11.01
%define sillyver 2024.11-01
Release:        0
Summary:        GAP: Extended Gauss Functionality for GAP
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/Gauss
#Git-Clone:	https://github.com/homalg-project/homalg_project
#Git-Web:	https://github.com/homalg-project/Gauss
Source:         https://github.com/homalg-project/homalg_project/releases/download/Gauss-%sillyver/Gauss-%sillyver.tar.gz
BuildRequires:  gap-devel >= 4.11
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
Requires:       gap-core >= 4.11.1
Suggests:       gap-gapdoc >= 1.0

%description
The GAP Gauss package provides algorithms to compute reduced row
echelon forms (RREF) of a matrix.

%prep
%autosetup -n Gauss-%sillyver

%build
./configure "%gapdir"
%make_build
rm -v doc/clean
find . -type f -name ".*" -print -delete

%install
%gappkg_simple_install
rm -Rf "%buildroot/$moddir/src"

%files -f %name.files

%changelog
