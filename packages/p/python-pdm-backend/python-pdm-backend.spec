#
# spec file for package python-pdm-backend
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

%{?sle15_python_module_pythons}
Name:           python-pdm-backend
Version:        2.1.0
Release:        0
Summary:        Backend used by PDM
License:        MIT
URL:            https://github.com/pdm-project/pdm-backend
Source:         https://files.pythonhosted.org/packages/8f/aa/df3ad85bf4eeb7a7a3364610ca399f56812e4827cff6495c2a20e4bf1bb4/pdm_backend-2.1.0.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module editables}
BuildRequires:  git
BuildRequires:  fdupes
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
%pytest

%files %{python_files}
%dir %{python_sitelib}/pdm
%{python_sitelib}/pdm/backend
%{python_sitelib}/pdm_backend-%{version}.dist-info

%changelog
