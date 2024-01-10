#
# spec file for package gap-sla
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


Name:           gap-sla
Version:        1.5.3
Release:        0
Summary:        GAP: Computations with simple Lie algebras
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/sla/
#Git-Clone:     https://github.com/gap-packages/sla
Source:         https://github.com/gap-packages/sla/releases/download/v%version/sla-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
Requires:       gap-core >= 4.8
Requires:       gap-quagroup >= 1.8

%description
The package SLA contains functionality for working with simple Lie algebras.

%prep
%autosetup -n sla-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
