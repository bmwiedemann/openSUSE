#
# spec file for package gap-liering
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


Name:           gap-liering
Version:        2.4.2
Release:        0
Summary:        GAP: finitely presented Lie rings
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/liering/
#Git-Clone:     https://github.com/gap-packages/liering
Source:         https://github.com/gap-packages/liering/releases/download/v2.4.2/liering-2.4.2.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
A GAP4 package containing functions for constructing Lie rings, and
working with them. The main functionality of interest concerns:

* Constructing finitely-presented Lie rings.
* Performing the Lazard correspondence.
* A small database of "largest" n-Engel Lie rings.

%prep
%autosetup -n liering-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
