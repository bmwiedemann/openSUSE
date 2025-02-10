#
# spec file for package gap-loops
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gap-loops
Version:        3.4.4
Release:        0
Summary:        GAP: Computing with quasigroups and loops in GAP
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/loops/
#Git-Clone:     https://github.com/gap-packages/loops
Source:         https://github.com/gap-packages/loops/releases/download/v%version/loops-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
Requires:       gap-core >= 4.8

%description
The LOOPS package provides researchers in nonassociative algebra with
a computational tool that integrates standard notions of loop theory
with libraries of loops and group-theoretical algorithms of GAP. The
package also expands GAP toward nonassociative structures.

%prep
%autosetup -n loops-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
