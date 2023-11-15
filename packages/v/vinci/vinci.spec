#
# spec file for package vinci
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


Name:           vinci
Version:        1.0.5
Release:        0
Summary:        Polytope volume computation program
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.multiprecision.org/vinci/index.html
Source:         https://www.multiprecision.org/downloads/%name-%version.tar.gz
Source2:        vinci.1
BuildRequires:  c_compiler

%description
Vinci implements several algorithms for computing the volume of a
full dimensional bounded polyhedron (polytope). The polytope must be
given by its vertex or hyperplane or double representation in the
lrslib or cddlib formats.

%prep
%autosetup -p1

%build
%make_build CC="%__cc" OPT="%optflags"

%install
mkdir -p "%buildroot/%_bindir" "%buildroot/%_mandir/man1"
cp -a vinci "%buildroot/%_bindir/"
cp -a %_sourcedir/*.1 "%buildroot/%_mandir/man1/"

%files
%_bindir/vinci
%_mandir/man*/*
%license COPYING
%doc manual.tex

%changelog
