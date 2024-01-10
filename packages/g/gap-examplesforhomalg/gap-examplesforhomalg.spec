#
# spec file for package gap-examplesforhomalg
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gap-examplesforhomalg
Version:        2022.11.01
%define sillyver 2022.11-01
Release:        0
Summary:        GAP: Examples for the homalg GAP Package
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/ExamplesForHomalg
#Git-Clone:     https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/ExamplesForHomalg-%sillyver/ExamplesForHomalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11.1
Requires:       gap-gapdoc >= 1.1
Requires:       gap-gaussforhomalg >= 2019.09.01
Requires:       gap-homalg >= 2015.06.01
Requires:       gap-homalgtocas >= 2011.08.25
Requires:       gap-matricesforhomalg >= 2020.05.09
Requires:       gap-modules >= 2020.05.09
Requires:       gap-ringsforhomalg >= 2021.10.01

%description
The ExamplesForHomalg package provides example scripts for the homalg
package that can be used with several computer algebra systems.

%prep
%autosetup -n ExamplesForHomalg-%sillyver
rm -v doc/clean

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
