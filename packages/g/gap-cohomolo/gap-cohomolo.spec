#
# spec file for package gap-cohomolo
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gap-cohomolo
Version:        1.6.12
Release:        0
Summary:        GAP: Cohomology groups of finite groups on finite modules
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/cohomolo
Source:         https://github.com/gap-packages/cohomolo/releases/download/v%version/cohomolo-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7

%description
The cohomolo package is a GAP interface to some C programs for
computing Schur multipliers and covering groups of finite groups and
first and second cohomology groups of finite groups acting on finite
modules.

%prep
%autosetup -n cohomolo-%version

%build
find standalone/{README,info.d} -type f -exec chmod a-x "{}" "+"
./configure "%gapdir"
%make_build CFLAGS="-O2 -g"

%install
%gappkg_simple_install
rm -Rf "%buildroot/$moddir/standalone/progs.d"
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
