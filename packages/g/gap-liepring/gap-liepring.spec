#
# spec file for package gap-liepring
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


Name:           gap-liepring
Version:        2.8
Release:        0
Summary:        GAP: Database and algorithms for Lie p-rings
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/liepring/
#Git-Clone:     https://github.com/gap-packages/liepring
Source:         https://github.com/gap-packages/liepring/releases/download/v%version/liepring-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-liering >= 2.1
Requires:       gap-singular >= 10

%description
LiePRing is a GAP4 package for access to the nilpotent Lie rings of
order p^n for p>2 and n<=7.

%prep
%autosetup -n liepring-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
