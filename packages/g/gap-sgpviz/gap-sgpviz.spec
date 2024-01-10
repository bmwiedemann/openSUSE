#
# spec file for package gap-sgpviz
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gap-sgpviz
Version:        0.999.5
Release:        0
Summary:        GAP: A package for semigroup visualization
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/sgpviz
#Git-Clone:     https://github.com/gap-packages/sgpviz
Source:         https://github.com/gap-packages/sgpviz/releases/download/v%version/SgpViz-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-automata >= 1.14
Requires:       gap-core >= 4.4

%description
The SgpViz package, is a package with some visualization functions
for semigroups. The features of this package include:

* drawing the D-Classes of a semigroup and the D-Class of an element
  of a semigroup
* computing a minimal factorization of an element of semigroup in the
  generators
* drawing the Schutzenberger graphs of an inverse semigroup
* computing the right Cayley graph of a semigroup
* a Tcl/Tk interface to specify a semigroup

%prep
%autosetup -n SgpViz-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
