#
# spec file for package gap-uuid
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


Name:           gap-uuid
Version:        0.7
Release:        0
Summary:        GAP: UUIDs for GAP
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/uuid/
#Git-Clone:     https://github.com/gap-packages/uuid
Source:         https://github.com/gap-packages/uuid/releases/download/v%version/uuid-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-gapdoc >= 1.5

%description
This package provides functionality to create, query, and
manipulate RFC 4122-style UUIDs within GAP.

%prep
%autosetup -n uuid-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
