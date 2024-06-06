#
# spec file for package gap-singular
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


Name:           gap-singular
Version:        2024.06.03
Release:        0
Summary:        GAP: An interface to Singular
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/singular/
#Git-Clone:     https://github.com/gap-packages/singular
Source:         https://github.com/gap-packages/singular/releases/download/v%version/singular-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
The singular package provides an interface from GAP to the
computer algebra system Singular.

%prep
%autosetup -n singular-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
