#
# spec file for package gap-modules
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


Name:           gap-modules
Version:        2022.11.01
%define sillyver 2022.11-01
Release:        0
Summary:        GAP: Abelian Finitely Presented Modules over Computable Rings
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            http://homalg-project.github.io/homalg_project/Modules/

#Git-Clone:	git://github.com/homalg-project/Modules
#Git-Web:	https://github.com/homalg-project/Modules
Source:         https://github.com/homalg-project/homalg_project/releases/download/Modules-%sillyver/Modules-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-gaussforhomalg >= 2019.09.01
Requires:       gap-homalg >= 2022.02.01
Requires:       gap-matricesforhomalg >= 2022.02.01
Requires:       gap-toolsforhomalg >= 2013.04.12

%description
The Modules package provides ring independent homological algebra
functionality for the abelian category of finitely presented modules
over computable rings.

%prep
%autosetup -n Modules-%sillyver

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
