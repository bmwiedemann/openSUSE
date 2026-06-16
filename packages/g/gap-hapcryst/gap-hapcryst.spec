#
# spec file for package gap-hapcryst
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


Name:           gap-hapcryst
Version:        0.2.0
Release:        0
Summary:        GAP: A HAP extension for crytallographic groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/hapcryst/
#Git-Clone:     https://github.com/gap-packages/hapcryst
Source:         https://github.com/gap-packages/hapcryst/releases/download/v%version/hapcryst-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-aclib >= 1.1
Requires:       gap-core >= 4.12
Requires:       gap-cryst >= 4.1.5
Requires:       gap-hap >= 1.8
Requires:       gap-polycyclic >= 2.8.1
Requires:       gap-polymaking >= 0.8.6
Requires:       polymake
Suggests:       gap-carat >= 1.1
Suggests:       gap-crystcat >= 1.1.2
Suggests:       gap-gapdoc >= 0.99

%description
This package is an add-on for Graham Ellis's HAP package. HAPcryst
implements some functions for crystallographic groups (namely
OrbitStabilizer-type methods). It is also capable of calculating free
resolutions for Bieberbach groups.

This is an extension to the HAP package by Graham Ellis. It implements
geometric methods for the calculation of resolutions of Bieberbach groups.

%prep
%autosetup -n hapcryst-%version

%build
find . -type f -name "*~" -delete

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
