#
# spec file for package gap-cap
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


Name:           gap-cap
Version:        2024.11.02
%define sillyver 2024.11-02
Release:        0
Summary:        GAP: Categories, Algorithms and Programming
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/CAP
#Git-Clone:     https://github.com/homalg-project/CAP_project
Source:         https://github.com/homalg-project/CAP_project/releases/download/CAP-%sillyver/CAP-%sillyver.tar.gz
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
BuildArch:      noarch
Requires:       gap-core >= 4.13.0
Requires:       gap-io
Requires:       gap-toolsforhomalg >= 2023.11.01
Suggests:       gap-browse >= 1.5
Suggests:       gap-compilerforcap >= 2021.12.05

%description
CAP is a package for category theory. It facilitates the
implementation of specific instances of categories and provides a
language for writing generic categorical algorithms.

%prep
%autosetup -n CAP-%sillyver

%build
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
