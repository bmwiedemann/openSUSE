#
# spec file for package gap-deepthought
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gap-deepthought
Version:        1.0.8
Release:        0
Summary:        GAP: Deep Thought for computations in nilpotent groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/DeepThought/
#Git-Clone:	https://github.com/gap-packages/DeepThought
Source:         https://github.com/gap-packages/DeepThought/releases/download/v%version/DeepThought-%version.tar.gz
BuildRequires:  c_compiler
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.5
Requires:       gap-polycyclic >= 2.11

%description
This package provides functions for multiplication and other
computations in finitely generated nilpotent groups based on the Deep
Thought algorithm.

%prep
%autosetup -n DeepThought-%version

%build
./configure "%gapdir"
%make_build
find . -type f -size 0 -name _Chunks.xml -print -delete

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
rm -Rf src
popd

%files -f %name.files

%changelog
