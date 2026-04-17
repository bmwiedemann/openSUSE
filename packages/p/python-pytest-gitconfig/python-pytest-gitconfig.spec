#
# spec file for package python-pytest-gitconfig
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-pytest-gitconfig
Version:        0.9.0
Release:        0
Summary:        Provide a Git config sandbox for testing
License:        MIT
URL:            https://github.com/noirbizarre/pytest-gitconfig
Source:         https://files.pythonhosted.org/packages/source/p/pytest-gitconfig/pytest_gitconfig-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7.1.2}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  git
Requires:       python-pytest >= 7.1.2
BuildArch:      noarch
%python_subpackages

%description
Provide a Git config sandbox for testing


%prep
%autosetup -p1 -n pytest_gitconfig-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/pytest_gitconfig
%{python_sitelib}/pytest_gitconfig-%{version}.dist-info

%changelog
