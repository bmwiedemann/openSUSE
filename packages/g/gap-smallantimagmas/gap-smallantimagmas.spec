#
# spec file for package gap-smallantimagmas
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


Name:           gap-smallantimagmas
Version:        0.3.0
Release:        0
Summary:        GAP: A library of antiassociative magmas of small order
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://limakzi.github.io/smallantimagmas/
#Git-Clone:     https://github.com/limakzi/smallantimagmas
Source:         https://github.com/limakzi/smallantimagmas/releases/download/v%version/smallantimagmas-v%version.tar.gz
BuildRequires:  gap-devel >= 4.12
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.5

%description
The smallantimagmas package classifies all finite, antiassociative magmas.

%prep
%autosetup -n smallantimagmas-v%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
