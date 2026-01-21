#
# spec file for package python-jaraco.context
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-jaraco.context
Version:        6.1.0
Release:        0
Summary:        Tools to work with functools
License:        MIT
URL:            https://github.com/jaraco/jaraco.context
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.context/jaraco_context-%{version}.tar.gz
BuildRequires:  %{python_module backports.tarfile}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module portend}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports.tarfile
BuildArch:      noarch
%python_subpackages

%description
jaraco.functools Tools for working with functools.
Additional functools in the spirit of stdlib’s functools.

%prep
%autosetup -p1 -n jaraco_context-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not repo_context"

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst NEWS.rst
%{python_sitelib}/jaraco[_.]context-%{version}.dist-info
%dir %{python_sitelib}/jaraco
%dir %{python_sitelib}/jaraco/context
%{python_sitelib}/jaraco/context/*
%dir %{python_sitelib}/jaraco/context/__pycache__
%pycache_only %{python_sitelib}/jaraco/context/__pycache__/*

%changelog
