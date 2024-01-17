#
# spec file for package gap-anupq
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


Name:           gap-anupq
Version:        3.2.6
Release:        0
Summary:        GAP: Support for p-quotients and p-groups
License:        Artistic-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/anupq/
#Git-Clone:	https://github.com/gap-packages/anupq
Source:         https://github.com/gap-packages/anupq/releases/download/v%version/anupq-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9
Requires:       gap-autpgrp >= 1.5

%description
The ANUPQ package is a GAP4 interface to the ANU pq C program, which
provides access to implementations of the following algorithms:

* A p-quotient algorithm to compute a power-commutator presentation
  for a group of prime power order.
* A p-group generation algorithm to generate descriptions of groups
  of prime power order.
* A standard presentation algorithm used to compute a canonical
  power-commutator presentation of a p-group.
* An algorithm which can be used to compute the automorphism group of
  a p-group.

%prep
%autosetup -n anupq-%version

%build
%configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$moddir/"
rm -Rf aclocal* autom4* cnf config* m4 include src testPq.in standalone/TEST
perl -i -lpe 's{#!/usr/bin/env perl}{#!/usr/bin/perl}' testPq
popd
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
