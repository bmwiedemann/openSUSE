#
# spec file for package gap-irredsol
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


Name:           gap-irredsol
Version:        1.4.4
Release:        0
Summary:        GAP: Library of irreducible soluble linear groups over finite fields
License:        BSD-2-Clause
Group:          Productivity/Scientific/Math
URL:            http://www.icm.tu-bs.de/~bhoeflin/irredsol/
#Git-Clone:     https://github.com/bh11/irredsol
Source:         https://github.com/bh11/irredsol/releases/latest/download/irredsol-%version.tar.bz2
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Suggests:       gap-crisp >= 1.3

%description
IRREDSOL provides a library of irreducible soluble linear groups over
finite fields and of finite primivite soluble groups.

%prep
%autosetup -n irredsol-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
