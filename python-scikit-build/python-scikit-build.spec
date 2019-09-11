#
# spec file for package python-scikit-build
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-scikit-build
Version:        0.10.0
Release:        0
Summary:        Improved build system generator for Python C/C++/Fortran/Cython extensions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/scikit-build/scikit-build
Source:         https://files.pythonhosted.org/packages/source/s/scikit-build/scikit-build-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools >= 28.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
Requires:       python-setuptools >= 28.0.0
Requires:       python-wheel >= 0.29.0
# SECTION test requirements
BuildRequires:  %{python_module Cython >= 0.25.1}
BuildRequires:  %{python_module codecov >= 2.0.5}
BuildRequires:  %{python_module coverage >= 4.2}
BuildRequires:  %{python_module flake8 >= 3.0.4}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module path.py >= 11.5.0}
BuildRequires:  %{python_module pytest >= 3.0.3}
BuildRequires:  %{python_module pytest-cov >= 2.4.0}
BuildRequires:  %{python_module pytest-mock >= 1.4.0}
BuildRequires:  %{python_module pytest-runner >= 2.9}
BuildRequires:  %{python_module pytest-virtualenv >= 1.2.5}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  %{python_module wheel >= 0.29.0}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  git-core
BuildRequires:  ninja
# /SECTION
%python_subpackages

%description
Improved build system generator for Python C/C++/Fortran/Cython extensions

%prep
%setup -q -n scikit-build-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}


%check
# setup.py install, develop, etc default to writing to /usr .
#  Tests need enhancing upstream or patching.
%pytest -k 'not (test_install_command or test_develop_command or test_test_command or test_hello_develop)'

%files %{python_files}
%doc AUTHORS.rst README.rst CONTRIBUTING.rst HISTORY.rst docs/
%license LICENSE
%{python_sitelib}/skbuild
%{python_sitelib}/scikit_build-%{version}-py*.egg-info

%changelog
