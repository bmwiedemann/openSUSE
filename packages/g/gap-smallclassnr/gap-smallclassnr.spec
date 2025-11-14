#
# spec file for package gap-smallclassnr
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gap-smallclassnr
Version:        1.4.3
Release:        0
Summary:        GAP: Finite groups library with small class number
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://stertooy.github.io/SmallClassNr/
#Git-Clone:     https://github.com/stertooy/SmallClassNr
Source:         https://github.com/stertooy/SmallClassNr/releases/download/v%version/SmallClassNr-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.14

%description
The SmallClassNr package provides access to finite groups with small
class number. Currently, the package contains the finite groups of
class number at most 14.

%prep
%autosetup -n SmallClassNr-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
