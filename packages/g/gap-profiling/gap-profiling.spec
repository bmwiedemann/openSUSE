#
# spec file for package gap-profiling
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


Name:           gap-profiling
Version:        2.6.2
Release:        0
Summary:        GAP: Line-by-line profiling and code coverage for GAP
License:        CDDL-1.0 AND MIT
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/profiling/
#Git-Clone:     https://github.com/gap-packages/profiling
Source:         https://github.com/gap-packages/profiling/releases/download/v%version/profiling-%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  gap-devel >= 4.12
BuildRequires:  gap-rpm-devel
BuildRequires:  python-rpm-macros
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.5
Requires:       gap-io >= 4.4.4

%description
Line by line profiling and code coverage for GAP.

%prep
%autosetup -n profiling-%version -p1

%build
./configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
rm -Rf "%buildroot/$moddir/src"
%python3_fix_shebang_path %buildroot/%_libdir/gap/pkg/profiling-%version/FlameGraph/*

%files -f %name.files

%changelog
