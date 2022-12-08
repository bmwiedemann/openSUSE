#
# spec file for package FreeCAD-test
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


Name:           FreeCAD-test
Version:        0.20.2
Release:        0
Summary:        Meta source package that runs the FreeCAD testsuite when built
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://www.freecadweb.org/
BuildRequires:  FreeCAD = %{version}
%if 0%{?suse_version} > 1500
BuildRequires:  gmsh
%endif

# Test suite fails on 32bit and I don't want to debug that anymore
ExcludeArch:    %ix86 %arm ppc s390 s390x

%description
This is just executing the test suite at build time.

%build
export LC_ALL="C.utf-8"
export PYTHONPATH=%{_libdir}/FreeCAD/lib
python3 -c "\
import FreeCAD
import unittest
print(FreeCAD.__unit_test__, file=sys.stderr)
results = {}
for name in FreeCAD.__unit_test__:
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(name))
    print(\"Running: {}\".format(name), file=sys.stderr)
    r = unittest.TextTestRunner()
    res = r.run(suite)
    results[name] = res

totalerrors = 0
totalfailures = 0
for [name,res] in results.items():
    print(name, file=sys.stderr)
    print(res, file=sys.stderr)
    totalerrors += len(res.errors)
    totalfailures += len(res.failures)

exit((totalerrors + totalfailures) > 0)
"

%changelog
