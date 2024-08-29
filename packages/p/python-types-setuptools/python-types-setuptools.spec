#
# spec file for package python-types-setuptools
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
%{?sle15_python_module_pythons}
%define _unpackaged_files_terminate_build 0
Name:           python-types-setuptools
Version:        70.1.0.20240627
Release:        0
Summary:        Typing stubs for setuptools
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source:         https://files.pythonhosted.org/packages/source/t/types-setuptools/types-setuptools-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 70.1.1 }
BuildRequires:  %{python_module mypy }
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Typing stubs for setuptools

%prep
%autosetup -p1 -n types-setuptools-%{version}

%build
%pyproject_wheel

%check
export PYTHONPATH=.
%python_exec -m mypy -m distutils-stubs
%python_exec -m mypy -m pkg_resources-stubs
%python_exec -m mypy -m setuptools-stubs

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.md
%{python_sitelib}/distutils-stubs
%{python_sitelib}/pkg_resources-stubs
%{python_sitelib}/setuptools-stubs
%{python_sitelib}/types_setuptools-%{version}.dist-info


%changelog
