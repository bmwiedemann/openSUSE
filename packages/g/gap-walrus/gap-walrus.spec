#
# spec file for package gap-walrus
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


Name:           gap-walrus
Version:        0.9991
Release:        0
Summary:        GAP: Proving assistant for hyperbolicity
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/walrus
#Git-Clone:     https://github.com/gap-packages/walrus
Source:         https://github.com/gap-packages/walrus/releases/download/v%version/walrus-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-gapdoc >= 1.5

%description
An implementation of hyperbolicity testing using an idea by Holt,
Neunhöffer, Parker and Roney-Dougal.

%prep
%autosetup -n walrus-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
