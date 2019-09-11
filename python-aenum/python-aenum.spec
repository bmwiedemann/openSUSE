#
# spec file for package python-aenum
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-aenum
Version:        2.2.1
Release:        0
Summary:        Advanced Enumerations, NamedTuples, and NamedConstants
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://bitbucket.org/stoneleaf/aenum
Source:         https://files.pythonhosted.org/packages/source/a/aenum/aenum-%{version}.tar.gz
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
%setup -q -n aenum-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B aenum/test.py
}

%files %{python_files}
%doc README aenum/CHANGES aenum/doc/*
%license aenum/LICENSE
%{python_sitelib}/*

%changelog
