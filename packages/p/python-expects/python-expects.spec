#
# spec file for package python-expects
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-expects
Version:        0.9.0
Release:        0
Summary:        Expressive and extensible TDD/BDD assertion library for Python
License:        Apache-2.0
URL:            https://github.com/jaimegildesagredo/expects
Source:         https://files.pythonhosted.org/packages/source/e/expects/expects-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
"Expects" is an expressive and extensible TDD/BDD assertion library for
Python. Expects can be extended by defining new matchers.

%prep
%setup -q -n expects-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# This uses its own test runner called mamba, which isn't packaged

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/expects
%{python_sitelib}/expects-%{version}.dist-info

%changelog
