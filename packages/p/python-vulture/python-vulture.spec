#
# spec file for package python-vulture
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
Name:           python-vulture
Version:        2.13
Release:        0
Summary:        Python module for finding dead code
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jendrikseipp/vulture
Source:         https://files.pythonhosted.org/packages/source/v/vulture/vulture-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pint
Requires:       python-tomli
Requires:       python-typing-extensions
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest > 3.2.3}
BuildRequires:  %{python_module Pint}
BuildRequires:  %{python_module tomli}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
%python_subpackages

%description
Vulture finds unused code in Python programs. This is useful for
cleaning up and finding errors in code bases. Running Vulture
on both the library and test suite, untested code can be found.

Due to Python's dynamic nature, static code analyzers like Vulture are
likely to miss some dead code. Also, code that is only called implicitly
may be reported as unused.

Features:

* static code analysis
* only one module
* tests itself and has complete test coverage
* complements pyflakes and has the same output syntax
* sorts unused classes and functions by size with ``--sort-by-size``
* supports Python 2.6, 2.7 and 3.x

%prep
%setup -q -n vulture-%{version}
sed -i -e '/^#! \//, 1d' vulture/core.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/vulture

%check
rm setup.cfg
%pytest

%post
%python_install_alternative vulture

%postun
%python_uninstall_alternative vulture

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%python_alternative %{_bindir}/vulture
%{python_sitelib}/*

%changelog
