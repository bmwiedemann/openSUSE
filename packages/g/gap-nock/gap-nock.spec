#
# spec file for package gap-nock
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


Name:           gap-nock
Version:        1.5
Release:        0
Summary:        GAP: Comapct Clifford–Klein form existence obstruction computation
License:        MPL-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/NoCK/
#Git-Clone:	https://github.com/gap-packages/NoCK
Source:         https://github.com/gap-packages/NoCK/releases/download/v%version/NoCK-%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-corelg >= 1.20
Requires:       gap-sla >= 1.2

%description
The NoCK package is used for computing Tolzanoss obstruction for
compact Clifford–Klein forms.

%prep
%autosetup -n NoCK-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
