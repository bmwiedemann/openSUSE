#
# spec file for package gap-itc
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-itc
Version:        1.5.1
Release:        0
Summary:        GAP: Interactive Todd-Coxeter
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/itc/
#Git-Clone:	https://github.com/gap-packages/itc
Source:         https://github.com/gap-packages/itc/releases/download/v%version/itc-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8
Requires:       gap-xgap >= 4.02

%description
This GAP package provides access to interactive Todd-Coxeter
computations with finitely presented groups.

%prep
%autosetup -n itc-%version

%build

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
popd

%files -f %name.files

%changelog
