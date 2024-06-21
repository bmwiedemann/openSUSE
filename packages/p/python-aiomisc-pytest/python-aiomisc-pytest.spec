#
# spec file for package python-aiomisc-pytest
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
Name:           python-aiomisc-pytest
Version:        1.2.1
Release:        0
Summary:        pytest integration for aiomisc
License:        MIT
URL:            https://libraries.io/pypi/aiomisc-pytest
Source:         https://files.pythonhosted.org/packages/source/a/aiomisc_pytest/aiomisc_pytest-%{version}.tar.gz
BuildRequires:  %{python_module aiomisc >= 17}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest >= 8.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package contains a plugin for pytest.

%prep
%autosetup -p1 -n aiomisc_pytest-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# tests are only in github but github is not tagged :-(
# %check
# pytest

%files %{python_files}
%license COPYING
%doc README.md
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%{python_sitelib}/aiomisc_pytest.py
%{python_sitelib}/aiomisc_pytest-%{version}.dist-info

%changelog
