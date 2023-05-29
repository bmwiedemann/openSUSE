#
# spec file for package python-cogapp
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
Name:           python-cogapp
Version:        3.3.0
Release:        0
Summary:        A code generator for executing Python snippets in source files
License:        MIT
Group:          Development/Languages/Python
URL:            http://nedbatchelder.com/code/cog
Source:         https://files.pythonhosted.org/packages/source/c/cogapp/cogapp-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Cog is a file generation tool. It lets you use pieces of Python code
as generators in your source files to generate whatever text you
need.

%prep
%autosetup -p1 -n cogapp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv %{buildroot}%{_bindir}/cog.py %{buildroot}%{_bindir}/cog
%python_clone -a %{buildroot}%{_bindir}/cog

%check
# reverse -q from addopts in setup.cfg
%pytest -v

%post
%python_install_alternative cog

%postun
%python_uninstall_alternative cog

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/cog
%{python_sitelib}/cogapp
%{python_sitelib}/cogapp-%{version}*-info

%changelog
