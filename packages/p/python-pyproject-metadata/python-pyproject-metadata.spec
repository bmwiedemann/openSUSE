#
# spec file for package python-pyproject-metadata
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


Name:           python-pyproject-metadata
Version:        0.6.1
Release:        0
Summary:        PEP 621 metadata parsing
License:        MIT
URL:            https://github.com/FFY00/python-pyproject-metadata
Source:         https://github.com/FFY00/python-pyproject-metadata/archive/refs/tags/%{version}.tar.gz#/python-pyproject-metadata-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module packaging >= 19}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 19
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli >= 1.0.0}
# /SECTION
%python_subpackages

%description
Dataclass for PEP 621 metadata with support for core metadata generation

This project does not implement the parsing of `pyproject.toml`
containing PEP 621 metadata.

Instead, given a Python data structure representing PEP 621 metadata (already
parsed), it will validate this input and generate a PEP 643-compliant metadata
file (e.g. `PKG-INFO`).

%prep
%setup -q -n python-pyproject-metadata-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/FFY00/python-pyproject-metadata/issues/41
donttest="(test_load and PEP and 508 and definitely)"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pyproject_metadata
%{python_sitelib}/pyproject_metadata-%{version}*-info

%changelog
