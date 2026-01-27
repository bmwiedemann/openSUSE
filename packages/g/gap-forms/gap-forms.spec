#
# spec file for package gap-forms
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


Name:           gap-forms
Version:        1.2.14
Release:        0
Summary:        GAP: Sesquilinear and quadratic forms
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/forms/
#Git-Clone:     https://github.com/gap-packages/forms
#Changelog:     <source>/doc/intro.xml
Source:         https://github.com/gap-packages/forms/releases/download/v%version/forms-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.9

%description
This package can be used for work with sesquilinear and quadratic
forms on finite vector spaces; objects that are used to describe
polar spaces and classical groups. It provides:

* A way to create and use sesquilinear and quadratic forms on finite
  vector spaces.
* An operation which finds an isometry between two forms of the same
  type.
* An operation which returns the forms left invariant by a matrix
  group.

%prep
%autosetup -n forms-%version
perl -i -lpe 's{^#!/usr/bin/env bash}{#!/bin/bash}g' *.sh

%build
# (rpmlint) not marked +x
rm doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
