#
# spec file for package gap-repsn
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


Name:           gap-repsn
Version:        3.1.2
Release:        0
Summary:        GAP: Finite group representation construction
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/repsn/
#Git-Clone:     https://github.com/gap-packages/repsn
Source:         https://github.com/gap-packages/repsn/releases/download/v%version/repsn-%version.tar.gz
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
The package provides GAP functions for computing characteristic zero
matrix representations of finite groups.

%prep
%autosetup -n repsn-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
