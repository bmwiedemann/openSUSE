#
# spec file for package python-papermill
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-papermill
Version:        1.2.1
Release:        0
License:        BSD-3-Clause
Summary:        Tool to parametrize and run Jupyter and nteract Notebooks
Url:            https://github.com/nteract/papermill
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/papermill/papermill-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module ansiwrap}
BuildRequires:  %{python_module azure-datalake-store}
BuildRequires:  %{python_module azure-storage-blob}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module gcsfs}
BuildRequires:  %{python_module ipython >= 5.0}
BuildRequires:  %{python_module jupyter-client}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module nbconvert >= 5.5}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tenacity}
BuildRequires:  %{python_module tqdm >= 4.29.1}
BuildRequires:  python-backports.tempfile
BuildRequires:  python-futures
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML
Requires:       python-ansiwrap
Requires:       python-click
Requires:       python-entrypoints
Requires:       python-future
Requires:       python-ipython >= 5.0
Requires:       python-jupyter-client
Requires:       python-nbconvert >= 5.5
Requires:       python-nbformat
Requires:       python-pandas
Requires:       python-requests >= 2.21.0
Requires:       python-six
Requires:       python-tenacity
Requires:       python-tqdm >= 4.29.1
Recommends:     python-boto3
Recommends:     python-gcsfs >= 0.2.0
Recommends:     python-azure-datalake-store >= 0.0.30
Recommends:     python-azure-storage-blob
BuildArch:      noarch

%python_subpackages

%description
Papermill is a tool for parameterizing, executing,
and analyzing Jupyter Notebooks.

%prep
%setup -q -n papermill-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python3_only %{_bindir}/papermill
%{python_sitelib}/*

%changelog
