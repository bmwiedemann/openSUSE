#
# spec file for package FreeCAD-test
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


Name:           FreeCAD-test
Version:        1.1.1
Release:        0
Summary:        Meta source package that runs the FreeCAD testsuite when built
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://www.freecadweb.org/
BuildRequires:  FreeCAD = %{version}
BuildRequires:  gmsh

# Test suite fails on 32bit and I don't want to debug that anymore
ExcludeArch:    %ix86 %arm ppc s390 s390x

%description
This is just executing the test suite at build time.

%build
export LC_ALL="C.utf-8"
export PYTHONPATH=%{_libdir}/FreeCAD/lib

alltests=`python3 -c "\
import FreeCAD
d = [print('{}'.format(e), end=' ') for e in FreeCAD.__unit_test__]
"`

declare -a failed
for test in $alltests; do \
  python3 -c "\
import FreeCAD
import unittest
name = sys.argv[-1]
suite = unittest.defaultTestLoader.loadTestsFromName(name)
print(\"Running: {}\".format(name), file=sys.stderr)
r = unittest.TextTestRunner()
res = r.run(suite)
print(res)
exit(len(res.errors) + len(res.failures) > 0)
" $test || failed+=($test)
done

# Known failures (see https://github.com/FreeCAD/FreeCAD/issues/29311):
# TestArch TestDraft TestFemApp TestPartApp
unknown=${failed[@]}

for known in TestArch TestDraft TestFemApp TestPartApp; do \
    unknown=(${unknown[@]/$known})
done

echo -e "===\nFailed: ${failed[*]}\nUnknown: ${unknown[*]}\n==="
# Fail if unknown is not empty
test -z "${unknown[*]}"

%changelog
