#
# spec file for package gap-kan
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gap-kan
Version:        1.34
Release:        0
Summary:        GAP: double coset rewriting systems
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/kan/
#Git-Clone:     https://github.com/gap-packages/kan
Source:         https://github.com/gap-packages/kan/releases/download/v%version/kan-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-automata >= 1.14
Requires:       gap-core >= 4.11
Requires:       gap-gapdoc >= 1.6.2
Requires:       gap-kbmag >= 1.5.9

%description
This package was conceived for computing induced actions of
categories. This version only deals with deouble coset rewriting
systems for finitely presented groups.

%prep
%autosetup -n kan-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
