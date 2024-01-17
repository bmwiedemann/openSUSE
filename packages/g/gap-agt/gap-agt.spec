#
# spec file for package gap-agt
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


Name:           gap-agt
Version:        0.2
Release:        0
Summary:        GAP: Algebraic Graph Theory
License:        Artistic-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/agt/

Source:         https://github.com/gap-packages/AGT/releases/download/v%version/AGT-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10
Requires:       gap-design >= 1.7
Requires:       gap-digraphs >= 0.15.2
Requires:       gap-gapdoc >= 1.6
Requires:       gap-grape >= 4.8

%description
The AGT package contains a methods used for the determination of
various algebraic and regularity properties of graphs, as well as
certain substructures of graphs. The package also contains a library
of strongly regular graphs, intended to be a resource for
computational experiments.

%prep
%autosetup -n AGT-%version
# duh
find . -type f -name "*.swp" -print -delete

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
