#
# spec file for package gap-gradedmodules
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gap-gradedmodules
Version:        2022.09.02
%define sillyver 2022.09-02
Release:        0
Summary:        GAP: Abelian finitely presented graded modules over a computable graded ring
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/GradedModules
#Git-Clone:     https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/GradedModules-%sillyver/GradedModules-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-gradedringforhomalg >= 2021.03.01
Requires:       gap-homalg >= 2022.02.01
Requires:       gap-homalgtocas >= 2011.10.05
Requires:       gap-matricesforhomalg >= 2022.02.01
Requires:       gap-modules >= 2022.02.01
Requires:       gap-ringsforhomalg >= 2020.04.17
Requires:       gap-toolsforhomalg >= 2014.12.08

%description
This homalg based package realizes the computability of the Abelian
category of finitely presented graded modules over a computable
graded ring.

%prep
%autosetup -n GradedModules-%sillyver

%build
rm -v doc/clean

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
