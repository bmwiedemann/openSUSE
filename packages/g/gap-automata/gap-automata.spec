#
# spec file for package gap-automata
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gap-automata
Version:        1.16
Release:        0
Summary:        GAP: A package on automata
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/automata/
#Git-Clone:     https://github.com/gap-packages/automata
Source:         https://github.com/gap-packages/automata/releases/download/v%version/automata-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
Requires:       gap-core >= 4.8
Requires:       graphviz
Suggests:       gap-gapdoc >= 1.2

%description
The features of this package include

* Computing a rational expression for the language recognized by a
  finite automaton;
* Compute an automaton for the language given by a rational
  expression;
* Minimalize a finite automaton;
* Has some features (using the external program GraphViz) to
  visualize automata;

%prep
%autosetup -n automata-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
