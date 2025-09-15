#
# spec file for package gap-xgap
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


Name:           gap-xgap
Version:        4.33
Release:        0
Summary:        GAP: Graphical user interface for GAP
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/xgap/
#Git-Clone:     https://github.com/gap-packages/xgap
Source:         https://github.com/gap-packages/xgap/releases/download/v%version/xgap-%version.tar.gz
Patch1:         gcc14.patch
BuildRequires:  c_compiler
BuildRequires:  fdupes
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
Requires:       gap-core >= 4.7

%description
The XGAP package allows to use graphics in GAP.

%prep
%autosetup -n xgap-%version -p1

%build
./configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
cd "%buildroot/$moddir"
rm -Rfv configure config.* bin/*/config.* bin/*/configure cnf src.x11
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
