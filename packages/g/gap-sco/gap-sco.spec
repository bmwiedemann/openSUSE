#
# spec file for package gap-sco
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


Name:           gap-sco
Version:        2022.09.01
%define sillyver 2022.09-01
Release:        0
Summary:        GAP: Simplicial Cohomology of Orbifolds
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/SCO
Source:         https://github.com/homalg-project/homalg_project/releases/download/SCO-%sillyver/SCO-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-matricesforhomalg >= 2011.08.10
Requires:       gap-modules >= 2011.06.29

%description
The SCO package provides functionality to compute simplicial
cohomology of orbifolds.

%prep
%autosetup -n SCO-%sillyver

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
