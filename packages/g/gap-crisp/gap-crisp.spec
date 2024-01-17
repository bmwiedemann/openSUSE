#
# spec file for package gap-crisp
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


Name:           gap-crisp
Version:        1.4.6
Release:        0
Summary:        GAP: Computing with Radicals, Injectors, Schunck classes and Projectors
License:        BSD-2-Clause
Group:          Productivity/Scientific/Math
URL:            https://github.com/bh11/crisp
Source:         https://github.com/bh11/crisp/archive/refs/tags/CRISP-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
Requires:       gap-core >= 4.5

%description
The GAP package "CRISP" provides algorithsmf roc omputing subgroups
of finite solvable groups related to a group class 'C'. In
particular, it allows to compute 'C' radicals and 'C'-injectors for
Fitting (and Fitting sets) 'C', 'C'-residuals for formations 'C', and
'C'-projectors for Schunck classes 'C'.

Moreover, CRISP contains algorithms for the computation of normal
subgroups invariant under a prescribed set of automorphisms and
belonging to a given group class.

%prep
%autosetup -n crisp-CRISP-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
