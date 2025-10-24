#
# spec file for package gap-alco
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


Name:           gap-alco
Version:        1.1.2
Release:        0
Summary:        GAP: Algebraic Combinatorics
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://bnasmith.github.io/alco/
#Git-Clone:     https://github.com/BNasmith/alco
Source:         https://github.com/BNasmith/alco/releases/download/v%version/ALCO-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.14
Requires:       gap-resclasses >= 4.7.3

%description
The ALCO package provides tools for algebraic combinatorics including
implementations of octonion and Jordan algebras.

%prep
%autosetup -n ALCO-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
