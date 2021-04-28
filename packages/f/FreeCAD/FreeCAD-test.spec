#
# spec file for package FreeCAD-test
#
# Copyright (c) 2021 SUSE LLC
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


Name:           FreeCAD-test
Version:        0.19.0
Release:        0
Summary:        Meta source package that runs the FreeCAD testsuite when built
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Graphics/CAD
URL:            http://www.freecadweb.org/
BuildRequires:  FreeCAD
%if 0%{?suse_version} > 1500
BuildRequires:  gmsh
%endif

# Test suite fails on 32bit and I don't want to debug that anymore
ExcludeArch:    %ix86 %arm ppc s390 s390x

%description
This is just executing the test suite at build time.

%build
export LC_ALL="C.utf-8"
file=`mktemp`
if ! FreeCAD --console --write-log --log-file="$file" --run-test 0; then
  cat "$file"
  exit 1
fi

%changelog
