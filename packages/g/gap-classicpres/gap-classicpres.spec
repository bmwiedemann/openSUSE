#
# spec file for package gap-classicpres
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


Name:           gap-classicpres
Version:        1.22
Release:        0
Summary:        GAP: Classical Group Presentations
License:        GPL-2.0 or GPL-3.0
Group:          Productivity/Scientific/Math
URL:            https://www.math.colostate.edu/~hulpke/classicpres/
#Git-Clone:	https://github.com/hulpke/magmapresentations/
Source:         http://www.math.colostate.edu/~hulpke/classicpres/classicpres%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11
Requires:       gap-atlasrep >= 1.4.0

%description
This GAP module is a translation of the `ClassicalStandardPresentation`
code from Magma.

%prep
%autosetup -n classicpres

%build

%install
%gappkg_simple_install
pushd "%buildroot/$moddir/"
popd

%files -f %name.files

%changelog
