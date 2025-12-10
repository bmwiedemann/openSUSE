#
# spec file for package gap-xmod
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gap-xmod
Version:        2.97
Release:        0
Summary:        GAP: Crossed Modules and Cat1-Groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/xmod/
#Git-Clone:     https://github.com/gap-packages/xmod
Source:         https://github.com/gap-packages/xmod/releases/download/v%version/XMod-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-autpgrp >= 1.10.2
Requires:       gap-core >= 4.11
Requires:       gap-groupoids >= 1.78
Requires:       gap-hap >= 1.29
Requires:       gap-smallgrp >= 1.4.2
Requires:       gap-utils >= 0.81

%description
The XMod package provides a collection of functions for computing
with crossed modules and cat1-groups, their derivations and sections,
morphisms of these structures, and higher-dimensional
generalisations.

%prep
%autosetup -n XMod-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
