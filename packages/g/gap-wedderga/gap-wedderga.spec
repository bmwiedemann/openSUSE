#
# spec file for package gap-wedderga
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gap-wedderga
Version:        4.11.3
Release:        0
Summary:        GAP: Wedderburn Decomposition of Group Algebras
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/wedderga/
#Git-Clone:     https://github.com/gap-packages/wedderga
Source:         https://github.com/gap-packages/wedderga/releases/download/v%version/wedderga-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-gapdoc >= 1.5.1
Suggests:       gap-guava >= 3.12
Suggests:       gap-laguna >= 3.4

%description
Wedderga is the package to compute the simple components of the
Wedderburn decomposition of semisimple group algebras of finite
groups over finite fields and over subfields of finite cyclotomic
extensions of the rational. It also contains functions that produce
the primitive central idempotents of semisimple group algebras. Other
functions of Wedderga allows to construct crossed products over a
group with coefficients in an associative ring with identity and the
multiplication determined by a given action and twisting.

%prep
%autosetup -n wedderga-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
