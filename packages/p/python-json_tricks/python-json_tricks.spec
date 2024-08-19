#
# spec file for package python-json_tricks
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-json_tricks
Version:        3.17.3
Release:        0
Summary:        Extra features for Python's JSON
License:        BSD-3-Clause
URL:            https://github.com/mverleg/pyjson_tricks
Source:         https://github.com/mverleg/pyjson_tricks/archive/v%{version}.tar.gz#/pyjson_tricks-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#mverleg/pyjson_tricks#102
Patch0:         support-pytest-8.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-numpy
Recommends:     python-pandas
Recommends:     python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
# /SECTION
%python_subpackages

%description
The json_tricks package brings several pieces of functionality to
python handling of json files:

1. Store and load numpy arrays in human-readable format.
2. Store and load class instances both generic and customized.
3. Store and load date/times as a dictionary (including timezone).
4. Preserve map order {} using OrderedDict.
5. Allow for comments in json files by starting lines with #.
6. Sets, complex numbers, Decimal, Fraction, enums, compression, duplicate keys, ...

As well as compression and disallowing duplicate keys.

%prep
%autosetup -p1 -n pyjson_tricks-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/json_tricks
%{python_sitelib}/json_tricks-%{version}.dist-info

%changelog
