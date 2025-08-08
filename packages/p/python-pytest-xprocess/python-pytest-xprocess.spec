#
# spec file for package python-pytest-xprocess
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
Name:           python-pytest-xprocess
Version:        1.0.2
Release:        0
Summary:        A pytest plugin for managing processes across test runs
License:        MIT
URL:            https://github.com/pytest-dev/pytest-xprocess
Source:         https://files.pythonhosted.org/packages/source/p/pytest-xprocess/pytest-xprocess-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-test_process_initialization.patch gh#pytest-dev/pytest-xprocess#157
# This patch fixes tests in slow machines
Patch0:         fix-test_process_initialization.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-psutil
Requires:       python-pytest >= 2.8
BuildArch:      noarch
%python_subpackages

%description
This will provide a xprocess fixture which can be used to ensure that
external processes on which your application depends are up and running
during testing. You can also use it to start and pre-configure
test-specific databases (i.e. Postgres, Couchdb).

%prep
%autosetup -p1 -n pytest-xprocess-%{version}
rm -rvf tests/__pycache__
chmod -x README.rst

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/xprocess
%{python_sitelib}/pytest_xprocess-%{version}.dist-info

%changelog
