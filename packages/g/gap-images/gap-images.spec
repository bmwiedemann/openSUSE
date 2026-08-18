#
# spec file for package gap-images
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


Name:           gap-images
Version:        1.4.2
Release:        0
Summary:        GAP: Minimal and Canonical images
License:        MPL-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/images/
#Git-Clone:	https://github.com/gap-packages/images
Source:         https://github.com/gap-packages/images/releases/download/v%version/images-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.13
Requires:       gap-datastructures >= 0.2.0
Requires:       gap-digraphs >= 1.0.0
Suggests:       gap-ferret >= 0.8.0
Suggests:       gap-vole >= 0.6.0

%description
A GAP package for finding minimal and canonical images in
permutation groups.

%prep
%autosetup -n images-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
