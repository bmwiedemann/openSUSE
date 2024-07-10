#
# spec file for package gap-json
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gap-json
Version:        2.2.1
Release:        0
Summary:        GAP: Package for reading and writing JSON
License:        BSD-2-Clause
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/json/
#Git-Clone:     https://github.com/gap-packages/json
Source:         https://github.com/gap-packages/json/releases/download/v%version/json-%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.5

%description
Enhances GAP by the ability to read and write JSON files.

%prep
%autosetup -n json-%version

%build
./configure "%gapdir"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
find src -type f ! -name LICENSE -delete
popd

%files -f %name.files

%changelog
