#
# spec file for package gap-transgrp
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


Name:           gap-transgrp
Version:        3.6.5
Release:        0
Summary:        GAP: Transitive Groups Library
License:        Artistic-2.0 AND GPL-2.0-only AND GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            http://www.math.colostate.edu/~hulpke/transgrp

Source:         https://www.math.colostate.edu/~hulpke/transgrp/transgrp%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9

%description
The TransGrp package provides the library of transitive groups.

%prep
%setup -qn transgrp

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
