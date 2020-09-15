#
# spec file for package python-asdf
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-asdf
Version:        2.7.1
Release:        0
Summary:        Python tools to handle ASDF files
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/spacetelescope/asdf
Source0:        https://files.pythonhosted.org/packages/source/a/asdf/asdf-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.10
Requires:       python-astropy >= 3.0
Requires:       python-astropy-helpers
Requires:       python-jsonschema >= 3.0.2
Requires:       python-numpy >= 1.10
Requires:       python-semantic_version >= 2.8
Recommends:     python-lz4 >= 0.10
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module astropy >= 3.0}
BuildRequires:  %{python_module astropy-helpers}
BuildRequires:  %{python_module jsonschema >= 3.0.2}
BuildRequires:  %{python_module numpy >= 1.10}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-openfiles >= 0.3.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module semantic_version >= 2.8}
# /SECTION
%python_subpackages

%description
The Advanced Scientific Data Format (ASDF) is a next-generation
interchange format for scientific data. This package contains the
Python implementation of the ASDF Standard.

%prep
%setup -q -n asdf-%{version}
sed -i -e '/^#!\//, 1d' asdf/extern/RangeHTTPServer.py
sed -i 's/\r$//' asdf/tests/data/example_schema.json
chmod a-x asdf/tests/data/example_schema.json

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/asdftool
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative asdftool

%postun
%python_uninstall_alternative asdftool

%files %{python_files}
%doc CHANGES.rst README.rst
%license licenses/*
%python_alternative %{_bindir}/asdftool
%{python_sitelib}/*

%changelog
