#
# spec file for package python-pycodestyle
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%global skip_python2 1
Name:           python-pycodestyle
Version:        2.9.1
Release:        0
Summary:        Python style guide checker
License:        MIT
Group:          Development/Languages/Python
URL:            https://pycodestyle.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/p/pycodestyle/pycodestyle-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Provides:       python-pep8 = %{version}
Obsoletes:      python-pep8 < %{version}
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
pycodestyle is a tool to check your Python code against some of the style
conventions in `PEP 8`.

This package used to be called ``pep8`` but was renamed to ``pycodestyle``
to reduce confusion.

%prep
%setup -q -n pycodestyle-%{version}
%autopatch -p1
sed -ri '1s/^#!.*//' pycodestyle.py

%build
%python_build

%install
%python_install
%python_clone %{buildroot}%{_bindir}/pycodestyle
ln -sf pycodestyle-%{python3_bin_suffix} %{buildroot}%{_bindir}/pycodestyle
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%post
%python_install_alternative pycodestyle

%postun
%python_uninstall_alternative pycodestyle

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/pycodestyle
%{_bindir}/pycodestyle-%{python_bin_suffix}
%{python_sitelib}/pycodestyle.py*
%pycache_only %{python_sitelib}/__pycache__/pycodestyle.*.py*
%{python_sitelib}/pycodestyle-%{version}-*.egg-info

%changelog
