#
# spec file for package gap-thelma
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


Name:           gap-thelma
Version:        1.3
Release:        0
Summary:        GAP: THreshold ELements, Modeling and Applications
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/Thelma
#Git-Clone:     https://github.com/gap-packages/Thelma
Source:         https://github.com/gap-packages/Thelma/releases/download/v%version/Thelma-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10
Requires:       gap-gapdoc >= 1.5
Requires:       gap-gauss >= 2018.09.08

%description
The Thelma package is package with algorithms to deal with threshold elements.

%prep
%autosetup -n Thelma-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
