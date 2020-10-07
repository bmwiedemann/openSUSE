#
# spec file for package python-nbclient
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
Name:           python-nbclient
Version:        0.5.0
Release:        0
Summary:        A client library for executing notebooks
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbclient
Source:         https://files.pythonhosted.org/packages/source/n/nbclient/nbclient-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-async_generator
Requires:       python-jupyter-client >= 6.1.5
Requires:       python-nbformat >= 5.0
Requires:       python-nest-asyncio
Requires:       python-traitlets >= 4.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module jupyter-client >= 6.1.5}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat >= 5.0}
BuildRequires:  %{python_module nest-asyncio}
BuildRequires:  %{python_module pytest >= 4.1}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module traitlets >= 4.2}
BuildRequires:  %{python_module xmltodict}
# /SECTION
%python_subpackages

%description
A client library for executing notebooks. Formally nbconvert's
ExecutePreprocessor.

NBClient is a tool for parameterizing andexecuting Jupyter Notebooks.

%prep
%setup -q -n nbclient-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_many_parallel_notebooks randomly fails - https://github.com/jupyter/nbclient/pull/74#issuecomment-635929953
%pytest -k 'not test_many_parallel_notebooks'

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/nbclient
%{python_sitelib}/nbclient-%{version}-py*.egg-info/

%changelog
