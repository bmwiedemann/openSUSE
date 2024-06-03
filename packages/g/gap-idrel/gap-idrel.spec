#
# spec file for package gap-idrel
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


Name:           gap-idrel
Version:        2.47
Release:        0
Summary:        GAP: Identities among relations
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/idrel/
#Git-Clone:     https://github.com/gap-packages/idrel
Source:         https://github.com/gap-packages/idrel/releases/download/v%version/idrel-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11.1

%description
The IdRel package is designed for computing the identities among
relations of a group presentation using rewriting, logged rewriting,
monoid polynomials, module polynomials and Y-sequences.

%prep
%autosetup -n idrel-%version

%build

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
