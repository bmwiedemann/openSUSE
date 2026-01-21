#
# spec file for package gap-ferret
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gap-ferret
Version:        1.0.16
Release:        0
Summary:        GAP: Backtrack Search in Permutation Groups
License:        MPL-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/ferret/
#Git-Clone:	https://github.com/gap-packages/ferret
Source:         https://github.com/gap-packages/ferret/releases/download/v%version/ferret-%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.5

%description
The Ferret package provides a C++ reimplementation of Jeffery Leon's Partition
Backtrack framework for solving problems in permutation groups

%prep
%autosetup -n ferret-%version

%build
%configure --with-gaproot="%gapdir"
%make_build
find . -type f -size 0 -name _Chunks.xml -print -delete

%install
%gappkg_simple_install
cd "%buildroot/$fmoddir/"
rm -Rf gap_cpp* src config.log
find YAPB++ -type f ! -name LICENSE -delete
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
