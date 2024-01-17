#
# spec file for package gap-aclib
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


Name:           gap-aclib
Version:        1.3.2
Release:        0
Summary:        GAP: Almost Crystallographic Groups
License:        Artistic-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/aclib/
#Git-Clone:     https://github.com/gap-packages/aclib
Source:         https://github.com/gap-packages/aclib/releases/download/v%version/aclib-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7
Requires:       gap-polycyclic >= 1.0
Suggests:       gap-crystcat >= 1.1

%description
The AClib package contains a library of almost crystallographic
groups and a some algorithms to compute with these groups. A group is
called almost crystallographic if it is finitely generated
nilpotent-by-finite and has no non-trivial finite normal subgroups.

%prep
%autosetup -n aclib-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
