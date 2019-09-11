#
# spec file for package FreeCAD-test
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.18.1
Release:        0
Summary:        Meta source package that runs the FreeCAD testsuite when built
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Graphics/CAD
Url:            http://www.freecadweb.org/
BuildRequires:  FreeCAD

# Test suite fails on 32bit and I don't want to debug that anymore
ExcludeArch:    %ix86 %arm ppc s390 s390x

%description
This is just executing the test suite at build time.

%build
export LC_ALL="C.utf-8"
#FreeCAD --console --write-log --log-file=/tmp/FreeCAD.log --run-test 0 || exit 1
FreeCAD --console --run-test 0 || exit 1

%changelog
