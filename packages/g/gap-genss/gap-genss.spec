#
# spec file for package gap-genss
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gap-genss
Version:        1.6.9
Release:        0
Summary:        GAP: generic Schreier-Sims
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://gap-packages.github.io/genss/
#Git-Clone:     https://github.com/gap-packages/genss
Source:         https://github.com/gap-packages/genss/releases/download/v%version/genss-%version.tar.bz2
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Requires:       gap-gapdoc >= 1.5
Requires:       gap-orb >= 4.5
Recommends:     gap-io >= 4.2

%description
The genss package implements the randomised Schreier-Sims algorithm
to compute a stabilizer chain and a base and strong generating set
for arbitrary finite groups.

%prep
%autosetup -n genss-%version

%build
# rpmlint (no +x bit present)
rm -v doc/clean

%install
rm -Rf scripts
%gappkg_simple_install

%files -f %name.files

%changelog
