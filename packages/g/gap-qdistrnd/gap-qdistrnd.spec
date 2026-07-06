#
# spec file for package gap-qdistrnd
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


Name:           gap-qdistrnd
Version:        0.9.5
Release:        0
Summary:        GAP: Q-ary quantum stabilizer code distance
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://qec-pages.github.io/QDistRnd/
#Git-Clone:     https://github.com/QEC-pages/QDistRnd
Source:         https://github.com/QEC-pages/QDistRnd/releases/download/v%version/qdistrnd-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11
Requires:       gap-autodoc >= 1.5
Requires:       gap-gapdoc >= 1.5
Requires:       gap-guava >= 3.14

%description
QDistRnd implements a probabilistic algorithm for finding the minimum distance
of a quantum code linear over a finite field GF(q).

%prep
%autosetup -n qdistrnd-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
