#
# spec file for package gap-grape
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


Name:           gap-grape
Version:        4.9.0
Release:        0
Summary:        GAP: GRaph Algorithms using PErmutation groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/grape/
#Git-Clone:     https://github.com/gap-packages/grape
Source:         https://github.com/gap-packages/grape/releases/download/v%{version}/grape-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
Requires:       bliss
Requires:       gap-core >= 4.11
Requires:       nauty >= 2.8.6

%description
GRAPE is a package for computing with graphs and groups, and is
primarily designed for constructing and analysing graphs related to
groups, finite geometries, and designs.

%prep
%autosetup -n grape-%version
# Make sure bundled nauty is not built
rm -Rf ./nauty*

%build

%install
rm -Rf scripts doc/.Rhistory
%gappkg_simple_install

%files -f %name.files

%changelog
