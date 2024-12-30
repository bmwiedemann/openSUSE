#
# spec file for package gap-modisom
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


Name:           gap-modisom
Version:        3.0.1
Release:        0
Summary:        GAP: Computing with nilpotent associative algebras
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/modisom/
#Git-Clone:	https://github.com/gap-packages/modisom
Source:         https://github.com/gap-packages/modisom/releases/download/v%version/modisom-%version.tar.gz
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7
Requires:       gap-polycyclic >= 1.0

%description
ModIsom is a GAP package containing various methods for computing
with nilpotent associative algebras. It has a method to determine the
automorphism group and to test isomorphis of such algebras over
finite fields and of modular group algebras of finite p-groups, and
it contains a nilpotent quotient algorithm for finitely presented
associative algebras and a method to determine Kurosh algebras.

%prep
%autosetup -n modisom-%version

%build

%install
%gappkg_simple_install
pushd "%buildroot/$moddir/"
popd

%files -f %name.files

%changelog
