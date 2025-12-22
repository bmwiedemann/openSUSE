#
# spec file for package python-papermill
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-papermill
Version:        2.6.0
Release:        0
Summary:        Tool to parametrize and run Jupyter and nteract Notebooks
License:        BSD-3-Clause
URL:            https://github.com/nteract/papermill
Source:         https://files.pythonhosted.org/packages/source/p/papermill/papermill-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-ansicolors
Requires:       python-click
Requires:       python-entrypoints
Requires:       python-nbclient >= 0.2.0
Requires:       python-nbformat >= 5.2.0
Requires:       python-requests >= 2.21.0
Requires:       python-tenacity >= 5.0.2
Requires:       python-tqdm >= 4.32.2
%if 0%{?python_version_nodots} >= 312
Requires:       python-aiohttp
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-azure-identity >= 1.3.1
Recommends:     python-azure-storage-blob >= 12.1.0
Recommends:     python-black
Recommends:     python-boto3
Recommends:     python-gcsfs >= 0.2.0
Recommends:     (python-azure-datalake-store >= 0.0.30 with python-azure-datalake-store < 1)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aiohttp if %python-base >= 3.12}
BuildRequires:  %{python_module ansicolors}
# https://github.com/nteract/papermill/issues/825
# BuildRequires:  %%{python_module azure-datalake-store >= 0.0.30 with python-azure-datalake-store < 1}
BuildRequires:  %{python_module azure-identity >= 1.3.1}
BuildRequires:  %{python_module azure-storage-blob >= 12.1.0}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module gcsfs}
# for python-azure-storage-blob (https://build.opensuse.org/request/show/1083380#comments)
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module ipython >= 5.0}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module nbclient >= 0.2.0}
BuildRequires:  %{python_module nbformat >= 5.2}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pyarrow}
BuildRequires:  %{python_module pytest-env}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.21.0}
BuildRequires:  %{python_module tenacity >= 5.0.2}
BuildRequires:  %{python_module tqdm >= 4.32.2}
# /SECTION
%python_subpackages

%description
Papermill is a tool for parameterizing, executing,
and analyzing Jupyter Notebooks.

%prep
%autosetup -p1 -n papermill-%{version}
# docs subfolder not in sdist https://github.com/nteract/papermill/issues/737
sed -i '/docs_/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/papermill
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/nteract/papermill/issues/825
ignoretests="--ignore papermill/tests/test_adl.py"
# different output type expected
donttest="TestBrokenNotebook2"
# https://github.com/nteract/papermill/issues/828
donttest="$donttest or test_output_formatting"
%pytest $ignoretests -k "not ($donttest)"

%post
%python_install_alternative papermill

%postun
%python_uninstall_alternative papermill

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/papermill
%{python_sitelib}/papermill
%{python_sitelib}/papermill-%{version}.dist-info

%changelog
