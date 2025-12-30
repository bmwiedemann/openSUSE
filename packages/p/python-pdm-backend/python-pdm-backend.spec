#
# spec file for package python-pdm-backend
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


%{?sle15_python_module_pythons}
Name:           python-pdm-backend
Version:        2.4.6
Release:        0
Summary:        Backend used by PDM
License:        MIT
URL:            https://github.com/pdm-project/pdm-backend
Source:         https://files.pythonhosted.org/packages/source/p/pdm-backend/pdm_backend-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module editables}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  git-core
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
The build backend used by [PDM] that supports latest packaging standards.

%prep
%autosetup -p1 -n pdm_backend-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
git config --global user.email "o@bs.com"
git config --global user.name "Open Build Service"
%pytest

%files %{python_files}
%dir %{python_sitelib}/pdm
%{python_sitelib}/pdm/backend
%{python_sitelib}/pdm_backend-%{version}.dist-info

%changelog
