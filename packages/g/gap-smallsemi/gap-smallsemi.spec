#
# spec file for package gap-smallsemi
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


Name:           gap-smallsemi
Version:        0.7.0
Release:        0
Summary:        GAP data library of semigroups of small size
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/smallsemi/
#Git-Clone:     https://github.com/gap-packages/smallsemi
Source:         https://github.com/gap-packages/smallsemi/releases/download/v%version/smallsemi-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gzip

%description
The "Smallsemi" package is a data library of semigroups of small
size. It provides all semigroups with at most 8 elements as well as
various information about these objects. The reason that semigroups
of higher orders are not included is the huge number of such objects.
(The number of semigroups of size 10 is not even known at the time of
writing.)

%prep
%autosetup -n smallsemi-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
