#
# spec file for package gap-localizeringforhomalg
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


Name:           gap-localizeringforhomalg
Version:        2022.11.01
%define sillyver 2022.11-01
Release:        0
Summary:        GAP: A Package for Localization of Polynomial Rings
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/LocalizeRingForHomalg
#Git-Clone:	https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/LocalizeRingForHomalg-%sillyver/LocalizeRingForHomalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-homalgtocas >= 2020.06.27
Requires:       gap-matricesforhomalg >= 2020.06.27
Requires:       gap-modules >= 2020.02.05

%description
This package is part of the homalg project and allows localization of
a (computable) commutative ring at a (finitely generated) maximal
ideal.

%prep
%autosetup -n LocalizeRingForHomalg-%sillyver

%build
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
