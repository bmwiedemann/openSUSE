#
# spec file for package python-aenum
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


Name:           python-aenum
Version:        3.1.11
Release:        0
Summary:        Advanced Enumerations, NamedTuples, and NamedConstants
License:        BSD-3-Clause
URL:            https://github.com/ethanfurman/aenum
Source:         https://files.pythonhosted.org/packages/source/a/aenum/aenum-%{version}.tar.gz
# PATCH-FIX-UPSTREAM tempdir_missing.patch gh#ethanfurman/aenum#12 mcepl@suse.com
# Make test file into a proper one.
Patch0:         tempdir_missing.patch
# PATCH-FIX-UPSTREAM skip_failing_testcases.patch gh#ethanfurman/aenum#12 mcepl@suse.com
# Skip failing tests
Patch1:         skip_failing_testcases.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Advanced Enumerations (compatible with Python's stdlib Enum),
NamedTuples, and NamedConstants

AEnum includes a Python stdlib Enum-compatible data type, as well as
a metaclass-based NamedTuple implementation and a NamedConstant
class.

An Enum is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared
by identity, and the enumeration itself can be iterated over.  If
using Python 3 there is built-in support for unique values, multiple
values, auto-numbering, and suspension of aliasing (members with the
same value are not identical), plus the ability to have values
automatically bound to attributes.

A NamedTuple is a class-based, fixed-length tuple with a name for
each possible position accessible using attribute-access notation as
well as the standard index notation.

A NamedConstant is a class whose members cannot be rebound; it lacks
all other Enum capabilities, however; consequently, it can have
duplicate values.

%prep
%autosetup -p1 -n aenum-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pyunittest -v aenum.test

%files %{python_files}
%doc README.md aenum/CHANGES aenum/doc/*
%license aenum/LICENSE
%{python_sitelib}/aenum
%{python_sitelib}/aenum-%{version}*-info

%changelog
