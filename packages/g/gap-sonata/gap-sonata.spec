#
# spec file for package gap-sonata
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


Name:           gap-sonata
Version:        2.9.6
Release:        0
Summary:        GAP: System of nearrings and their applications
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/sonata/
#Git-Clone:     https://github.com/gap-packages/sonata
Source:         https://github.com/gap-packages/sonata/releases/download/v%{version}/sonata-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Suggests:       gap-xgap >= 0

%description
The SONATA package provides methods for the construction and analysis
of finite nearrings.

%prep
%setup -qn sonata-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
