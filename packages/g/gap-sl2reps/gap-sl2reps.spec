#
# spec file for package gap-sl2reps
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-sl2reps
Version:        1.1
Release:        0
Summary:        GAP: Construction of symmetric representations of SL(2,Z)
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            https://snw-0.github.io/sl2-reps
#Git-Clone:     https://github.com/snw-0/sl2-reps
Source:         https://github.com/snw-0/sl2-reps/releases/download/v%version/sl2-reps-%version.tar.gz
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
Requires:       gap-core >= 4.10

%description
The SL2Reps GAP package provides provides methods for constructing and testing
matrix presentations of the representations of SL(2,Z) whose kernels are
congruence subgroups of SL(2,Z).

%prep
%autosetup -n sl2-reps-%version

%build

%install
rm -v setup-gh-pages
%gappkg_simple_install

%files -f %name.files

%changelog
