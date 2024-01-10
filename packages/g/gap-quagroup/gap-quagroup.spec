#
# spec file for package gap-quagroup
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


Name:           gap-quagroup
Summary:        GAP: a package for doing computations with quantum groups
Version:        1.8.3
Release:        0
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/quagroup/
#Git-Clone:     https://github.com/gap-packages/quagroup
Source:         https://github.com/gap-packages/quagroup/releases/download/v%version/quagroup-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
The package QuaGroup contains functionality for working with
quantized enveloping algebras of finite-dimensional semisimple Lie
algebras.

%prep
%autosetup -n quagroup-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
