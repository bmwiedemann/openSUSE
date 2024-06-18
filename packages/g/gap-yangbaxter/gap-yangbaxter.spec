#
# spec file for package gap-yangbaxter
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


Name:           gap-yangbaxter
Version:        0.10.5
Release:        0
Summary:        GAP: Combinatorial Solutions for the Yang-Baxter equation
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/YangBaxter
#Git-Clone:     https://github.com/gap-packages/YangBaxter
Source:         https://github.com/gap-packages/YangBaxter/releases/download/v%version/YangBaxter-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Requires:       gap-cryst >= 4.0

%description
The YangBaxter package provides functionality to construct classical
and skew braces. It also includes a database of classical and skew
braces of small orders.

%prep
%autosetup -n YangBaxter-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
