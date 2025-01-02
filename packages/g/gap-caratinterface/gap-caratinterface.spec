#
# spec file for package gap-caratinterface
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gap-caratinterface
Version:        2.3.7
Release:        0
Summary:        GAP: Interface to CARAT, a crystallographic groups package
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/gap-packages/CaratInterface

Source:         https://www.math.uni-bielefeld.de/~gaehler/gap/CaratInterface/CaratInterface-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
BuildRequires:  xz
Requires:       carat
Requires:       gap-core >= 4.11.1
Suggests:       gap-cryst >= 4.1.24
Requires:       gap-io >= 4.8.0
Obsoletes:      gap-carat
Provides:       gap-carat

%description
This package provides GAP interface routines to some of the
stand-alone programs of CARAT, a package for the computation with
crystallographic groups. CARAT is to a large extent complementary to
the GAP package Cryst. In particular, it provides routines for the
computation of normalizers and conjugators of finite unimodular
groups in GL(n,Z), and routines for the computation of Bravais
groups, which are all missing in Cryst. A catalog of Bravais groups
up to dimension 6 is also provided.

%prep
%autosetup -n CaratInterface

%build
perl -pe 's{^#!/usr/local/bin/bash}{#!/bin/bash}g' \
	carat/tables/lattices/maximal.sh \
	carat/tables/lattices/check_trivilities.sh

%install
rm -rf configure scripts
%gappkg_simple_install

%files -f %name.files

%changelog
