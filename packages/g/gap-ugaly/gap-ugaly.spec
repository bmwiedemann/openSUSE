#
# spec file for package gap-ugaly
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


Name:           gap-ugaly
Version:        4.1.3
Release:        0
Summary:        GAP: Universal Groups Acting LocallY
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/UGALY
#Git-Clone:     https://github.com/gap-packages/UGALY
Source:         https://github.com/gap-packages/UGALY/releases/download/v%version/UGALY-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10.2
Requires:       gap-fga >= 1.0

%description
UGALY (Universal Groups Acting LocallY) is a GAP package that
provides methods to create, analyse and find local actions of
generalised universal groups acting on locally finite regular trees,
following Burger-Mozes and Tornier.

%prep
%autosetup -n UGALY-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
