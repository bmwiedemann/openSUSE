#
# spec file for package gap-rds
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


Name:           gap-rds
Version:        1.8
Release:        0
Summary:        GAP: A package for searching relative difference sets
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/rds/
#Git-Clone:     https://github.com/gap-packages/rds
Source:         https://github.com/gap-packages/rds/releases/download/v%version/rds-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-design >= 1.3
Suggests:       gap-autpgrp >= 1.0

%description
RDS is a package for the search for relative difference set in
(nonabelian) finite groups.

%prep
%autosetup -n rds-%version

%build
find . -name .DS_Store -exec rm -Rf "{}" "+"

%install
%gappkg_simple_install

%files -f %name.files

%changelog
