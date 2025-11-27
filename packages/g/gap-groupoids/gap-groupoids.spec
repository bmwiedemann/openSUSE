#
# spec file for package gap-groupoids
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


Name:           gap-groupoids
Version:        1.81
Release:        0
Summary:        GAP: Groupoids, graphs of groups, and graphs of groupoids
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/groupoids/
#Git-Clone:     https://github.com/gap-packages/groupoids
Source:         https://github.com/gap-packages/groupoids/releases/download/v%version/groupoids-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10.1
Requires:       gap-fga >= 1.4.0
Requires:       gap-utils >= 0.76
Suggests:       gap-semigroups >= 3.1.1

%description
This package allows for the computation of finite groupoids, both
connected and with several components. Graphs of groups and graphs of
groupoids are also constructed, allowing the calculation of normal
forms for Free Products with Amalgamation and for HNN extensions when
the initial groups have rewriting systems.

%prep
%autosetup -n groupoids-%version

%build

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
