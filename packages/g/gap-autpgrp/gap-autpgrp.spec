#
# spec file for package gap-autpgrp
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


Name:           gap-autpgrp
Version:        1.11
Release:        0
Summary:        GAP: Computing the Automorphism Group of a p-Group
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/autpgrp/

Source:         https://github.com/gap-packages/autpgrp/releases/download/v%version/autpgrp-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildArch:      noarch
Requires:       gap-core >= 4.4

%description
The AutPGrp package introduces a new function to compute the
automorphism group of a finite $p$-group. The underlying algorithm is
a refinement of the methods described in O'Brien (1995). In
particular, this implementation is more efficient in both time and
space requirements and hence has a wider range of applications than
the ANUPQ method.

%prep
%autosetup -n autpgrp-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
