#
# spec file for package gap-utils
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


Name:           gap-utils
Summary:        GAP: Utility functions in GAP
Version:        0.93
Release:        0
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/utils
#Git-Clone:     https://github.com/gap-packages/utils
Source:         https://github.com/gap-packages/utils/releases/download/v%version/utils-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
Requires:       gap-core >= 4.10.1
Suggests:       gap-curlinterface >= 2.3.0
BuildArch:      noarch

%description
The Utils package provides a collection of utility functions gleaned
from many packages.

%prep
%autosetup -n utils-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
