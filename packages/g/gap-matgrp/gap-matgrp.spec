#
# spec file for package gap-matgrp
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


Name:           gap-matgrp
Version:        0.71
Release:        0
Summary:        GAP: Matric group interface routines
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://www.math.colostate.edu/~hulpke/matgrp/
#Git-Clone:     https://github.com/hulpke/matgrp/
Source:         http://www.math.colostate.edu/~hulpke/matgrp/matgrp%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-atlasrep >= 1.4.0
Requires:       gap-core >= 4.12
Requires:       gap-forms >= 1.2
Requires:       gap-genss >= 1.3
Requires:       gap-orb >= 3.4
Requires:       gap-recog >= 1.2

%description
The matgrp package provides an interface to the solvable radical
functionality for matrix groups, building on constructive
recognition.

%prep
%autosetup -n matgrp

%build
find doc -type f -name ".*" -print -delete

%install
%gappkg_simple_install

%files -f %name.files

%changelog
