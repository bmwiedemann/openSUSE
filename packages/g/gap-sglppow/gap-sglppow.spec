#
# spec file for package gap-sglppow
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gap-sglppow
Version:        2.4
Release:        0
Summary:        GAP: Database of groups of prime-power order for some prime powers
License:        Artistic-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/sglppow/
#Git-Clone:     https://github.com/gap-packages/sglppow
Source:         https://github.com/gap-packages/sglppow/releases/download/v%version/sglppow-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
SglPPow is an extension to the GAP Small Groups Library; this package
gives access to the groups of order p^7 for primes p > 11, and to the
groups of order 3^8.

%prep
%autosetup -n sglppow-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
