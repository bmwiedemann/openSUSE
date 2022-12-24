#
# spec file for package plantri
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


Name:           plantri
Version:        5.3
Release:        0
Summary:        Programs for generating certain types of planar graphs
License:        Apache-2.0
Group:          Productivity/Scientific/Math
URL:            https://users.cecs.anu.edu.au/~bdm/plantri/
Source:         https://users.cecs.anu.edu.au/~bdm/plantri/plantri53.tar.gz
BuildRequires:  c_compiler

%description
plantri is a program that generates certain types of graphs that are
embedded on the sphere.

Exactly one member of each isomorphism class is output, using an
amount of memory almost independent of the number of graphs produced.
Isomorphisms are defined with respect to the imbeddings, so in some
cases outputs may be isomorphic as abstract graphs.

%prep
%autosetup -n plantri53

%build
%make_build CC="%__cc" CFLAGS="%optflags"

%install
mkdir -p "%buildroot/%_bindir"
cp -a plantri fullgen "%buildroot/%_bindir/"

%files
%_bindir/*

%changelog
