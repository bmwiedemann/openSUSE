#
# spec file for package gap-recog
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gap-recog
Version:        1.4.4
Release:        0
Summary:        GAP: A collection of group recognition methods
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/recog/
#Git-Clone:     https://github.com/gap-packages/recog
Source:         https://github.com/gap-packages/recog/releases/download/v%version/recog-%version.tar.bz2
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-atlasrep >= 1.4.0
Requires:       gap-core >= 4.11
Requires:       gap-factint >= 1.5.2
Requires:       gap-forms >= 1.2
Requires:       gap-genss >= 1.3
Requires:       gap-orb >= 3.4
Conflicts:      gap-recogbase

%description
This packages contains a collection of methods for the constructive
recognition of groups. It is mostly intended for permutation groups,
matrix groups and projective groups.

%prep
%autosetup -n recog-%version

%build
chmod a-x misc/bbox/*.g
rm -v doc/clean
perl -i -lpe 's{^#!/usr/bin/env py\w+}{#!/usr/bin/python3}' misc/bbox/bbtogap.py

%install
%gappkg_simple_install

%files -f %name.files

%changelog
