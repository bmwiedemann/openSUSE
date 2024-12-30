#
# spec file for package gap-4ti2interface
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


Name:           gap-4ti2interface
Version:        2024.11.01
%define sillyversion 2024.11-01
Release:        0
Summary:        GAP: Interface to 4ti2
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/homalg_project/4ti2Interface/
#Git-Clone:     https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/4ti2Interface-%sillyversion/4ti2Interface-%sillyversion.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       4ti2
Requires:       gap-core >= 4.12.1
Requires:       gap-io >= 4.2

%description
This package provides a GAP module to interface with 4ti2,
a collection of programs that compute and solve algebraic,
geometric and combinational problems on linear spaces.

%prep
%autosetup -n 4ti2Interface-%sillyversion

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
