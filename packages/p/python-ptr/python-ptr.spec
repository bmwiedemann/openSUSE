#
# spec file for package python-ptr
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
Name:           python-ptr
Version:        22.7.12
Release:        0
Summary:        Parallel asyncio Python setup(cfg|py) test runner
License:        MIT
URL:            https://github.com/facebookincubator/ptr
Source:         https://files.pythonhosted.org/packages/source/p/ptr/ptr-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
# Conflicts on site-packages/ptr.py
Conflicts:      python-pytest-runner
BuildArch:      noarch
%python_subpackages

%description
Parallel asyncio Python setup.(cfg|py) test runner.

%prep
%setup -q -n ptr-%{version}
sed -i 's/test_config/_test_config/' ptr_tests.py
sed -i '1{/^#!/d}' *.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ptr
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v ptr_tests

%post
%python_install_alternative ptr

%postun
%python_uninstall_alternative ptr

%files %{python_files}
%doc CHANGES.md README.md
%python_alternative %{_bindir}/ptr
%{python_sitelib}/ptr.py
%pycache_only %{python_sitelib}/__pycache__/ptr.*
%{python_sitelib}/ptr-%{version}.dist-info

%changelog
