#
# spec file for package gap-corelg
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


Name:           gap-corelg
Version:        1.56
Release:        0
Summary:        GAP: computation with real Lie groups
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            http://users.monash.edu/~heikod/corelg/README
Source:         https://github.com/gap-packages/corelg/releases/download/v%version/corelg-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.4
Requires:       gap-sla >= 0.14
Suggests:       gap-gapdoc >= 1.0

%description
The CoReLG package contains functionality for working with real
semisimple Lie algebras.

%prep
%autosetup -n corelg-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
