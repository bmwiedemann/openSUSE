#
# spec file for package gap-repndecomp
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


Name:           gap-repndecomp
Version:        1.2.1
Release:        0
Summary:        GAP: Decomposition of finite groups reprensentations into irreducibles
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/RepnDecomp/
#Git-Clone:     https://github.com/gap-packages/RepnDecomp
Source:         https://github.com/gap-packages/RepnDecomp/releases/download/v%version/RepnDecomp-%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10
Requires:       gap-gapdoc >= 1.6.1
Requires:       gap-grape >= 4.8.1
Suggests:       gap-io >= 4.7.0

%description
The RepnDecomp package provides functions implementing various
algorithms for decomposing linear representations of finite groups.

%prep
%autosetup -n RepnDecomp-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
