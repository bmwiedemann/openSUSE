#
# spec file for package gap-resclasses
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


Name:           gap-resclasses
Version:        4.7.3
Release:        0
Summary:        GAP: Set-Theoretic Computations with Residue Classes
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/resclasses/
#Git-Clone:     https://github.com/gap-packages/resclasses
Source:         https://github.com/gap-packages/resclasses/releases/download/v%version/resclasses-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8.7
Requires:       gap-gapdoc >= 1.5.1
Requires:       gap-polycyclic >= 2.11
Requires:       gap-utils >= 0.40
Suggests:       gap-io >= 4.4.5

%description
ResClasses is a package for set-theoretic computations with residue
classes of the integers and a couple of other rings. The class of
sets which ResClasses can deal with includes the open and the closed
sets in the topology on the respective ring which is induced by
taking the set of all residue classes as a basis, as far as the usual
restrictions imposed by the finiteness of computing resources permit
this.

%prep
%autosetup -n resclasses-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
