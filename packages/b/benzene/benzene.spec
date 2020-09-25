#
# spec file for package benzene
#
# Copyright (c) 2020 SUSE LLC
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


Name:           benzene
Version:        20130630
Release:        0
Summary:        Generator for nonisomorphic fusenes and benzenoids
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/sagemath/sage/tree/develop/build/pkgs/benzene
Source:         https://mirrors.mit.edu/sage/spkg/upstream/benzene/%name-%version.tar.bz2
BuildRequires:  gmp-devel >= 4.3.2

%description
Benzene is a program for the efficient generation of all
nonisomorphic fusenes and benzenoids with a given number of faces.
Fusenes are planar polycyclic hydrocarbons with all bounded faces
hexagons. Benzenoids are fusenes that are subgraphs of the hexagonal
lattice.

%prep
%autosetup -p1 -n src

%build
%make_build CFLAGS="%optflags"

%install
b="%buildroot"
mkdir -p "$b/%_bindir"
cp -a benzene "$b/%_bindir/"

%files
%_bindir/benzene

%changelog
