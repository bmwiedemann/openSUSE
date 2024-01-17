#
# spec file for package gap-openmath
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


Name:           gap-openmath
Version:        11.5.3
Release:        0
Summary:        GAP: OpenMath functionality in GAP
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/openmath/
#Git-Clone:     https://github.com/gap-packages/openmath
Source:         https://github.com/gap-packages/openmath/releases/download/v%version/OpenMath-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildArch:      noarch
Requires:       gap-core >= 4.9
Requires:       gap-gapdoc >= 1.6
Requires:       gap-io >= 4.5.1

%description
The package provides an OpenMath phrasebook for GAP: it allows GAP
users to import and export mathematical objects encoded in OpenMath,
for the purpose of exchanging them with other OpenMath-enabled
applications.

%prep
%autosetup -n OpenMath-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
