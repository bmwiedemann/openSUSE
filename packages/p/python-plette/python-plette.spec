#
# spec file for package python-plette
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


Name:           python-plette
Version:        2.0.2
Release:        0
Summary:        Structured Pipfile and Pipfile.lock models
License:        ISC
URL:            https://github.com/sarugaku/plette
Source:         https://github.com/sarugaku/plette/archive/refs/tags/v%{version}.tar.gz#/plette-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tomlkit
Suggests:       python-Cerberus
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Cerberus}
BuildRequires:  %{python_module invoke}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomlkit}
# /SECTION
%python_subpackages

%description
Structured Pipfile and Pipfile.lock models.

%prep
%autosetup -p1 -n plette-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_pipfile_load https://github.com/sarugaku/plette/issues/9
%pytest -k 'not test_pipfile_load'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/plette
%{python_sitelib}/plette-%{version}.dist-info

%changelog
