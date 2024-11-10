#
# spec file for package python-autoflake
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
Name:           python-autoflake
Version:        2.3.1
Release:        0
Summary:        Program to removes unused Python imports and variables
License:        MIT
URL:            https://github.com/myint/autoflake
Source:         https://files.pythonhosted.org/packages/source/a/autoflake/autoflake-%{version}.tar.gz
Requires:       python-tomli
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyflakes >= 3.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyflakes >= 3.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Autoflake removes unused imports and unused variables from Python
code. It makes use of pyflakes to do this.

By default, autoflake only removes unused imports for modules that
are part of the standard library. (Other modules may have side
effects that make them unsafe to remove automatically.) Removal of
unused variables is also disabled by default.

autoflake also removes useless pass statements.

%prep
%autosetup -p1 -n autoflake-%{version}
sed -i '1{/env python/d}' autoflake.py
chmod -x autoflake.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm %{buildroot}%{$python_sitelib}/{LICENSE,README.md,test*.py,__pycache__/test*.pyc}
%python_clone -a %{buildroot}%{_bindir}/autoflake
%fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pyunittest -v test_autoflake

%post
%python_install_alternative autoflake

%postun
%python_uninstall_alternative autoflake

%files %{python_files}
%doc AUTHORS.rst README.md
%license LICENSE
%python_alternative %{_bindir}/autoflake
%{python_sitelib}/autoflake.py*
%pycache_only %{python_sitelib}/__pycache__/autoflake*.pyc
%{python_sitelib}/autoflake-%{version}*-info

%changelog
