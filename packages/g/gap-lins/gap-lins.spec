#
# spec file for package gap-lins
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


Name:           gap-lins
Version:        0.9
Release:        0
Summary:        GAP: Algorithm for computing the normal subgroups of a finitely presented group
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://gap-packages.github.io/lins/
#Git-Clone:     https://github.com/gap-packages/lins
Source:         https://github.com/gap-packages/lins/releases/download/v%version/LINS-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12

%description
This package provides an algorithm for computing the normal
subgroups of a finitely presented group up to some given index
bound.

%prep
%autosetup -n LINS-%version

%build

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
