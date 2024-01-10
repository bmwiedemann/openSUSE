#
# spec file for package gap-hecke
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


Name:           gap-hecke
Version:        1.5.3
Release:        0
Summary:        GAP: Hecke - Specht 2.4 ported to GAP 4
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/hecke/

Source:         https://github.com/gap-packages/hecke/releases/download/v%version/hecke-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
The Hecke package provides functions for calculating decomposition
matrices of Hecke algebras of the symmetric groups and q-Schur
algebras.

%prep
%autosetup -n hecke-%version -p1

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
