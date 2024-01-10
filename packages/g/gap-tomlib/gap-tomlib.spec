#
# spec file for package gap-tomlib
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


Name:           gap-tomlib
Version:        1.2.9
Release:        0
Summary:        GAP: Library of Tables of Marks
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/tomlib
#Git-Clone:     https://github.com/gap-packages/tomlib
Source:         https://github.com/gap-packages/tomlib/releases/download/v%version/tomlib-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.4
Requires:       gap-atlasrep >= 1.5
Suggests:       gap-ctbllib >= 1.1

%description
The package contains the GAP Library of Tables of Marks.

%prep
%autosetup -n tomlib-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
