#
# spec file for package python-pydocstyle
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pydocstyle
Version:        5.1.1
Release:        0
Summary:        Python docstring style checker
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/pydocstyle/
Source:         https://github.com/PyCQA/pydocstyle/archive/%{version}.tar.gz#/pydocstyle-%{version}.tar.gz
# Tests invoke pip and pycodestyle directly, when they should use sys.executable.
# https://github.com/PyCQA/pydocstyle/pull/403
Patch0:         integration-tests-invocation.patch
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pathlib}
# Tests invoke pip
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six > 1.10.0}
BuildRequires:  %{python_module snowballstemmer}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six > 1.10.0
Requires:       python-snowballstemmer
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-pep257 = %{version}
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
%patch0 -p1
dos2unix README.rst

# Disable pip fixture
sed -i /^pytestmark/d src/tests/test_integration.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pydocstyle
%{python_expand  #
sed -i -e '/^#! \//, 1d' %{buildroot}%{$python_sitelib}/pydocstyle/__main__.py
dos2unix %{buildroot}%{$python_sitelib}/pydocstyle/__main__.py
%fdupes %{buildroot}%{$python_sitelib}
}

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
%{python_sitelib}/pydocstyle-%{version}-py*.egg-info

%changelog
