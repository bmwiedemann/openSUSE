#
# spec file for package gap-polymaking
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-polymaking
Version:        0.8.8
Release:        0
Summary:        GAP: Interfacing the geometry software polymake
License:        GPL-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/polymaking/
#Git-Clone:     https://github.com/gap-packages/polymaking
Source:		https://github.com/gap-packages/polymaking/releases/download/v%version/polymaking-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
BuildArch:      noarch
Requires:       gap-core >= 4.8
Requires:       polymake
Suggests:       gap-gapdoc >= 0.99

%description
A very basic GAP-interface to the program "polymake" by Ewgenij
Gawrilow and Michael Joswi.

%prep
%autosetup -n polymaking-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
