#
# spec file for package gap-fwtree
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-fwtree
Version:        1.3
Release:        0
Summary:        GAP: Computation of trees related to some pro-p-groups of finite width
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/fwtree/
#Git-Clone:     https://github.com/gap-packages/fwtree
Source:         https://github.com/gap-packages/fwtree/releases/download/v1.3/fwtree-1.3.tar.gz
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.4
Requires:       gap-anupq >= 1.0
Requires:       gap-autpgrp >= 1.0
Requires:       gap-polycyclic >= 1.0
Suggests:       gap-xgap >= 1.0

%description
The fwtree package contains some code related to the computation
of trees corresponding to some groups of finite rank, width and
obliquity.

%prep
%autosetup -n fwtree-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
