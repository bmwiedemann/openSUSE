#
# spec file for package gap-unipot
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


Name:           gap-unipot
Version:        1.5
Release:        0
Summary:        GAP: Elements of unipotent subgroups of Chevalley groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/unipot/
#Git-Clone:     https://github.com/gap-packages/unipot
Source:         https://github.com/gap-packages/unipot/releases/download/v%version/unipot-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7

%description
Tools for computing with elements of unipotent subgroups of Chevalley groups.

%prep
%autosetup -n unipot-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
