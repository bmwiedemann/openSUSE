#
# spec file for package gap-intpic
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gap-intpic
Version:        0.4.0
Release:        0
Summary:        GAP: package for drawing integers
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/intpic
#Git-Clone:     https://github.com/gap-packages/intpic
Source:         https://github.com/gap-packages/intpic/releases/download/v%version/IntPic-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7
Requires:       gap-gapdoc >= 1.5
Requires:       gap-numericalsgps >= 1.0

%description
The IntPic package, is a package for drawing integers, by emphasizing
some subsets.

%prep
%autosetup -n IntPic-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
