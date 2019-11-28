#
# spec file for package python-asdf
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
%define         skip_python2 1
Name:           python-asdf
Version:        2.4.2
Release:        0
Summary:        Python tools to handle ASDF files
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/spacetelescope/asdf
Source0:        https://files.pythonhosted.org/packages/source/a/asdf/asdf-%{version}.tar.gz
# PATCH-FIX-UPSTREAM allow_recent_semantic_version.patch -- https://github.com/spacetelescope/asdf/pull/715
Patch0:         allow_recent_semantic_version.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.10
Requires:       python-astropy
Requires:       python-astropy-helpers
Requires:       python-jsonschema < 4
Requires:       python-jsonschema >= 2.3
Requires:       python-numpy >= 1.8
Requires:       python-semantic_version >= 2.8
Requires:       python-six >= 1.9.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module astropy-helpers}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module jsonschema < 4}
BuildRequires:  %{python_module jsonschema >= 2.3}
BuildRequires:  %{python_module numpy >= 1.8}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-openfiles >= 0.3.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module semantic_version >= 2.8}
BuildRequires:  %{python_module six >= 1.9.0}
# /SECTION
%python_subpackages

%description
The Advanced Scientific Data Format (ASDF) is a next-generation
interchange format for scientific data. This package contains the
Python implementation of the ASDF Standard.

%prep
%setup -q -n asdf-%{version}
%autopatch -p1
sed -i -e '/^#!\//, 1d' asdf/extern/RangeHTTPServer.py
sed -i 's/\r$//' asdf/tests/data/example_schema.json
chmod a-x asdf/tests/data/example_schema.json

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license licenses/*
%python3_only %{_bindir}/asdftool
%{python_sitelib}/*

%changelog
