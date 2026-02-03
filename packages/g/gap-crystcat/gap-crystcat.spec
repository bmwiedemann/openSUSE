#
# spec file for package gap-crystcat
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gap-crystcat
Version:        1.1.11
Release:        0
Summary:        GAP: The crystallographic groups catalog
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php#CrystCat
Source:         https://www.math.uni-bielefeld.de/~gaehler/gap/CrystCat/crystcat-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
Requires:       gap-core >= 4.5
Requires:       gap-cryst >= 4.1.8

%description
CrystCat provides a catalog of crystallographic groups of dimensions
2, 3, and 4, which covers most of the data contained in the book
"Crystallographic groups of four-dimensional space" by H. Brown, R.
Bülow, J. Neubüser, H. Wondratschek, and H. Zassenhaus (John Wiley,
New York, 1978).

%prep
%autosetup -n crystcat

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
