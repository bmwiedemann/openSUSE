#
# spec file for package python-pydocstyle
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


%define skip_python2 1
Name:           python-pydocstyle
Version:        6.3.0
Release:        0
Summary:        Python docstring style checker
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/pydocstyle/
# Only the Repository Archive has the tests
Source:         https://github.com/PyCQA/pydocstyle/archive/%{version}.tar.gz#/pydocstyle-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module importlib-metadata >= 2 if %python-base < 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module snowballstemmer >= 2.2.0}
BuildRequires:  %{python_module tomli >= 1.2.3 if %python-base < 3.11}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-snowballstemmer >= 2.2.0
Requires:       (python-importlib-metadata >= 2 if python-base < 3.8)
Requires:       (python-tomli >= 1.2.3 if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-pep257 = %{version}-%{release}
Obsoletes:      python-pep257 < %{version}
BuildArch:      noarch
%python_subpackages

%description
pydocstyle is a static analysis tool for checking compliance with
Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box, but it should not
be considered a reference implementation.

The framework for checking docstring style is flexible, and custom
checks can be easily added, for example to cover NumPy docstring
conventions.

%prep
%setup -q -n pydocstyle-%{version}
# Stupid poetry!
sed -i '/version/ s/0.0.0-dev/%{version}/' pyproject.toml
# remove shebang
sed -i -e '/^#! \//, 1d' src/pydocstyle/__main__.py
# Disable pip fixture: We have the package already installed with a proper cmd
# Can't get the builddeps from network
sed -i /^pytestmark.*install_package/d src/tests/test_integration.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pydocstyle
%python_expand  %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=$(pwd)/src
%pytest

%post
%python_install_alternative pydocstyle

%postun
%python_uninstall_alternative pydocstyle

%files %{python_files}
%doc README.rst
%license LICENSE-MIT
%python_alternative %{_bindir}/pydocstyle
%{python_sitelib}/pydocstyle
%{python_sitelib}/pydocstyle-%{version}.dist-info

%changelog
