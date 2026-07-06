#
# spec file for package gap-classicalmaximals
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gap-classicalmaximals
Version:        1.1
Release:        0
Summary:        GAP: Maximal subgroups of the classical quasisimple groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/ClassicalMaximals/
#Git-Clone:     https://github.com/gap-packages/ClassicalMaximals/
Source:         https://github.com/gap-packages/ClassicalMaximals/releases/download/v1.1/ClassicalMaximals-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.15
Requires:       gap-forms >= 1.2.12
Requires:       gap-recog >= 1.5.0

%description
The ClassicalMaximals function returns a list of the maximal
subgroups of the classical quasisimple groups in their natural
representations. The list should be complete for dimensions up to 17.
For larger dimensions, all maximal subgroups of geometric type are
returned, but not those of Type S (sometimes known as Class C9).

There are also options to return the normalisers of these subgroups
in various groups, such as (GL)(n, q), (CU)(n, q), that lie between
the quasisimple group and its normaliser in the general linear group.
These should be sufficient to enable the skilled user to determine
the maximal subgroups of any group lying between the quasisimple
groups and its normaliser.

%prep
%autosetup -n ClassicalMaximals-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
