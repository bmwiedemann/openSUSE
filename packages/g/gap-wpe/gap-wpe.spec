#
# spec file for package gap-wpe
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


Name:           gap-wpe
Version:        0.8
Release:        0
Summary:        GAP: Wreath Product Elements
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/io/
#Git-Clone:     https://github.com/gap-packages/WPE
Source:       	https://github.com/gap-packages/WPE/releases/download/v%version/WPE-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-devel >= 4.13
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
Requires:       gap-core >= 4.13

%description
WPE provides methods for working with Wreath Product Elements in the
GAP computer algebra system.

%prep
%autosetup -n WPE-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
