#
# spec file for package python-branca
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


Name:           python-branca
Version:        0.6.0
Release:        0
Summary:        HTML+JS page generator
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/python-visualization/branca
# Only the Github archive has the tests. Requires manually setting the version for setuptools_scm below
Source:         https://github.com/python-visualization/branca/archive/v%{version}.tar.gz#/branca-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 41.2}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
# /SECTION
%python_subpackages

%description
Generate HTML+JS pages with Python.

%prep
%setup -q -n branca-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_rendering_utf8_iframe and test_rendering_figure_notebook require geckodriver
%pytest -k 'not (test_rendering_utf8_iframe or test_rendering_figure_notebook)'

%files %{python_files}
%doc CHANGES.txt README.md
%license LICENSE.txt
%{python_sitelib}/branca
%{python_sitelib}/branca-%{version}.dist-info

%changelog
