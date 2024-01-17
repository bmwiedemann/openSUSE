#
# spec file for package gap-difsets
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


Name:           gap-difsets
Version:        2.3.1
Release:        0
Summary:        GAP: Algorithm for enumerating all difference sets in a group
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://dylanpeifer.github.io/difsets/
#Git-Clone:	https://github.com/dylanpeifer/difsets
Source:         https://github.com/dylanpeifer/difsets/releases/download/v%version/difsets-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Requires:       gap-gapdoc >= 1.5
Requires:       gap-grape >= 4.7
Suggests:       gap-smallgrp >= 1.3

%description
The DifSets package is a GAP package implementing an algorithm for
enumerating all difference sets up to equivalence in a group.

%prep
%autosetup -n difsets-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
