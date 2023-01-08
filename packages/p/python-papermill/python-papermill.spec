#
# spec file for package python-papermill
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


Name:           python-papermill
Version:        2.4.0
Release:        0
Summary:        Tool to parametrize and run Jupyter and nteract Notebooks
License:        BSD-3-Clause
URL:            https://github.com/nteract/papermill
Source:         https://files.pythonhosted.org/packages/source/p/papermill/papermill-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-ansiwrap
Requires:       python-click
Requires:       python-entrypoints
Requires:       python-nbclient >= 0.2.0
Requires:       python-nbformat >= 5.1.2
Requires:       python-requests >= 2.21.0
Requires:       python-tenacity
Requires:       python-tqdm >= 4.32.2
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-azure-datalake-store >= 0.0.30
Recommends:     python-azure-storage-blob
Recommends:     python-black
Recommends:     python-boto3
Recommends:     python-gcsfs >= 0.2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module ansiwrap}
BuildRequires:  %{python_module azure-datalake-store}
BuildRequires:  %{python_module azure-storage-blob}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module gcsfs}
BuildRequires:  %{python_module ipython >= 5.0}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module nbclient >= 0.2.0}
BuildRequires:  %{python_module nbformat >= 5.1.2}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest-env}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.21.0}
BuildRequires:  %{python_module tenacity}
BuildRequires:  %{python_module tqdm >= 4.32.2}
# /SECTION
%python_subpackages

%description
Papermill is a tool for parameterizing, executing,
and analyzing Jupyter Notebooks.

%prep
%autosetup -p1 -n papermill-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/papermill
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# different output type expected
donttest="TestBrokenNotebook2"
# no pyarrow
donttest="$donttest or test_hdfs_listdir"
%pytest -k "not ($donttest)"

%post
%python_install_alternative papermill

%postun
%python_uninstall_alternative papermill

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/papermill
%{python_sitelib}/papermill
%{python_sitelib}/papermill-%{version}*-info

%changelog
