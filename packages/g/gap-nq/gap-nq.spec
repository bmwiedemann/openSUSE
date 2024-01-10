#
# spec file for package gap-nq
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


Name:           gap-nq
Version:        2.5.10
Release:        0
Summary:        GAP: Nilpotent Quotients of Finitely Presented Groups
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/nq/

#Git-Clone:	https://github.com/gap-packages/nq
Source:         https://github.com/gap-packages/nq/releases/download/v%version/nq-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-devel >= 4.9
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
Requires:       gap-core >= 4.9
Requires:       gap-polycyclic >= 2.11

%description
This package provides access to the ANU nilpotent quotient program
for computing nilpotent factor groups of finitely presented groups.

%prep
%setup -qn nq-%version

%build
%configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
rm -Rf "%buildroot/$moddir"/{aclocal*,autogen*,autom4*,config*,cnf,Makefile*,m4,src}
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
