#
# spec file for package python-scikit-hep-testdata
#
# Copyright (c) 2021 SUSE LLC
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
%define srcname scikit-hep-testdata
%define modname %( echo %{srcname} | tr '-' '_' )
Name:           python-scikit-hep-testdata
Version:        0.4.4
Release:        0
Summary:        Example HEP files for testing and demonstrating
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scikit-hep/scikit-hep-testdata
Source:         https://github.com/scikit-hep/scikit-hep-testdata/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION Test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module importlib-resources}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A common package to provide example files (*e.g*. ROOT) for testing and
developing packages against.  The sample of files is representative of typical
files found "in the wild".

In addition to including some root files directly, this package adds some
simple helper methods to get larger files from common open-access data
repositories.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
# GH source doesn't allow proper detection of version: https://github.com/scikit-hep/scikit-hep-testdata/issues/40
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/scikit-hep-testdata
%python_clone -a %{buildroot}%{_bindir}/skhep-testdata

%check
# test_data_path needs network
%pytest -k 'not test_data_path'

%post
%python_install_alternative scikit-hep-testdata
%python_install_alternative skhep-testdata

%postun
%python_uninstall_alternative scikit-hep-testdata
%python_uninstall_alternative skhep-testdata

%files %{python_files}
%python_alternative %{_bindir}/scikit-hep-testdata
%python_alternative %{_bindir}/skhep-testdata
%{python_sitelib}/skhep_testdata/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
